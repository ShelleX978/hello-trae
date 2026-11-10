import csv
import sys
from pathlib import Path


def load_rows(path: Path):
    with path.open(encoding="utf-8") as f:
        return list(csv.DictReader(f))


def main():
    path = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("data.csv")
    if not path.exists():
        print(f"找不到文件: {path}")
        return 1

    rows = load_rows(path)
    print(f"文件: {path.name}")
    print(f"数据行数: {len(rows)}")
    for i, row in enumerate(rows[:3], start=1):
        print(f"  {i}. {row}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
