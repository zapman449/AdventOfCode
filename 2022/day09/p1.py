#!/usr/bin/env python3

import collections
import copy
import fileinput
import pprint
import string
import sys
import typing


class Point(typing.NamedTuple):
    x: int
    y: int


def move_up(p: Point) -> Point:
    return Point(p.x, p.y+1)


def move_down(p: Point) -> Point:
    return Point(p.x, p.y-1)


def move_left(p: Point) -> Point:
    return Point(p.x-1, p.y)


def move_right(p: Point) -> Point:
    return Point(p.x+1, p.y)


dmap = {
    "U": move_up,
    "D": move_down,
    "L": move_left,
    "R": move_right,
}


def new_tail(h: Point, t: Point) -> Point:
    delta_x = abs(h.x - t.x)
    delta_y = abs(h.y - t.y)
    if delta_x >= 2 and delta_y >= 2:
        print(f"failure. delta_x {delta_x} and delta_y {delta_y} >=2. h is {h} t is {t}")
        sys.exit()
    elif delta_x <= 1 and delta_y <= 1:
        return Point(t.x, t.y)
    elif delta_x == 0:
        # then delta_y is 2
        if h.y > t.y:
            return move_up(t)
        return move_down(t)
    elif delta_y == 0:
        # then delta_x is 2
        if h.x > t.x:
            return move_right(t)
        return move_left(t)
    elif delta_x == 2 or delta_y == 2:
        # then delta_y is 1
        if h.x > t.x and h.y > t.y:
            return move_up(move_right(t))
        elif h.x > t.x and h.y < t.y:
            return move_down(move_right(t))
        elif h.x < t.x and h.y < t.y:
            return move_down(move_left(t))
        elif h.x < t.x and h.y > t.y:
            return move_up(move_left(t))
    else:
        print(f"WTF?. delta_x {delta_x} and delta_y {delta_y} >=2. h is {h} t is {t}")
        sys.exit()


def main() -> None:
    visited: typing.Set[Point] = set()
    current_h = Point(0, 0)
    current_t = Point(0, 0)
    for line in fileinput.input():
        d, count_str = line.strip().split(" ")
        count = int(count_str)
        for z in range(count):
            current_h = dmap[d](current_h)
            current_t = new_tail(current_h, current_t)
            visited.add(current_t)

    print(f"p1 {len(visited)}, p2 {len(visited)}")


if __name__ == "__main__":
    main()
