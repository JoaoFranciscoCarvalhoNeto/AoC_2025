from pathlib import Path
import argparse
import time
from typing import List

from src.utils.io import read_input

#!/usr/bin/env python3


def main():
    data = read_input()
    if data == "":
        print(f"No input found.")
        return

    for line in data:
        print(line)


if __name__ == "__main__":
    main()
