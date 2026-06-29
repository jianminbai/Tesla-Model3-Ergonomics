from __future__ import annotations

from pathlib import Path
import re


ROOT = Path(__file__).resolve().parents[1]
SVG_DIR = ROOT / "assets" / "diagrams" / "svg"
INDEX = ROOT / "docs" / "diagram_index.md"

NAME_PATTERN = re.compile(r"^\d{2}_[a-z0-9_]+\.svg$")


def main() -> int:
    if not SVG_DIR.exists():
        print(f"[ERROR] SVG directory not found: {SVG_DIR}")
        return 1

    svgs = sorted(SVG_DIR.glob("*.svg"))
    if not svgs:
        print("[WARN] No SVG files found.")
        return 0

    print("# Diagram Check")
    print("")
    print(f"SVG directory: {SVG_DIR}")
    print(f"SVG count: {len(svgs)}")
    print("")

    bad_names = []
    for svg in svgs:
        ok = bool(NAME_PATTERN.match(svg.name))
        status = "OK" if ok else "BAD_NAME"
        print(f"- {status}: {svg.name}")
        if not ok:
            bad_names.append(svg.name)

    print("")
    if INDEX.exists():
        text = INDEX.read_text(encoding="utf-8")
        missing_in_index = [svg.name for svg in svgs if svg.name not in text]
        if missing_in_index:
            print("[WARN] SVG files not mentioned in docs/diagram_index.md:")
            for name in missing_in_index:
                print(f"  - {name}")
        else:
            print("[OK] All SVG files appear in diagram_index.md")
    else:
        print(f"[WARN] Missing index file: {INDEX}")

    if bad_names:
        print("")
        print("[ERROR] Some files do not match naming pattern: NN_english_name.svg")
        return 2

    print("")
    print("[OK] Diagram check completed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
