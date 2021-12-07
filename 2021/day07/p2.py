#!/usr/bin/env python3

import collections
import fileinput
import pprint
import statistics
import sys
import typing


def delta_average(x: int, median: int) -> int:
    last_term = abs(x-median)
    return int((last_term/2)*(1+last_term))


def main() -> None:
    data: typing.List[int] = []
    for line in fileinput.input():
        data = [int(x) for x in line.strip().split(',')]
    average = sum(data) / len(data)
    lower = int(average)
    upper = lower + 1
    sumdeltalower = sum([delta_average(x, lower) for x in data])
    print(f"average {average} using {lower} sum-delta-average {sumdeltalower}")
    sumdeltaupper = sum([delta_average(x, upper) for x in data])
    print(f"average {average} using {upper} sum-delta-average {sumdeltaupper}")
    print(f"real result: {min(sumdeltaupper, sumdeltalower)}")


if __name__ == "__main__":
    main()
