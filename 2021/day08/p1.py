#!/usr/bin/env python3

import collections
import fileinput
import pprint
import statistics
import sys
import typing


def main() -> None:
    tally = 0
    for line in fileinput.input():
        x = line.strip().split(" | ")
        # print(f"x is {repr(x)}")
        puzzle_in, puzzle_out = x
        # print(f"puzzle_in is {puzzle_in} puzzle_out is {puzzle_out}")
        for word in puzzle_out.split():
            # print(f"word is {word}")
            if len(word) in (2, 3, 4, 7):
                tally += 1
    print(f"tally {tally}")


if __name__ == "__main__":
    main()
