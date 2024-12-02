#!/usr/bin/env python3

import fileinput
import typing


def test_increase(row: typing.List[int]) -> bool:
    for i in range(1, len(row)):
        delta = row[i - 1] - row[i]
        if 1 <= delta <= 3:
            continue
        else:
            return False
    return True


def test_decrease(row: typing.List[int]) -> bool:
    for i in range(1, len(row)):
        delta = row[i] - row[i - 1]
        if 1 <= delta <= 3:
            continue
        else:
            return False
    return True


def test_skip_one(row: typing.List[int]) -> bool:
    for i in range(len(row)):
        new_row = row[:i] + row[i+1:]
        if test_increase(new_row) or test_decrease(new_row):
            return True
    return False


def main() -> None:
    p1_tally = 0
    p2_tally = 0
    for line in fileinput.input():
        row = list(map(int, line.split()))
        if test_increase(row) or test_decrease(row):
            p1_tally += 1
            p2_tally += 1
        elif test_skip_one(row):
            p2_tally += 1
    print("part1: ", p1_tally)
    print("part2: ", p2_tally)


if __name__ == '__main__':
    main()