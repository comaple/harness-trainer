#!/usr/bin/env python3
# Traceability: FR-022, STORY-018
"""
Deterministic evaluator for harness design artifacts.

The evaluator is intentionally dependency-free. It scores the current harness
catalog and worker contract artifacts, reports missing coverage, and can run a
small fixture suite for replacement-safety behavior.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parent
CATALOG = ROOT / "docs" / "harness" / "capability-catalog.md"
WORKER_CONTRACT = ROOT / "docs" / "harness" / "worker-contract.md"
SPEC = ROOT / "docs" / "specs" / "spec-replaceable-harness-capabilities" / "SPEC.md"
FIXTURE_DIR = ROOT / "examples" / "harness-eval"

REQUIRED_RUNTIME_FRS = [f"FR-{number:03d}" for number in range(13, 23)]
REQUIRED_CATALOG_FIELDS = [
    "Capability ID:",
    "Capability name:",
    "Product area:",
    "Owning FR IDs:",
    "Owning Story IDs:",
    "Intent:",
    "Public contract surface:",
    "State ownership:",
    "Emitted events:",
    "Failure behavior:",
    "Replacement boundary:",
    "Evaluator evidence:",
    "Trace evidence:",
]
REQUIRED_CONTRACT_FIELDS = [
    "function ID",
    "capability ID",
    "trigger name",
    "input shape",
    "output shape",
    "recoverable errors",
    "fail-closed errors",
    "timeout",
    "idempotency",
    "state reads",
    "state writes",
    "emitted events",
    "trace tags",
    "version expectations",
    "fixture expectations",
]
REPLACEMENT_CHECKS = [
    "contract_compatibility",
    "state_boundary_compatibility",
    "failure_mode_equivalence",
    "event_compatibility",
    "trace_compatibility",
    "regression_fixture_result",
]


@dataclass
class DimensionResult:
    name: str
    passed: bool
    missing: list[str]


def read_text(path: Path) -> str:
    if not path.is_file():
        return ""
    return path.read_text(encoding="utf-8")


def find_ids(pattern: str, text: str) -> set[str]:
    return set(re.findall(pattern, text))


def split_capability_sections(catalog_text: str) -> dict[str, str]:
    matches = list(re.finditer(r"^### (HC-\d{3}): .+$", catalog_text, flags=re.MULTILINE))
    sections: dict[str, str] = {}
    for index, match in enumerate(matches):
        start = match.start()
        end = matches[index + 1].start() if index + 1 < len(matches) else len(catalog_text)
        sections[match.group(1)] = catalog_text[start:end]
    return sections


def result(name: str, missing: list[str]) -> DimensionResult:
    return DimensionResult(name=name, passed=not missing, missing=missing)


def evaluate_current_artifacts() -> dict[str, Any]:
    catalog_text = read_text(CATALOG)
    contract_text = read_text(WORKER_CONTRACT)
    spec_text = read_text(SPEC)
    catalog_sections = split_capability_sections(catalog_text)
    contract_lower = contract_text.lower()

    dimensions = [
        evaluate_capability_coverage(catalog_text, catalog_sections),
        evaluate_contract_completeness(contract_text, contract_lower),
        evaluate_replacement_safety(contract_text, contract_lower),
        evaluate_failure_semantics(catalog_text, contract_lower),
        evaluate_state_boundaries(catalog_text, contract_lower),
        evaluate_policy_and_approval_safety(catalog_text, contract_text),
        evaluate_observability(catalog_text, contract_lower),
        evaluate_traceability(catalog_text, contract_text, spec_text),
    ]

    passed = sum(1 for dimension in dimensions if dimension.passed)
    score = round((passed / len(dimensions)) * 100, 2)
    missing_coverage = sorted(
        {
            item
            for dimension in dimensions
            for item in dimension.missing
            if item.startswith("FR-") or item.startswith("HC-")
        }
    )
    replacement_safety = "accepted" if dimensions[2].passed else "rejected"

    return {
        "harness_score": score,
        "status": "pass" if score == 100 else "fail",
        "missing_coverage": missing_coverage,
        "replacement_safety": replacement_safety,
        "dimensions": [
            {
                "name": dimension.name,
                "passed": dimension.passed,
                "missing": dimension.missing,
            }
            for dimension in dimensions
        ],
    }


def evaluate_capability_coverage(catalog_text: str, catalog_sections: dict[str, str]) -> DimensionResult:
    missing: list[str] = []
    if not CATALOG.is_file():
        missing.append(str(CATALOG.relative_to(ROOT)))
        return result("capability coverage", missing)

    for fr_id in REQUIRED_RUNTIME_FRS:
        if fr_id not in catalog_text:
            missing.append(fr_id)

    if not catalog_sections:
        missing.append("HC-* capability sections")

    for capability_id, section in catalog_sections.items():
        for field in REQUIRED_CATALOG_FIELDS:
            if field not in section:
                missing.append(f"{capability_id} missing {field.rstrip(':')}")

    return result("capability coverage", missing)


def evaluate_contract_completeness(contract_text: str, contract_lower: str) -> DimensionResult:
    missing: list[str] = []
    if not WORKER_CONTRACT.is_file():
        missing.append(str(WORKER_CONTRACT.relative_to(ROOT)))
        return result("contract completeness", missing)

    for field in REQUIRED_CONTRACT_FIELDS:
        if field.lower() not in contract_lower:
            missing.append(field)

    if "trigger style: synchronous call | event-triggered handler" not in contract_lower:
        missing.append("synchronous and event-triggered trigger styles")

    if "policy.evaluate_tool_call" not in contract_text:
        missing.append("policy check example contract")
    if "model.lookup_capabilities" not in contract_text:
        missing.append("model capability lookup example contract")

    return result("contract completeness", missing)


def evaluate_replacement_safety(contract_text: str, contract_lower: str) -> DimensionResult:
    missing: list[str] = []
    required_headings = [
        "Accepted Input Shape",
        "Compatible Output Shape",
        "Equivalent Failure Behavior",
        "Equivalent State Boundary",
        "Equivalent Event and Trace Evidence",
        "Compatible Timeout and Idempotency",
        "Fixture Result",
    ]
    for heading in required_headings:
        if heading not in contract_text:
            missing.append(heading)

    for phrase in [
        "replacement comparison fixtures",
        "must not downgrade a fail-closed error",
        "replacement implementation",
    ]:
        if phrase not in contract_lower:
            missing.append(phrase)

    return result("replacement safety", missing)


def evaluate_failure_semantics(catalog_text: str, contract_lower: str) -> DimensionResult:
    missing: list[str] = []
    if "Failure behavior:" not in catalog_text:
        missing.append("catalog failure behavior")
    if "recoverable errors" not in contract_lower:
        missing.append("recoverable errors")
    if "fail-closed errors" not in contract_lower:
        missing.append("fail-closed errors")
    if "forbidden next action" not in contract_lower:
        missing.append("fail-closed forbidden next action")
    return result("failure semantics", missing)


def evaluate_state_boundaries(catalog_text: str, contract_lower: str) -> DimensionResult:
    missing: list[str] = []
    if "State ownership:" not in catalog_text:
        missing.append("catalog state ownership")
    if "state reads" not in contract_lower:
        missing.append("state reads")
    if "state writes" not in contract_lower:
        missing.append("state writes")
    if "owner:" not in contract_lower:
        missing.append("state owner")
    return result("state boundaries", missing)


def evaluate_policy_and_approval_safety(catalog_text: str, contract_text: str) -> DimensionResult:
    missing: list[str] = []
    for phrase in [
        "HC-005",
        "Policy and Approval Gates",
        "policy.evaluate_tool_call",
        "needs_approval",
        "approval.requested",
    ]:
        if phrase not in catalog_text and phrase not in contract_text:
            missing.append(phrase)
    return result("policy and approval safety", missing)


def evaluate_observability(catalog_text: str, contract_lower: str) -> DimensionResult:
    missing: list[str] = []
    if "Emitted events:" not in catalog_text:
        missing.append("catalog emitted events")
    if "Trace evidence:" not in catalog_text:
        missing.append("catalog trace evidence")
    if "emitted events" not in contract_lower:
        missing.append("contract emitted events")
    if "trace tags" not in contract_lower:
        missing.append("contract trace tags")
    return result("observability", missing)


def evaluate_traceability(catalog_text: str, contract_text: str, spec_text: str) -> DimensionResult:
    missing: list[str] = []
    if not SPEC.is_file() or "Replaceable Harness Capabilities" not in spec_text:
        missing.append(str(SPEC.relative_to(ROOT)))
    for artifact, text in {
        "capability catalog": catalog_text,
        "worker contract": contract_text,
    }.items():
        if "Traceability:" not in text:
            missing.append(f"{artifact} traceability marker")
        if "docs/specs/spec-replaceable-harness-capabilities/SPEC.md" not in text:
            missing.append(f"{artifact} SPEC reference")

    if "FR-022" not in catalog_text:
        missing.append("FR-022 catalog evaluator coverage")
    return result("traceability", missing)


def evaluate_design_fixture(fixture: dict[str, Any]) -> dict[str, Any]:
    coverage = set(fixture.get("capability_coverage", []))
    missing_coverage = [fr_id for fr_id in REQUIRED_RUNTIME_FRS if fr_id not in coverage]
    checks = {
        "contract_complete": bool(fixture.get("contract_complete")),
        "replacement_safety": bool(fixture.get("replacement_safety")),
        "failure_semantics": bool(fixture.get("failure_semantics")),
        "state_boundaries": bool(fixture.get("state_boundaries")),
        "policy_and_approval_safety": bool(fixture.get("policy_and_approval_safety")),
        "observability": bool(fixture.get("observability")),
        "traceability": bool(fixture.get("traceability")),
    }
    missing = missing_coverage + [name for name, passed in checks.items() if not passed]
    passed_checks = sum(1 for passed in checks.values() if passed)
    coverage_score = 1 if not missing_coverage else 0
    score = round(((passed_checks + coverage_score) / (len(checks) + 1)) * 100, 2)
    return {
        "fixture": fixture.get("name", "unnamed fixture"),
        "type": "harness_design",
        "harness_score": score,
        "status": "pass" if not missing else "fail",
        "missing_coverage": missing,
    }


def evaluate_replacement_fixture(fixture: dict[str, Any]) -> dict[str, Any]:
    checks = fixture.get("checks", {})
    missing = [name for name in REPLACEMENT_CHECKS if not checks.get(name)]
    score = round(((len(REPLACEMENT_CHECKS) - len(missing)) / len(REPLACEMENT_CHECKS)) * 100, 2)
    return {
        "fixture": fixture.get("name", "unnamed replacement"),
        "type": "replacement_candidate",
        "replacement_safety": "accepted" if not missing else "rejected",
        "harness_score": score,
        "missing_coverage": missing,
    }


def evaluate_fixture(path: Path) -> dict[str, Any]:
    fixture = json.loads(path.read_text(encoding="utf-8"))
    fixture_type = fixture.get("type")
    if fixture_type == "harness_design":
        return evaluate_design_fixture(fixture)
    if fixture_type == "replacement_candidate":
        return evaluate_replacement_fixture(fixture)
    raise ValueError(f"{path}: unsupported fixture type {fixture_type!r}")


def run_self_test() -> dict[str, Any]:
    fixture_paths = sorted(FIXTURE_DIR.glob("*.json"))
    if not fixture_paths:
        return {
            "status": "fail",
            "failures": ["no evaluator fixtures found"],
            "fixtures": [],
        }

    failures: list[str] = []
    results: list[dict[str, Any]] = []
    for path in fixture_paths:
        fixture = json.loads(path.read_text(encoding="utf-8"))
        actual = evaluate_fixture(path)
        expected = fixture.get("expected")
        if fixture.get("type") == "harness_design":
            actual_value = actual["status"]
        else:
            actual_value = actual["replacement_safety"]
        if actual_value != expected:
            failures.append(f"{path.relative_to(ROOT)} expected {expected}, got {actual_value}")
        results.append(actual)

    return {
        "status": "pass" if not failures else "fail",
        "failures": failures,
        "fixtures": results,
    }


def print_text_report(report: dict[str, Any], self_test: dict[str, Any] | None) -> None:
    print(f"harness_score: {report['harness_score']}")
    print(f"status: {report['status']}")
    print(f"replacement_safety: {report['replacement_safety']}")
    print("missing_coverage:")
    if report["missing_coverage"]:
        for item in report["missing_coverage"]:
            print(f"  - {item}")
    else:
        print("  - none")
    print("dimensions:")
    for dimension in report["dimensions"]:
        status = "pass" if dimension["passed"] else "fail"
        print(f"  - {dimension['name']}: {status}")
        for missing in dimension["missing"]:
            print(f"    missing: {missing}")

    if self_test is not None:
        print(f"self_test: {self_test['status']}")
        for failure in self_test["failures"]:
            print(f"  failure: {failure}")


def main(argv: list[str]) -> int:
    parser = argparse.ArgumentParser(description="Evaluate harness design artifacts.")
    parser.add_argument("--json", action="store_true", help="print JSON report")
    parser.add_argument("--strict", action="store_true", help="exit non-zero unless score is 100")
    parser.add_argument("--self-test", action="store_true", help="run evaluator fixtures")
    args = parser.parse_args(argv)

    report = evaluate_current_artifacts()
    self_test = run_self_test() if args.self_test else None

    if args.json:
        output = {"evaluation": report}
        if self_test is not None:
            output["self_test"] = self_test
        print(json.dumps(output, indent=2, sort_keys=True))
    else:
        print_text_report(report, self_test)

    if args.strict and report["status"] != "pass":
        return 1
    if self_test is not None and self_test["status"] != "pass":
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
