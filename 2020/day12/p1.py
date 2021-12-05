#!/usr/bin/env python3

"""

"""

import collections
import copy
import fileinput
import typing
import sys


ORDERED_CARDINAL_DIRECTIONS = ("N", "E", "S", "W")


class Vector(typing.NamedTuple):
    direction: str
    distance: int


def split_vect(line: str) -> Vector:
    dire = line[0]
    dist = int(line[1:])
    return Vector(dire, dist)


def gather() -> typing.List[Vector]:
    result = [split_vect(line.strip()) for line in fileinput.input()]
    return result


def calc_mdist_sum(mdist: typing.Dict[str, int]) -> int:
    nstally = 0
    ewtally = 0
    for key in mdist:
        if key == "N":
            nstally += mdist[key]
        elif key == "S":
            nstally -= mdist[key]
        elif key == "E":
            ewtally += mdist[key]
        elif key == "W":
            ewtally -= mdist[key]
    # print(f"DEBUG: {nstally} {ewtally}")
    return abs(nstally) + abs(ewtally)


def traverse(data: typing.List[Vector], current_direction: str) -> typing.Dict[str, int]:
    mdist: typing.Dict[str, int] = collections.defaultdict(int)
    for v in data:
        if v.direction in ORDERED_CARDINAL_DIRECTIONS:
            mdist[v.direction] += v.distance
        elif v.direction == "F":
            mdist[current_direction] += v.distance
        elif v.direction in ("L", "R"):
            turn90s = int(v.distance / 90)
            idx = ORDERED_CARDINAL_DIRECTIONS.index(current_direction)
            if v.direction == "L":
                new_idx = idx - turn90s
            else:
                new_idx = (idx + turn90s) % len(ORDERED_CARDINAL_DIRECTIONS)
            current_direction = ORDERED_CARDINAL_DIRECTIONS[new_idx]
        # print(f"after {v}, current_direction is {current_direction} mdist is {mdist} totaling {calc_mdist_sum(mdist)}")
    return mdist


def main() -> None:
    data = gather()
    mdist = traverse(data, 'E')
    print(f"Result: {calc_mdist_sum(mdist)}")


if __name__ == "__main__":
    main()
