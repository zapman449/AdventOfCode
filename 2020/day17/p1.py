#!/usr/bin/env python3

"""

"""

import collections
import copy
import fileinput
import pprint
import typing
import sys


class Point(typing.NamedTuple):
    x: int
    y: int
    z: int


def gather() -> typing.Dict[Point, bool]:
    result = collections.defaultdict(bool)
    z = 0
    y = 0
    for line in fileinput.input():
        for x, char in enumerate(line.strip()):
            if char == "#":
                result[Point(x, y, z)] = True
        y += 1
    return result


def print_plane(data: typing.Dict[Point, bool], z: int):
    plane_list = []
    all_x = set()
    all_y = set()
    for p in data.keys():
        all_x.add(p.x)
        all_y.add(p.y)
        if data[p] and p.z == z:
            plane_list.append(p)
    if len(all_x) == 0:
        print("empty plane")
        return
    min_x = min(all_x)
    max_x = max(all_x)
    min_y = min(all_y)
    max_y = max(all_y)
    d_x = max_x - min_x
    d_y = max_y - min_y
    # print(f"min_x {min_x} max_x {max_x} d_x {d_x} min_y {min_y} max_y {max_y} d_y {d_y}")
    row_x = [".", ] * (d_x + 1)
    draw_plane = [copy.copy(row_x) for y in range(d_y + 1)]
    # print(f"start draw_plane: {draw_plane}")
    for p in plane_list:
        draw_plane[p.y + min_y][p.x + min_x] = "#"
        # print(f"point {p} x {p.x + min_x} y {p.y + min_y} draw_plane: {draw_plane}")
    for row in draw_plane:
        print("".join(row))


def count_active_neighbors(p: Point, data: typing.Dict[Point, bool]) -> int:
    count = 0
    for x in (p.x - 1, p.x, p.x + 1):
        for y in (p.y - 1, p.y, p.y + 1):
            for z in (p.z - 1, p.z, p.z + 1):
                if x == p.x and y == p.y and z == p.z:
                    continue
                elif data[p]:
                    count += 1
    return count


def ranges(data: typing.Dict[Point, bool]) -> typing.Tuple[int, int, int, int, int, int]:
    xs = set()
    ys = set()
    zs = set()
    for p in data:
        xs.add(p.x)
        ys.add(p.y)
        zs.add(p.z)
    print(f"xs is {xs} ys {ys} zs {zs}")
    return min(xs), max(xs), min(ys), max(ys), min(zs), max(zs)


def looper(data: typing.Dict[Point, bool], iter_count=6) -> typing.Dict[Point, bool]:
    new_data: typing.Dict[Point, bool] = collections.defaultdict(bool)
    for xxyzzy in range(iter_count):
        min_x, max_x, min_y, max_y, min_z, max_z = ranges(data)
        new_data: typing.Dict[Point, bool] = collections.defaultdict(bool)
        for x in range(min_x-1, max_x+2):
            for y in range(min_y-1, max_y+2):
                for z in range(min_z-1, max_z + 2):
                    p = Point(x, y, z)
                    active_neighbors = count_active_neighbors(p, data)
                    print(f"DEBUG: point {p} active_neighbors {active_neighbors}")
                    if active_neighbors > 9:
                        print(f"DEBUG: data is {data}")
                    if data[p] and active_neighbors in (2, 3):
                        new_data[p] = True
                    elif data[p] is False and active_neighbors == 3:
                        new_data[p] = True
        data = new_data
        for z in range(min_z-1, max_z+2):
            print(f"Z is {z}")
            print_plane(data, z)
        print(f"DONE WITH ITERATION {xxyzzy}")
    return new_data


def count_all_active(data: typing.Dict[Point, bool]) -> int:
    count = 0
    for p in data.keys():
        if data[p]:
            count += 1
    return count


def main() -> None:
    data = gather()
    # z = 0
    # print_plane(data, z)
    new_data = looper(data)
    print(f"result: {count_all_active(new_data)}")


if __name__ == "__main__":
    main()
