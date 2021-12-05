#!/usr/bin/env python3

"""

"""

import collections
import copy
import fileinput
import typing
import sys


def gather() -> typing.Tuple[int, typing.List[int]]:
    first = True
    start_time = 0
    unprocessed = ""
    for line in fileinput.input():
        if first:
            first = False
            start_time = int(line.strip())
        else:
            unprocessed = line.strip()
    data = [int(val) for val in unprocessed.split(',') if val != "x"]
    data.sort()
    return start_time, data


def traverse(start_time: int, data: typing.List[int]) -> typing.Tuple[int, int]:
    while True:
        for bus in data:
            if start_time % bus == 0:
                return bus, start_time
        start_time += 1


def main() -> None:
    start_time, data = gather()
    bus_id, departure = traverse(start_time, data)
    delta = departure - start_time
    product = delta * bus_id
    print(f"Result: bus_id {bus_id}, departure {departure} departure-start {delta} product {product}")


if __name__ == "__main__":
    main()
