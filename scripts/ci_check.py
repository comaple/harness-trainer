#!/usr/bin/env python3
# Traceability: FR-005, FR-007, FR-008, FR-009, STORY-002, STORY-003, STORY-004, STORY-005
"""
Repository quality gate for harness-trainer.

The gate is intentionally dependency-free so it can run locally, in CI, and
before commits without bootstrapping a toolchain.
"""

from __future__ import annotations

import os
import re
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

REQUIRED_FILES = [
    "AGENTS.md",
    "README.md",
    ".gitignore",
    ".github/workflows/ci.yml",
    "docs/prd.md",
    "docs/architecture.md",
    "docs/epics/EPIC-001-governance-and-gates.md",
    "docs/stories/STORY-001-project-charter.md",
    "docs/stories/STORY-002-traceability-gate.md",
    "docs/stories/STORY-003-branch-workflow-gate.md",
    "docs/stories/STORY-004-feature-branch-naming.md",
    "docs/stories/STORY-005-prd-requirement-classes.md",
    "scripts/ci_check.py",
]

REQUIRED_GITIGNORE_PATTERNS = [
    "__pycache__/",
    ".venv/",
    "harness_results.tsv",
    "harness_run.log",
]

UNTRACKED_ONLY_FILES = [
    "harness_results.tsv",
    "harness_run.log",
    "results.tsv",
]

LOCAL_MARKDOWN_LINK = re.compile(r"\[[^\]]+\]\((?!https?://|mailto:|#)([^)]+)\)")
BR_ID = re.compile(r"\bBR-\d{3}\b")
UR_ID = re.compile(r"\bUR-\d{3}\b")
FR_ID = re.compile(r"\bFR-\d{3}\b")
NFR_ID = re.compile(r"\bNFR-\d{3}\b")
EPIC_ID = re.compile(r"\bEPIC-\d{3}\b")
STORY_ID = re.compile(r"\bSTORY-\d{3}\b")
TRACEABILITY_MARKER = re.compile(r"Traceability:\s*(?P<ids>.+)")
SOURCE_SUFFIXES = {".py", ".yml", ".yaml", ".js", ".ts", ".tsx", ".jsx", ".sh"}
FEATURE_BRANCH = re.compile(r"^feat/[a-z0-9][a-z0-9-]*[a-z0-9]$")
REQUIRED_PRD_SECTIONS = [
    "## Product",
    "## Requirement Taxonomy",
    "## Business Requirements",
    "## User Requirements",
    "## Functional Requirements",
    "## Non-Functional Requirements",
    "## Constraints",
    "## Assumptions and Dependencies",
    "## Out of Scope",
    "## Success Metrics",
]


def fail(message: str) -> None:
    print(f"FAIL: {message}")
    raise SystemExit(1)


def ok(message: str) -> None:
    print(f"OK:   {message}")


def run_git(args: list[str]) -> str:
    try:
        return subprocess.check_output(["git", *args], cwd=ROOT, text=True).strip()
    except (OSError, subprocess.CalledProcessError) as error:
        fail(f"git {' '.join(args)} failed: {error}")


def ensure_repo_root() -> None:
    top = Path(run_git(["rev-parse", "--show-toplevel"])).resolve()
    if top != ROOT:
        fail(f"script root mismatch: expected {ROOT}, git top-level is {top}")
    ok("running at repository root")


def ensure_required_files() -> None:
    missing = [path for path in REQUIRED_FILES if not (ROOT / path).is_file()]
    if missing:
        fail(f"missing required files: {', '.join(missing)}")
    ok("required project files exist")


def ensure_gitignore_patterns() -> None:
    gitignore = (ROOT / ".gitignore").read_text(encoding="utf-8")
    missing = [pattern for pattern in REQUIRED_GITIGNORE_PATTERNS if pattern not in gitignore]
    if missing:
        fail(f".gitignore missing patterns: {', '.join(missing)}")
    ok(".gitignore protects local/generated files")


