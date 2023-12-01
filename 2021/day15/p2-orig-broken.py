#!/usr/bin/env python3

import collections
import copy
import fileinput
import pprint
import re
import statistics
import sys
import typing


class Point(typing.NamedTuple):
    x: int
    y: int


class RollingSum(typing.NamedTuple):
    point: Point
    tally: int


def is_point_in(data: typing.List[typing.List[int]], point: Point) -> bool:
    len_x = len(data[0])
    len_y = len(data)
    if point.x >= len_x:
        return False
    if point.y >= len_y:
        return False
    if point.x < 0:
        return False
    if point.y < 0:
        return False
    return True


def is_terminus(data: typing.List[typing.List[int]], point: Point) -> bool:
    max_x = len(data[0]) - 1
    max_y = len(data) - 1
    if point.x == max_x and point.y == max_y:
        return True
    return False


def down_right(data: typing.List[typing.List[int]], point: Point) -> typing.List[Point]:
    result: typing.List[Point] = []
    p1 = Point(point.x + 1, point.y)
    p2 = Point(point.x, point.y + 1)
    if is_point_in(data, p1):
        result.append(p1)
    if is_point_in(data, p2):
        result.append(p2)
    return result


def point_value(data: typing.List[typing.List[int]], point: Point) -> int:
    return data[point.y][point.x]


def grid_plus_x(data: typing.List[typing.List[int]], adder) -> typing.List[typing.List[int]]:
    new_data: typing.List[typing.List[int]] = []
    for idx_y, row in enumerate(data):
        new_data.append([])
        for idx_x, i in enumerate(row):
            if i + adder >= 10:
                new_data[idx_y].append(((i+adder)%10)+1)
            else:
                new_data[idx_y].append(i+adder)
            # if adder == 4 and row[-1] == 5 and row[-2] == 7:
            #     print(f"HELP: i {i}, adder {adder}, sum {i+adder}")
    return new_data


def grid_add_right(data: typing.List[typing.List[int]], to_add_right: typing.List[typing.List[int]], adder: int) -> typing.List[typing.List[int]]:
    data_plus_one = grid_plus_x(to_add_right, adder)
    new_data: typing.List[typing.List[int]] = []
    for idx_y, row in enumerate(data):
        new_data.append(row + data_plus_one[idx_y])
    # print(data[0][-10:])
    # print(data_plus_one[0][-10:])
    # print(new_data[0][-10:])
    return new_data


def grid_add_down(data: typing.List[typing.List[int]], to_add_below: typing.List[typing.List[int]], adder: int) -> typing.List[typing.List[int]]:
    new_data = grid_plus_x(to_add_below, adder)
    return data + new_data


def grid_print(data: typing.List[typing.List[int]]) -> None:
    for row in data:
        print("".join(map(str, row)))


def main() -> None:
    data: typing.List[typing.List[int]] = []
    for line in fileinput.input():
        row: typing.List[int] = []
        for c in line.strip():
            row.append(int(c))
        data.append(row)

    og_data = copy.copy(data)
    # grid_print(data)
    data = grid_add_right(data, og_data, 1)
    # grid_print(data)
    data = grid_add_right(data, og_data, 2)
    # grid_print(data)
    data = grid_add_right(data, og_data, 3)
    # grid_print(data)
    data = grid_add_right(data, og_data, 4)
    # grid_print(data)

    og_all_right_data = copy.copy(data)
    data = grid_add_down(data, og_all_right_data, 1)
    data = grid_add_down(data, og_all_right_data, 2)
    data = grid_add_down(data, og_all_right_data, 3)
    data = grid_add_down(data, og_all_right_data, 4)

    print(f"dimensions of data: {len(data[0])}, {len(data)}")
    print(f"dimensions of og_data: {len(og_data[0])}, {len(og_data)}")

    # grid_print(data)

    rolling_sums: typing.List[RollingSum] = [RollingSum(Point(0, 0), 0)]
    while True:
        diag: typing.Dict[Point, int] = collections.defaultdict(int)
        for rs in rolling_sums:
            next_points = down_right(data, rs.point)
            for np in next_points:
                pv = point_value(data, np)
                if diag[np] == 0:
                    diag[np] = pv + rs.tally
                elif diag[np] > pv + rs.tally:
                    diag[np] = pv + rs.tally
        # print(repr(diag))
        rolling_sums = [RollingSum(k, v) for k, v in diag.items()]
        if len(rolling_sums) == 1:
            print(repr(rolling_sums))
            break


if __name__ == "__main__":
    main()
