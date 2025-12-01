from pathlib import Path
import argparse
import time
from typing import List

from src.utils.io import read_lines

#!/usr/bin/env python3


def main():
    data = read_lines("input.txt")
    if not data:
        print(f"No input found.")
        return

    for line in data:
        print(line)


if __name__ == "__main__":
    main()
