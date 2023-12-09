#!/usr/bin/env python3

import argparse
import collections
import itertools
import pprint
import sys
import typing


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("input", help="input file")
    return parser.parse_args()


def get_input(in_file: str) -> typing.List[str]:
    with open(in_file) as f:
        return f.read().splitlines()


def run_tests() -> None:
    pass


def p1(row_i: typing.Iterable[int], c=0) -> int:
    row = list(row_i)
    if sum(row) == 0:
        return 0
    new_row = []
    for i, num in enumerate(row):
        if i + 1 == len(row):
            break
        new_row.append(row[i + 1] - num)
    r = p1(new_row, c+1)
    return r + row[-1]


def p2(row_i: typing.Iterable[int], c=0) -> int:
    row = list(row_i)
    if sum(row) == 0:
        return 0
    new_row = []
    for i, num in enumerate(row):
        if i + 1 == len(row):
            break
        new_row.append(row[i + 1] - num)
    r = p2(new_row, c+1)
    return row[0] - r


def main() -> None:
    args = parse_args()
    data = get_input(args.input)
    print(f"p1: {sum([p1(map(int, row.split())) for row in data])}")
    print(f"p2: {sum([p2(map(int, row.split())) for row in data])}")
    print(f"p2_alt: {sum([p1(reversed(list(map(int, row.split())))) for row in data])}")


if __name__ == "__main__":
    main()
