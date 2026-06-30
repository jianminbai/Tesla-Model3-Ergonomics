from __future__ import annotations

import io
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[1]

REQUIRED_FILES = [
    "README.md",
    "QUICKSTART.md",
    "ROADMAP.md",
    "CONTRIBUTING.md",
    "requirements.txt",
    "mkdocs.yml",
    "book/00-前言.md",
    "book/01-驾驶为什么会让人疼.md",
    "book/02-骨盆决定受力.md",
    "book/03-坐骨与软组织受力.md",
    "book/04-Tesla_Model3座椅结构分析.md",
    "book/05-座椅调节流程.md",
    "book/06-踏板几何与右腿疲劳.md",
    "book/07-症状决策树.md",
    "book/08-康复与办公椅联动.md",
    "book/09-实验系统与量化记录.md",
    "book/10-可视化插图与图表体系.md",
    "book/11-GitHub_Pages发布与项目运营.md",
    "docs/quick_diagnosis_table.md",
    "docs/office_chair_checklist.md",
    "docs/experiment_system.md",
    "docs/case_library.md",
    "docs/model_y_and_other_cars.md",
    "docs/english_summary.md",
    "docs/diagram_index.md",
    "docs/visual_style_guide.md",
    "docs/github_pages_publish_guide.md",
    "docs/navigation_map.md",
    "assets/diagrams/svg/01_pressure_distribution.svg",
    "assets/diagrams/svg/02_pelvis_postures.svg",
    "assets/diagrams/svg/03_model3_seat_top_view.svg",
    "assets/diagrams/svg/04_seat_height_force_change.svg",
    "assets/diagrams/svg/05_pedal_dynamic_load_chain.svg",
    "assets/diagrams/svg/06_symptom_decision_overview.svg",
    "assets/diagrams/svg/07_experiment_system_flow.svg",
    "assets/diagrams/svg/08_rehab_office_triangle.svg",
    ".github/workflows/docs.yml",
    "scripts/sync_site_docs.py",
]


# Ensure UTF-8 output for Chinese filenames
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")


def main() -> int:
    print("# Site Validation")
    print("")
    missing: list[str] = []

    for rel in REQUIRED_FILES:
        path = ROOT / rel
        if path.exists():
            print(f"[OK] {rel}")
        else:
            print(f"[MISSING] {rel}")
            missing.append(rel)

    print("")
    if missing:
        print(f"[ERROR] Missing {len(missing)} required files.")
        return 1

    print("[OK] All required files exist.")
    print("")
    print("Next steps:")
    print("  mkdocs build --strict")
    print("  mkdocs serve")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