def ensure_generated_files_untracked() -> None:
    tracked = set(run_git(["ls-files"]).splitlines())
    bad = [path for path in UNTRACKED_ONLY_FILES if path in tracked]
    if bad:
        fail(f"generated result files must not be tracked: {', '.join(bad)}")
    ok("generated experiment files are not tracked")


def iter_project_files() -> list[Path]:
    files: list[Path] = []
    for dirpath, dirnames, filenames in os.walk(ROOT):
        rel_dir = Path(dirpath).relative_to(ROOT)
        if ".git" in dirnames:
            dirnames.remove(".git")
        if "__pycache__" in dirnames:
            dirnames.remove("__pycache__")
        if ".venv" in dirnames:
            dirnames.remove(".venv")
        for filename in filenames:
            path = rel_dir / filename
            files.append(ROOT / path)
    return files


def ensure_no_nested_git_repos() -> None:
    nested = []
    for dirpath, dirnames, _ in os.walk(ROOT):
        rel_dir = Path(dirpath).relative_to(ROOT)
        if rel_dir == Path("."):
            continue
        if ".git" in dirnames:
            nested.append(str(rel_dir / ".git"))
    if nested:
        fail(f"nested git repositories are not allowed: {', '.join(nested)}")
    ok("no nested git repositories")


def ensure_markdown_local_links() -> None:
    broken = []
    for path in iter_project_files():
        if path.suffix.lower() != ".md":
            continue
        text = path.read_text(encoding="utf-8")
        for match in LOCAL_MARKDOWN_LINK.finditer(text):
            target = match.group(1).strip()
            target = target.split("#", 1)[0]
            if not target:
                continue
            target_path = (path.parent / target).resolve()
            try:
                target_path.relative_to(ROOT)
            except ValueError:
                broken.append(f"{path.relative_to(ROOT)} -> {match.group(1)} escapes repo")
                continue
            if not target_path.exists():
                broken.append(f"{path.relative_to(ROOT)} -> {match.group(1)}")
    if broken:
        fail("broken local Markdown links:\n  " + "\n  ".join(broken))
    ok("local Markdown links resolve")


def ensure_text_files_have_trailing_newline() -> None:
    checked_suffixes = {".md", ".py", ".yml", ".yaml", ".toml", ".txt"}
    missing = []
    for path in iter_project_files():
        if path.suffix.lower() not in checked_suffixes:
            continue
        data = path.read_bytes()
        if data and not data.endswith(b"\n"):
            missing.append(str(path.relative_to(ROOT)))
    if missing:
        fail("text files missing trailing newline: " + ", ".join(missing))
    ok("text files have trailing newlines")


def ids_in(path: Path, pattern: re.Pattern[str]) -> set[str]:
    return set(pattern.findall(path.read_text(encoding="utf-8")))


def ensure_prd_requirement_classes() -> None:
    prd = ROOT / "docs" / "prd.md"
    text = prd.read_text(encoding="utf-8")

    missing_sections = [section for section in REQUIRED_PRD_SECTIONS if section not in text]
    if missing_sections:
        fail("docs/prd.md missing required sections: " + ", ".join(missing_sections))

    required_ids = {
        "business requirements": (BR_ID, "BR-XXX"),
        "user requirements": (UR_ID, "UR-XXX"),
        "functional requirements": (FR_ID, "FR-XXX"),
        "non-functional requirements": (NFR_ID, "NFR-XXX"),
    }
    missing_ids = [
        f"{label} ({example})"
        for label, (pattern, example) in required_ids.items()
        if not pattern.search(text)
    ]
    if missing_ids:
        fail("docs/prd.md missing stable IDs for: " + ", ".join(missing_ids))

    ok("PRD requirement classes are present")


