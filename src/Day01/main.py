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

    num_pos = 100
    current_pos = 50
    num_zeros = 0

    for line in data:
        direction = line[0]
        ammount = int(line[1:])

        if direction == "R":
            current_pos += ammount
        if direction == "L":
            current_pos -= ammount

        current_pos %= num_pos

        if current_pos == 0:
            num_zeros += 1

        print(
            f"Direction: {direction}. Ammount: {ammount}. Current position: {current_pos}"
        )

    print(f"Number of times at 0: {num_zeros}")


if __name__ == "__main__":
    main()
