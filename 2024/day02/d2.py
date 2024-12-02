#!/usr/bin/env python3

import fileinput
import typing


def test_row(row: typing.List[int]) -> bool:
    if row[1] > row[0]:
        # increasing
        def delta_calc(i:int, i_minus_one: int) -> int:
            return i - i_minus_one
    else:
        # decreasing
        def delta_calc(i:int, i_minus_one: int) -> int:
            return i_minus_one - i
    for j in range(1, len(row)):
        delta = delta_calc(row[j], row[j - 1])
        if 1 <= delta <= 3:
            continue
        else:
            return False
    return True


def test_skip_one(row: typing.List[int]) -> bool:
    for i in range(len(row)):
        new_row = row[:i] + row[i+1:]
        if test_row(new_row):
            return True
    return False


def main() -> None:
    p1_tally = 0
    p2_tally = 0
    for line in fileinput.input():
        row = list(map(int, line.split()))
        if test_row(row):
            p1_tally += 1
            p2_tally += 1
        elif test_skip_one(row):
            p2_tally += 1
    print("part1: ", p1_tally)
    print("part2: ", p2_tally)


if __name__ == '__main__':
    main()