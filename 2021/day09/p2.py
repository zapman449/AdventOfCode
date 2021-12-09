#!/usr/bin/env python3

import collections
import fileinput
import functools
import operator
import pprint
import statistics
import sys
import typing


def prod(iterable):
    return functools.reduce(operator.mul, iterable, 1)


def local_min(x: int, y:int, data: typing.Dict[typing.Tuple[int, int], int]) -> bool:
    points = [
        (x + 1, y),
        (x - 1, y),
        (x, y + 1),
        (x, y - 1),
    ]
    current = data[(x, y)]
    return all([current < data[p] for p in points])


def basin_recurse(current: typing.Tuple[int, int], data: typing.Dict[typing.Tuple[int, int], int], seen: typing.Set[typing.Tuple[int, int]]) -> None:
    current_value = data[current]
    if current in seen:
        return
    seen.add(current)
    x, y = current
    points = [
        (x + 1, y),
        (x - 1, y),
        (x, y + 1),
        (x, y - 1),
    ]
    for p in points:
        if p not in seen:
            p_value = data[p]
            if current_value <= p_value < 9:
                basin_recurse(p, data, seen)


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
    min_points: typing.Dict[typing.Tuple[int, int], int] = {}
    for y in range(maxy+1):
        for x in range(maxx + 1):
            if local_min(x, y, data):
                # print(f"found min point at ({x}, {y}) with value {data[(x,y)]}")
                min_points[(x, y)] = 0
    for point in min_points:
        seen: typing.Set[typing.Tuple[int, int]] = set()
        basin_recurse(point, data, seen)
        min_points[point] = len(seen)
        # print(f"min point {point} has size {len(seen)}")

    sizes = sorted(min_points.values())
    print(f"top three sizes: {repr(sizes[-3:])} product {prod(sizes[-3:])}")


if __name__ == "__main__":
    main()
