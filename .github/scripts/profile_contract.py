from __future__ import annotations

import re
import sys
from pathlib import Path
from urllib.parse import unquote, urlsplit
from xml.etree import ElementTree

ROOT = Path(__file__).resolve().parents[2]
FAILURES: list[str] = []


def fail(message: str) -> None:
    FAILURES.append(message)


def require_file(relative: str) -> None:
    if not (ROOT / relative).is_file():
        fail(f"required file missing: {relative}")


def require_dir(relative: str) -> None:
    if not (ROOT / relative).is_dir():
        fail(f"required directory missing: {relative}")


def require_text(path: str, values: list[str]) -> None:
    file_path = ROOT / path
    if not file_path.is_file():
        fail(f"cannot inspect missing file: {path}")
        return
    text = file_path.read_text(encoding="utf-8")
    for value in values:
        if value not in text:
            fail(f"{path}: missing required contract text {value!r}")


def forbid_text(path: Path, values: list[str]) -> None:
    text = path.read_text(encoding="utf-8", errors="replace")
    for value in values:
        if value in text:
            fail(f"{path.relative_to(ROOT)}: forbidden legacy/sensitive text {value!r}")


required_root_files = [
    ".gitignore",
    "README.md",
    "README.es.md",
    "README.zh-CN.md",
]
for item in required_root_files:
    require_file(item)

for item in ["brand", "evidence", ".github"]:
    require_dir(item)

required_assets = [
    "brand/assets/github-banner.svg",
    "brand/assets/github-banner-mobile.svg",
    "brand/assets/fdr-flagship.svg",
    "brand/assets/fdr-flagship-mobile.svg",
    "brand/assets/fdr-product-showcase.svg",
    "brand/assets/fdr-product-showcase-mobile.svg",
    "brand/assets/fdr-evidence-strip.svg",
    "brand/assets/engineering-depth.svg",
    "brand/assets/delivery-contexts.svg",
    "brand/assets/crohnoz-operating-model.svg",
    "brand/assets/portfolio-maturity.svg",
    "brand/assets/portfolio-maturity-mobile.svg",
    "brand/assets/professional-engagement.svg",
    "brand/assets/evidence-library.svg",
    "brand/assets/case-rental-operations.svg",
    "brand/assets/case-rental-operations-mobile.svg",
    "brand/assets/case-forge.svg",
    "brand/assets/case-forge-mobile.svg",
    "brand/assets/case-fresh-market.svg",
    "brand/assets/case-fresh-market-mobile.svg",
    "brand/assets/case-inclume.svg",
    "brand/assets/case-inclume-mobile.svg",
]
for item in required_assets:
    require_file(item)

required_cases = [
    "evidence/README.md",
    "evidence/fdr.md",
    "evidence/rental-operations.md",
    "evidence/forge.md",
    "evidence/fresh-market.md",
    "evidence/inclume.md",
]
for item in required_cases:
    require_file(item)

# The primary README must preserve flagship hierarchy, responsive visuals and case-study routes.
require_text(
    "README.md",
    [
        "FDR",
        "L2+",
        "evidence/forge.md",
        "evidence/fresh-market.md",
        "evidence/inclume.md",
        "brand/assets/github-banner-mobile.svg",
        "brand/assets/fdr-flagship-mobile.svg",
        "brand/assets/fdr-product-showcase-mobile.svg",
        "brand/assets/portfolio-maturity-mobile.svg",
        "Professional collaboration",
        "evidence/README.md",
        "crohnozlabs.cl/profile",
    ],
)

# Localized surfaces can translate labels; enforce semantic anchors rather than English badge literals.
for localized_readme in ["README.es.md", "README.zh-CN.md"]:
    require_text(
        localized_readme,
        [
            "FDR",
            "L2+",
            "evidence/forge.md",
            "evidence/fresh-market.md",
            "evidence/inclume.md",
            "L1",
            "brand/assets/github-banner-mobile.svg",
            "brand/assets/portfolio-maturity-mobile.svg",
            "evidence/README.md",
        ],
    )