def ensure_agile_traceability() -> tuple[set[str], set[str], set[str]]:
    prd = ROOT / "docs" / "prd.md"
    fr_ids = ids_in(prd, FR_ID)
    if not fr_ids:
        fail("docs/prd.md must define at least one FR-XXX requirement")

    epic_files = sorted((ROOT / "docs" / "epics").glob("EPIC-*.md"))
    story_files = sorted((ROOT / "docs" / "stories").glob("STORY-*.md"))
    if not epic_files:
        fail("docs/epics must contain at least one EPIC-XXX markdown file")
    if not story_files:
        fail("docs/stories must contain at least one STORY-XXX markdown file")

    epic_ids: set[str] = set()
    epic_story_refs: set[str] = set()
    for path in epic_files:
        text = path.read_text(encoding="utf-8")
        ids = set(EPIC_ID.findall(text)) | set(EPIC_ID.findall(path.name))
        if not ids:
            fail(f"{path.relative_to(ROOT)} must declare an EPIC-XXX id")
        epic_ids.update(ids)
        refs = set(FR_ID.findall(text))
        missing = sorted(refs - fr_ids)
        if missing:
            fail(f"{path.relative_to(ROOT)} references missing FR ids: {', '.join(missing)}")
        if not refs:
            fail(f"{path.relative_to(ROOT)} must reference at least one FR-XXX id")
        epic_story_refs.update(STORY_ID.findall(text))

    story_ids: set[str] = set()
    story_fr_refs: set[str] = set()
    for path in story_files:
        text = path.read_text(encoding="utf-8")
        ids = set(STORY_ID.findall(text)) | set(STORY_ID.findall(path.name))
        if not ids:
            fail(f"{path.relative_to(ROOT)} must declare a STORY-XXX id")
        story_ids.update(ids)

        story_epics = set(EPIC_ID.findall(text))
        if not story_epics:
            fail(f"{path.relative_to(ROOT)} must reference an EPIC-XXX id")
        missing_epics = sorted(story_epics - epic_ids)
        if missing_epics:
            fail(f"{path.relative_to(ROOT)} references missing epic ids: {', '.join(missing_epics)}")

        refs = set(FR_ID.findall(text))
        if not refs:
            fail(f"{path.relative_to(ROOT)} must reference at least one FR-XXX id")
        missing_frs = sorted(refs - fr_ids)
        if missing_frs:
            fail(f"{path.relative_to(ROOT)} references missing FR ids: {', '.join(missing_frs)}")
        story_fr_refs.update(refs)

        if "## Implementation Plan" not in text:
            fail(f"{path.relative_to(ROOT)} must include ## Implementation Plan")

    missing_story_docs = sorted(epic_story_refs - story_ids)
    if missing_story_docs:
        fail("epics reference missing story files: " + ", ".join(missing_story_docs))

    unplanned_frs = sorted(fr_ids - story_fr_refs)
    if unplanned_frs:
        fail("PRD requirements are not covered by stories: " + ", ".join(unplanned_frs))

    ok("PRD, epics, and stories are traceable")
    return fr_ids, epic_ids, story_ids


def ensure_code_traceability(fr_ids: set[str], story_ids: set[str]) -> None:
    missing = []
    bad_refs = []
    for path in iter_project_files():
        rel = path.relative_to(ROOT)
        if path.suffix.lower() not in SOURCE_SUFFIXES:
            continue
        text = path.read_text(encoding="utf-8")
        marker = TRACEABILITY_MARKER.search(text)
        if not marker:
            missing.append(str(rel))
            continue
        marker_text = marker.group("ids")
        refs = set(FR_ID.findall(marker_text))
        stories = set(STORY_ID.findall(marker_text))
        if not refs or not stories:
            bad_refs.append(f"{rel}: marker must contain FR-XXX and STORY-XXX")
            continue
        unknown_frs = sorted(refs - fr_ids)
        unknown_stories = sorted(stories - story_ids)
        if unknown_frs or unknown_stories:
            details = []
            if unknown_frs:
                details.append("unknown FR " + ", ".join(unknown_frs))
            if unknown_stories:
                details.append("unknown story " + ", ".join(unknown_stories))
            bad_refs.append(f"{rel}: {'; '.join(details)}")
    if missing:
        fail("source files missing traceability markers: " + ", ".join(missing))
    if bad_refs:
        fail("invalid source traceability:\n  " + "\n  ".join(bad_refs))
    ok("source files bind to FR and Story IDs")


