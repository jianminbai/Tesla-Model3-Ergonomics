from __future__ import annotations

import shutil
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
TARGET = ROOT / "site_docs"

GENERATED_FILE_NAMES = {
    ".nojekyll",
    "404.html",
    "index.html",
    "sitemap.xml",
    "sitemap.xml.gz",
}

GENERATED_DIR_PATHS = {
    "assets/javascripts",
    "assets/stylesheets",
    "search",
}

FILES = [
    "README.md",
    "QUICKSTART.md",
    "ROADMAP.md",
    "CONTRIBUTING.md",
]

DIRS = [
    "book",
    "docs",
    "assets",
]

EXPERIMENT_FILES = [
    "driver_log_template.md",
    "symptom_decision_log_template.md",
    "rehab_office_log_template.md",
    "case_001_current_setup.md",
]

EXPERIMENT_DIRS = [
    "templates",
]


def copy_file(relative_path: str) -> None:
    source = ROOT / relative_path
    destination = TARGET / relative_path
    destination.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(source, destination)


def ignore_generated_site_files(directory: str, names: list[str]) -> set[str]:
    ignored: set[str] = set()
    base = Path(directory)

    for name in names:
        path = base / name
        rel = path.relative_to(ROOT).as_posix()

        if name in GENERATED_FILE_NAMES:
            ignored.add(name)
        elif path.is_dir() and rel in GENERATED_DIR_PATHS:
            ignored.add(name)

    return ignored


def copy_tree(relative_path: str) -> None:
    source = ROOT / relative_path
    destination = TARGET / relative_path
    shutil.copytree(source, destination, ignore=ignore_generated_site_files)


def main() -> None:
    if TARGET.exists():
        shutil.rmtree(TARGET)

    TARGET.mkdir(parents=True)

    for relative_path in FILES:
        copy_file(relative_path)

    for relative_path in DIRS:
        copy_tree(relative_path)

    (TARGET / "experiments").mkdir()
    for filename in EXPERIMENT_FILES:
        copy_file(f"experiments/{filename}")
    for dirname in EXPERIMENT_DIRS:
        copy_tree(f"experiments/{dirname}")

    print(f"[OK] Synced MkDocs content to {TARGET}")


if __name__ == "__main__":
    main()
