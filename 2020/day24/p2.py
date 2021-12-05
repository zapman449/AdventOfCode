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


def neighbor_coords(x: float, y: float) -> typing.List[typing.Tuple[float, float]]:
    result = []
    for dx, dy in [(-1, 0), (1, 0), (-.5, .5), (.5, .5), (-.5, -.5), (.5, -.5)]:
        result.append((x+dx, y+dy))
    return result


def day_flip(tiles: typing.DefaultDict[typing.Tuple[float, float], bool]) -> typing.DefaultDict[typing.Tuple[float, float], bool]:
    result: typing.DefaultDict[typing.Tuple[float, float], bool] = collections.defaultdict(bool)
    ctiles = list(tiles.keys())
    # print(f"ctiles {ctiles}")
    # for x, y in ctiles:
    #     if tiles[(x,y)]:
    #         print(f"tile {x}, {y} is {tiles[(x,y)]}")
    for x, y in ctiles:
        checked = set()
        for (nx, ny) in neighbor_coords(x, y):
            if (nx, ny) in checked:
                continue
            checked.add((nx, ny))
            bcount = 0
            for nnx, nny in neighbor_coords(nx, ny):
                if tiles[(nnx, nny)]:
                    bcount += 1
            # print(f"tile {nx}, {ny} is {tiles[(nx, ny)]} and has bcount of {bcount}")
            # if tiles[(nx, ny)] and bcount in (0, 2, 3, 4, 5, 6):
            #     result[(nx, ny)] = False
            if tiles[(nx, ny)] and bcount == 1:
                result[(nx, ny)] = True
            elif bcount == 2:
                result[(nx, ny)] = True
    return result


def main() -> None:
    result = gather()
    for d in range(1, 101, 1):
        new_result = day_flip(result)
        result = new_result
        print(f"day {d} tally {sum([1 for coord in result if result[coord]])}")


if __name__ == "__main__":
    main()
