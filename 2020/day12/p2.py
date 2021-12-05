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


def waypoint_delta(waypoint: typing.List[int], v: Vector) -> typing.List[int]:
    result = copy.copy(waypoint)
    if v.direction == "N":
        result[0] += v.distance
    elif v.direction == "S":
        result[0] -= v.distance
    elif v.direction == "E":
        result[1] += v.distance
    elif v.direction == "W":
        result[1] -= v.distance
    # print(f"DEBUG: start: {waypoint} + vector {v} becomes {result}")
    return result


# n5 e2 -> w5 n2 -> n2 w5 -> n2 e-5
# n2 e-5 -> w2 n-5 -> n-5 e-2
# n-5 e-2 -> n-2 w-5 -> n-2 e5
def waypoint_rotate_left(waypoint: typing.List[int], count: int) -> typing.List[int]:
    result = copy.copy(waypoint)
    for c in range(count):
        result = [result[1], result[0]*-1]
    # print(f"DEBUG: start {waypoint} rotations {count} result {result}")
    return result


# n5 e2 -> e5 s2 -> n-2 e5
def waypoint_rotate_right(waypoint: typing.List[int], count: int) -> typing.List[int]:
    result = copy.copy(waypoint)
    for c in range(count):
        result = [result[1]*-1, result[0]]
    # print(f"DEBUG: start {waypoint} rotations {count} result {result}")
    return result


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


def traverse(data: typing.List[Vector], waypoint: typing.List[int]) -> int:
    location: typing.List[int] = [0, 0]
    for v in data:
        if v.direction in ORDERED_CARDINAL_DIRECTIONS:
            waypoint = waypoint_delta(waypoint, v)
        elif v.direction == "L":
            waypoint = waypoint_rotate_left(waypoint, int(v.distance / 90))
        elif v.direction == "R":
            waypoint = waypoint_rotate_right(waypoint, int(v.distance / 90))
        elif v.direction == "F":
            for count in range(v.distance):
                location[0] += waypoint[0]
                location[1] += waypoint[1]
        # print(f"after {v} waypoint is {waypoint} current_location is {location} totaling {sum([abs(i) for i in location])}")
    return sum([abs(i) for i in location])


def main() -> None:
    data = gather()
    waypoint = [1, 10]
    mdist = traverse(data, waypoint)
    print(f"Result: {mdist}")


if __name__ == "__main__":
    main()
