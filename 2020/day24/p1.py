#!/usr/bin/env python3

"""

"""

import collections
import copy
import fileinput
import pprint
import re
import typing
import sys


def parse(cardinal: str) -> typing.Tuple[float, float]:
    # esenee
    # e se ne e
    directions = []
    previous: typing.Union[None, str] = None
    for char in cardinal:
        if char in ('e', 'w'):
            if previous is None:
                directions.append(char)
            else:
                directions.append(previous + char)
                previous = None
        elif char in ('n', 's'):
            previous = char
    x = 0
    y = 0
    for step in directions:
        if step == "e":
            x += 1
        elif step == "w":
            x -= 1
        elif step == "ne":
            x += .5
            y += .5
        elif step == "nw":
            x -= .5
            y += .5
        elif step == "se":
            x += .5
            y -= .5
        elif step == "sw":
            x -= .5
            y -= .5
    return x, y


def gather() -> typing.DefaultDict[typing.Tuple[float, float], bool]:
    result: typing.DefaultDict[typing.Tuple[float, float], bool] = collections.defaultdict(bool)
    for line in fileinput.input():
        coord = parse(line.strip())
        result[coord] = not result[coord]
    return result


def main() -> None:
    result = gather()
    print(f"tally {sum([1 for coord in result if result[coord]])}")


if __name__ == "__main__":
    main()
