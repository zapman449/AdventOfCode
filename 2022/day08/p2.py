#!/usr/bin/env python3

import collections
import copy
import fileinput
import pprint
import string
import sys
import typing


def north(data: typing.List[typing.List[int]], x: int, y: int) -> typing.List[int]:
    result = [data[yi][x] for yi in range(0, y)]
    if len(result) == 0:
        result = [-1]
    result.reverse()
    return result


def south(data: typing.List[typing.List[int]], x: int, y: int) -> typing.List[int]:
    result = [data[yi][x] for yi in range(y+1, len(data))]
    if len(result) == 0:
        result = [-1]
    return result


def east(data: typing.List[typing.List[int]], x: int, y: int) -> typing.List[int]:
    try:
        result = data[y][x+1:]
    except IndexError:
        result = [-1]
    if len(result) == 0:
        result = [-1]
    return result


def west(data: typing.List[typing.List[int]], x: int, y: int) -> typing.List[int]:
    try:
        result = data[y][:x]
    except IndexError:
        result = [-1]
    if len(result) == 0:
        result = [-1]
    result.reverse()
    return result


def viewing_distance(h: int, vector: typing.List[int]) -> int:
    if len(vector) == 0:
        return 0
    view = 0
    for v in vector:
        if v == -1:
            return 0
        elif v < h:
            view += 1
        elif v >= h:
            view += 1
            break
    return view


def scenic_score(h: int, n: typing.List[int], s: typing.List[int], e: typing.List[int], w: typing.List[int]) -> int:
    vdn = viewing_distance(h, n)
    vds = viewing_distance(h, s)
    vde = viewing_distance(h, e)
    vdw = viewing_distance(h, w)
    # print(vdn, vds, vde, vdw)
    return vdn * vds * vde * vdw


def main() -> None:
    data: typing.List[typing.List[int]] = []
    for line in fileinput.input():
        data.append(list(map(int, line.strip())))
    visible = 0
    invisible = 0
    # print()
    # print(scenic_score(5, north(data, 2, 1), south(data, 2, 1), east(data, 2, 1), west(data, 2, 1)))
    # print(scenic_score(5, north(data, 2, 3), south(data, 2, 3), east(data, 2, 3), west(data, 2, 3)))
    max_scenic_score = 0
    # ss_data = copy.deepcopy(data)
    for x in range(len(data[0])):
        for y in range(len(data)):
            height = data[y][x]
            n = north(data, x, y)
            s = south(data, x, y)
            e = east(data, x, y)
            w = west(data, x, y)
            if max(n) >= height and max(s) >= height and max(e) >= height and max(w) >= height:
                invisible += 1
            else:
                visible += 1
            ss = scenic_score(height, n, s, e, w)
            # ss_data[y][x] = ss
            if ss > max_scenic_score:
                max_scenic_score = ss
    # pprint.pprint(ss_data)

    print(f"p1 {visible}, max scenic score {max_scenic_score}")


if __name__ == "__main__":
    main()
