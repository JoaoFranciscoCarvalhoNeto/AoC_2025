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

        full_turns = ammount // num_pos
        num_zeros += full_turns

        partial_turns = ammount % num_pos

        if current_pos == 0:
            num_zeros += 1

        if direction == "R":
            if (current_pos + partial_turns) > num_pos and current_pos != 0:
                num_zeros += 1
            current_pos += ammount
        if direction == "L":
            if (current_pos - partial_turns) < 0 and current_pos != 0:
                num_zeros += 1
            current_pos -= ammount

        current_pos %= num_pos

        print(
            f"Rotation {line}. Current position: {current_pos}. Times at 0: {num_zeros}"
        )

    print(f"Number of times at 0: {num_zeros}")


if __name__ == "__main__":
    main()
