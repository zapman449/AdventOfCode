#!/usr/bin/env python3

import collections
import fileinput
import pprint
import statistics
import sys
import typing


def delta_median(x: int, median: int) -> int:
    return abs(x-median)


def main() -> None:
    data: typing.List[int] = []
    for line in fileinput.input():
        data = [int(x) for x in line.strip().split(',')]
    median = int(statistics.median(data))
    sumdelta = sum([delta_median(x, median) for x in data])
    print(f"median {median} sum-delta-median {sumdelta}")


if __name__ == "__main__":
    main()
