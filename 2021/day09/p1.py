#!/usr/bin/env python3

import collections
import fileinput
import pprint
import statistics
import sys
import typing


def local_min(x: int, y:int, data: typing.Dict[typing.Tuple[int, int], int]) -> bool:
    points = [
        (x + 1, y),
        (x - 1, y),
        (x, y + 1),
        (x, y - 1),
    ]
    current = data[(x, y)]
    # if x == 1 and y == 0:
    #     print(f"{x}, {y} -> {data[(x,y)]} -> will return {all([current < data[p] for p in points])}")
    #     print(f"surrounds: ")
    #     for p in points:
    #         print(f"{p[0]}, {p[1]} -> {data[p]}")
    return all([current < data[p] for p in points])


def main() -> None:
    maxy = 0
    maxx = None
    data: typing.Dict[typing.Tuple[int, int], int] = collections.defaultdict(lambda: 10)
    for line in fileinput.input():
        if maxx is None:
            maxx = len(line.strip())
        for idx, c in enumerate(line.strip()):
            data[(idx, maxy)] = int(c)
        maxy += 1
    print(f"max-x {maxx} max-y {maxy}")
    risk_level = 0
    tally = 0
    for y in range(maxy+1):
        for x in range(maxx + 1):
            if local_min(x, y, data):
                # print(f"found min point at ({x}, {y}) with value {data[(x,y)]}")
                tally += 1
                risk_level += data[(x, y)] + 1
    print(f"min points {tally} sum of risk_level {risk_level}")


if __name__ == "__main__":
    main()
