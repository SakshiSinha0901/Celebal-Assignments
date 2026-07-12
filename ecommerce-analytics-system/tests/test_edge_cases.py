"""Small executable checks for important edge cases."""
from __future__ import annotations
import sqlite3
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CLI = ROOT / "scripts" / "report_cli.py"


def run_cli(*args: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run([sys.executable, str(CLI), *args], text=True, capture_output=True)


def main() -> None:
    invalid_limit = run_cli("--report", "top_customers", "--limit", "0")
    assert invalid_limit.returncode == 2
    assert "between 1 and 100" in invalid_limit.stderr

    missing_db = run_cli("--report", "revenue", "--db", str(ROOT / "database" / "missing.db"))
    assert missing_db.returncode == 1
    assert "database not found" in missing_db.stderr

    with tempfile.TemporaryDirectory() as tmp:
        empty_db = Path(tmp) / "empty.db"
        with sqlite3.connect(empty_db) as conn:
            conn.executescript((ROOT / "sql" / "schema.sql").read_text(encoding="utf-8"))
        empty_result = run_cli("--report", "revenue", "--db", str(empty_db))
        assert empty_result.returncode == 0
        assert "No data found" in empty_result.stdout

    print("All edge-case checks passed.")


if __name__ == "__main__":
    main()