def commit_range_from_env() -> list[str]:
    before = os.environ.get("GITHUB_EVENT_BEFORE")
    sha = os.environ.get("GITHUB_SHA")
    if before and sha and not set(before) == {"0"}:
        try:
            output = subprocess.check_output(
                ["git", "log", "--format=%s%n%b%x00", f"{before}..{sha}"],
                cwd=ROOT,
                text=True,
            )
            return [item.strip() for item in output.split("\0") if item.strip()]
        except subprocess.CalledProcessError:
            return []
    return []


def ensure_commit_traceability(fr_ids: set[str], story_ids: set[str]) -> None:
    messages = commit_range_from_env()
    if not messages:
        ok("commit-message traceability skipped outside CI commit range")
        return
    errors = []
    for message in messages:
        subject = message.splitlines()[0]
        refs = set(FR_ID.findall(message))
        stories = set(STORY_ID.findall(message))
        if not refs or not stories:
            errors.append(f"{subject}: missing FR-XXX or STORY-XXX")
            continue
        unknown_frs = sorted(refs - fr_ids)
        unknown_stories = sorted(stories - story_ids)
        if unknown_frs or unknown_stories:
            errors.append(
                f"{subject}: unknown ids "
                f"{', '.join(unknown_frs + unknown_stories)}"
            )
    if errors:
        fail("commit messages are not traceable:\n  " + "\n  ".join(errors))
    ok("commit messages bind to FR and Story IDs")


def ensure_branch_workflow() -> None:
    if not os.environ.get("GITHUB_ACTIONS"):
        ok("branch workflow check skipped outside GitHub Actions")
        return

    event_name = os.environ.get("GITHUB_EVENT_NAME", "")
    ref_name = os.environ.get("GITHUB_REF_NAME", "")
    base_ref = os.environ.get("GITHUB_BASE_REF", "")
    head_ref = os.environ.get("GITHUB_HEAD_REF", "")

    if event_name == "pull_request":
        if base_ref != "main":
            fail(f"pull requests must target main, got {base_ref!r}")
        if not FEATURE_BRANCH.fullmatch(head_ref):
            fail(
                "pull requests must originate from feat/<feature-description>, "
                f"got {head_ref!r}"
            )
        ok(f"pull request branch flow is {head_ref} -> main")
        return

    if event_name == "push":
        if ref_name != "main" and not FEATURE_BRANCH.fullmatch(ref_name):
            fail(
                "push CI is only allowed on main or feat/<feature-description>, "
                f"got {ref_name!r}"
            )
        ok(f"push branch {ref_name!r} is allowed")
        return

    ok(f"branch workflow check skipped for event {event_name!r}")


def ensure_bmad_config_if_present() -> None:
    config = ROOT / "_bmad" / "config.toml"
    if not config.exists():
        ok("BMad project config not present in repo yet")
        return
    text = config.read_text(encoding="utf-8")
    required = [
        'project_name = "harness-trainer"',
        'output_folder = "{project-root}/docs"',
    ]
    missing = [item for item in required if item not in text]
    if missing:
        fail("BMad config missing expected settings: " + ", ".join(missing))
    ok("BMad config matches harness-trainer project")


def main() -> int:
    print(f"Repository: {ROOT}")
    ensure_repo_root()
    ensure_required_files()
    ensure_gitignore_patterns()
    ensure_generated_files_untracked()
    ensure_no_nested_git_repos()
    ensure_markdown_local_links()
    ensure_text_files_have_trailing_newline()
    ensure_prd_requirement_classes()
    fr_ids, _epic_ids, story_ids = ensure_agile_traceability()
    ensure_code_traceability(fr_ids, story_ids)
    ensure_commit_traceability(fr_ids, story_ids)
    ensure_branch_workflow()
    ensure_bmad_config_if_present()
    print("CI gate passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
