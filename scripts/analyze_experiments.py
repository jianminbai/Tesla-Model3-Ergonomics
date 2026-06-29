from __future__ import annotations

from pathlib import Path
import sys

import pandas as pd
import matplotlib.pyplot as plt


ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT / "experiments" / "data"
OUTPUT_DIR = ROOT / "experiments" / "output"

DRIVER_LOG = DATA_DIR / "driver_daily_log.csv"
SEAT_EVENTS = DATA_DIR / "seat_adjustment_events.csv"
OFFICE_LOG = DATA_DIR / "office_rehab_daily_log.csv"


SYMPTOM_COLUMNS = [
    "sit_bone_point_pain_60min",
    "side_soft_tissue_squeeze_60min",
    "thigh_root_pressure_60min",
    "hamstring_tightness_60min",
    "numbness_or_tingling_60min",
    "right_leg_pedal_fatigue_60min",
    "after_drive_residual_score",
]


def read_csv_if_exists(path: Path) -> pd.DataFrame:
    if not path.exists():
        print(f"[WARN] Missing file: {path}")
        return pd.DataFrame()
    return pd.read_csv(path)


def coerce_dates(df: pd.DataFrame) -> pd.DataFrame:
    if "date" in df.columns:
        df["date"] = pd.to_datetime(df["date"], errors="coerce")
        df = df.dropna(subset=["date"]).sort_values("date")
    return df


def make_trend_chart(driver: pd.DataFrame, events: pd.DataFrame) -> Path | None:
    if driver.empty:
        return None

    driver = coerce_dates(driver.copy())
    available_cols = [c for c in SYMPTOM_COLUMNS if c in driver.columns]
    if not available_cols:
        print("[WARN] No symptom columns found.")
        return None

    for col in available_cols:
        driver[col] = pd.to_numeric(driver[col], errors="coerce")

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    plt.figure(figsize=(12, 7))
    for col in available_cols:
        if driver[col].notna().any():
            plt.plot(driver["date"], driver[col], marker="o", label=col)

    if not events.empty and "date" in events.columns:
        events = coerce_dates(events.copy())
        for _, row in events.iterrows():
            date = row.get("date")
            label = str(row.get("seat_setup_id", "")) + " " + str(row.get("adjustment_type", ""))
            if pd.notna(date):
                plt.axvline(date, linestyle="--", alpha=0.35)
                plt.text(date, 9.5, label[:18], rotation=90, va="top", fontsize=8)

    plt.title("Tesla Model 3 Ergonomics Symptom Trends")
    plt.xlabel("Date")
    plt.ylabel("Score 0-10")
    plt.ylim(0, 10)
    plt.grid(True, alpha=0.25)
    plt.legend(loc="upper left", bbox_to_anchor=(1, 1))
    plt.tight_layout()

    output = OUTPUT_DIR / "symptom_trends.png"
    plt.savefig(output, dpi=160)
    plt.close()
    return output


def make_summary(driver: pd.DataFrame, office: pd.DataFrame, events: pd.DataFrame, chart_path: Path | None) -> Path:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    lines: list[str] = []
    lines.append("# 实验数据摘要")
    lines.append("")

    if driver.empty:
        lines.append("未找到驾驶记录。请先复制模板到 `experiments/data/` 并填写。")
    else:
        driver = coerce_dates(driver.copy())
        for col in SYMPTOM_COLUMNS:
            if col in driver.columns:
                driver[col] = pd.to_numeric(driver[col], errors="coerce")

        lines.append("## 驾驶记录")
        lines.append("")
        lines.append(f"- 记录条数：{len(driver)}")
        if "date" in driver.columns and len(driver) > 0:
            lines.append(f"- 日期范围：{driver['date'].min().date()} 至 {driver['date'].max().date()}")

        recent = driver.tail(7)
        lines.append("")
        lines.append("## 最近 7 条记录平均分")
        lines.append("")
        lines.append("| 指标 | 平均分 |")
        lines.append("|---|---:|")
        for col in SYMPTOM_COLUMNS:
            if col in recent.columns:
                avg = pd.to_numeric(recent[col], errors="coerce").mean()
                if pd.notna(avg):
                    lines.append(f"| {col} | {avg:.2f} |")

    if not events.empty:
        lines.append("")
        lines.append("## 座椅调整事件")
        lines.append("")
        cols = [c for c in ["date", "seat_setup_id", "adjustment_type", "adjustment_value", "hypothesis"] if c in events.columns]
        if cols:
            lines.append("| " + " | ".join(cols) + " |")
            lines.append("|" + "|".join(["---"] * len(cols)) + "|")
            for _, row in events.iterrows():
                lines.append("| " + " | ".join(str(row.get(c, "")) for c in cols) + " |")

    if not office.empty:
        lines.append("")
        lines.append("## 办公与康复记录")
        lines.append("")
        lines.append(f"- 记录条数：{len(office)}")
        for col in ["max_continuous_sitting_minutes", "hamstring_tightness_office", "side_soft_tissue_squeeze_office"]:
            if col in office.columns:
                avg = pd.to_numeric(office[col], errors="coerce").tail(7).mean()
                if pd.notna(avg):
                    lines.append(f"- 最近 7 条 `{col}` 平均值：{avg:.2f}")

    if chart_path is not None:
        rel = chart_path.relative_to(ROOT).as_posix()
        lines.append("")
        lines.append("## 趋势图")
        lines.append("")
        lines.append(f"![symptom trends](../../{rel})")

    output = OUTPUT_DIR / "summary.md"
    output.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return output


def main() -> int:
    driver = read_csv_if_exists(DRIVER_LOG)
    events = read_csv_if_exists(SEAT_EVENTS)
    office = read_csv_if_exists(OFFICE_LOG)

    chart_path = make_trend_chart(driver, events)
    summary_path = make_summary(driver, office, events, chart_path)

    print(f"[OK] Summary written: {summary_path}")
    if chart_path:
        print(f"[OK] Chart written: {chart_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