# Case-study maturity/publication boundaries.
require_text("evidence/fdr.md", ["L2+", "ADVANCED PILOT", "sanitized", "fdr-flagship-mobile.svg"])
require_text("evidence/rental-operations.md", ["NON-FLAGSHIP", "case-rental-operations-mobile.svg"])
require_text("evidence/forge.md", ["L1 · PROTOTYPE / R&D", "case-forge-mobile.svg"])
require_text("evidence/fresh-market.md", ["L1 · PROTOTYPE / R&D", "case-fresh-market-mobile.svg"])
require_text("evidence/inclume.md", ["L1 · EARLY PRODUCT", "case-inclume-mobile.svg"])

# The evidence index must expose every current case in the intended hierarchy.
require_text(
    "evidence/README.md",
    [
        "01 · Flagship engineering case",
        "02 · Selected operational engineering",
        "03 · Product R&D",
        "fdr-flagship-mobile.svg",
        "case-rental-operations-mobile.svg",
        "case-forge-mobile.svg",
        "case-fresh-market-mobile.svg",
        "case-inclume-mobile.svg",
    ],
)

# The profile repository is editorial/portfolio infrastructure, not an application build dump.
forbidden_root_entries = {
    "venv",
    ".venv",
    "build",
    "dist",
    "Crohnoz.zip",
    "Crohnoz.spec",
    "crohnoz_gui.py",
    "README.txt",
}
for name in forbidden_root_entries:
    if (ROOT / name).exists():
        fail(f"forbidden legacy root entry returned: {name}")

# Mermaid was replaced by sanitized branded public diagrams.
for markdown in (ROOT / "evidence").glob("*.md"):
    forbid_text(markdown, ["```mermaid"])

# Basic public-secret guardrail for text surfaces.
sensitive_markers = [
    "-----BEGIN PRIVATE KEY-----",
    "sk-proj-",
    "ghp_",
    "SUPABASE_SERVICE_ROLE_KEY=",
]
for path in [*ROOT.glob("*.md"), *(ROOT / "brand").glob("*.md"), *(ROOT / "evidence").glob("*.md")]:
    forbid_text(path, sensitive_markers)

# Validate every public SVG as XML so malformed visual assets cannot silently land.
for svg in (ROOT / "brand" / "assets").glob("*.svg"):
    try:
        ElementTree.parse(svg)
    except ElementTree.ParseError as exc:
        fail(f"malformed SVG {svg.relative_to(ROOT)}: {exc}")

# Validate repository-local Markdown/HTML references, ignoring fenced code examples.
markdown_link = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")
html_link = re.compile(r"(?:href|src|srcset)=\"([^\"]+)\"")
fenced_code = re.compile(r"```.*?```", re.DOTALL)

for markdown in [*ROOT.glob("*.md"), *(ROOT / "brand").glob("*.md"), *(ROOT / "evidence").glob("*.md")]:
    text = markdown.read_text(encoding="utf-8", errors="replace")
    inspectable = fenced_code.sub("", text)
    candidates = markdown_link.findall(inspectable) + html_link.findall(inspectable)
    for raw_target in candidates:
        target = raw_target.strip().split()[0]
        if not target or target.startswith(("http://", "https://", "mailto:", "#", "data:")):
            continue
        parsed = urlsplit(target)
        local = unquote(parsed.path)
        if not local:
            continue
        resolved = (markdown.parent / local).resolve()
        try:
            resolved.relative_to(ROOT.resolve())
        except ValueError:
            fail(f"{markdown.relative_to(ROOT)}: local reference escapes repository: {target}")
            continue
        if not resolved.exists():
            fail(f"{markdown.relative_to(ROOT)}: broken local reference: {target}")

if FAILURES:
    print("\nCrohnoz public profile contract: FAIL\n", file=sys.stderr)
    for item in FAILURES:
        print(f"- {item}", file=sys.stderr)
    raise SystemExit(1)

print("Crohnoz public profile contract: PASS")
