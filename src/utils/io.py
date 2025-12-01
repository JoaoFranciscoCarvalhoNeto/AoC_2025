from pathlib import Path
from typing import List


BASE = Path(__file__).resolve().parent


def read_input() -> str:
    fname = "input.txt"
    path = BASE / fname
    if not path.exists():
        return ""
    return path.read_text(encoding="utf-8")


def read_lines() -> List[str]:
    raw = read_input()
    if raw == "":
        return []
    return [line.rstrip("\n") for line in raw.splitlines()]
