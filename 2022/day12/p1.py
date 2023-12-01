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
    # if elevation is -1, it's Start, if 26 it's End
    elevation: int


def main() -> None:
    start: Point
    end: Point
    data: typing.Dict[Point, bool] = {}
    y = 0
    for line in fileinput.input():
        sline = line.strip()
        for x, char in enumerate(sline):
            if char == "S":
                v = -1
            elif char == "E":
                v = 26
            else:
                v = string.ascii_lowercase.find(char)
            p = Point(x, y, v)
            data[p] = True


    # print(f"p1 {rolling_ss}, p2 {rolling_ss}")


if __name__ == "__main__":
    main()
