"""Export selected reports to CSV and text files for submission evidence."""
from __future__ import annotations
import sqlite3
from pathlib import Path
import pandas as pd
from tabulate import tabulate
from report_cli import REPORTS

ROOT = Path(__file__).resolve().parents[1]
DB_PATH = ROOT / "database" / "ecommerce_analytics.db"
OUT = ROOT / "output" / "sample_reports"


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    with sqlite3.connect(DB_PATH) as conn:
        for name, query in REPORTS.items():
            frame = pd.read_sql_query(query, conn, params={"limit": 20})
            frame.to_csv(OUT / f"{name}.csv", index=False)
            (OUT / f"{name}.txt").write_text(
                f"Report: {name.replace('_', ' ').title()}\n\n" +
                (tabulate(frame, headers="keys", tablefmt="github", showindex=False) if not frame.empty else "No data found.") + "\n",
                encoding="utf-8",
            )
            print(f"Exported {name}.csv and {name}.txt")


if __name__ == "__main__":
    main()
