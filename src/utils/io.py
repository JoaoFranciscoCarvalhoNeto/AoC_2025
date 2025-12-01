from pathlib import Path
from typing import List
import inspect


def read_lines(filename: str) -> List[str]:
    caller_frame = inspect.currentframe().f_back
    caller_file = caller_frame.f_globals["__file__"]
    caller_dir = Path(caller_file).resolve().parent

    path = caller_dir / filename
    if not path.exists():
        return []

    return [line.rstrip("\n") for line in path.read_text(encoding="utf-8").splitlines()]
