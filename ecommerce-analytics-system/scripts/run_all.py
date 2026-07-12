"""Run the complete project pipeline in the correct order."""
from __future__ import annotations
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
STEPS = [
    "generate_data.py",
    "clean_data.py",
    "load_database.py",
    "export_sample_reports.py",
]


def main() -> None:
    for script in STEPS:
        print(f"\n{'=' * 70}\nRunning {script}\n{'=' * 70}")
        subprocess.run([sys.executable, str(ROOT / "scripts" / script)], check=True, cwd=ROOT)
    print("\nPipeline completed successfully.")
    print("Try: python scripts/report_cli.py --report top_customers --limit 10")


if __name__ == "__main__":
    main()
