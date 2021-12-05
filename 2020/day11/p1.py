#!/usr/bin/env python3

"""

"""

import copy
import fileinput
import typing
import sys

EMPTY = "L"
OCCUPIED = "#"
FLOOR = "."


class Point(typing.NamedTuple):
    x: int
    y: int


def gather() -> typing.List[typing.List[str]]:
    result = [list(line.strip()) for line in fileinput.input()]
    return result


def display(data: typing.List[typing.List[str]]) -> None:
    for row in data:
        print("".join(row))


def char_at_point(data: typing.List[typing.List[str]], x: int, y: int) -> typing.Optional[str]:
    if x < 0 or y < 0:
        return None
    elif x >= len(data[0]) or y >= len(data):
        return None
    # print(f"x {x} y {y} len(data[0] {len(data[0])} len(data) {len(data)}")
    return data[y][x]


def count_unoccupied_around(data: typing.List[typing.List[str]], x: int, y: int) -> int:
    tally = 0
    for xs in (x-1, x, x+1):
        for ys in (y - 1, y, y + 1):
            if xs == x and ys == y:
                continue
            elif is_empty_q(data, xs, ys) or is_floor_q(data, xs, ys):
                tally += 1
    return tally


def count_occupied_around(data: typing.List[typing.List[str]], x: int, y: int) -> int:
    tally = 0
    for xs in (x-1, x, x+1):
        for ys in (y - 1, y, y + 1):
            if xs == x and ys == y:
                continue
            elif is_occupied_q(data, xs, ys):
                tally += 1
    return tally


def is_empty_q(data: typing.List[typing.List[str]], x: int, y: int) -> int:
    value = char_at_point(data, x, y)
    if value == EMPTY:
        return True
    return False


def is_occupied_q(data: typing.List[typing.List[str]], x: int, y: int) -> int:
    value = char_at_point(data, x, y)
    if value == OCCUPIED:
        return True
    return False


def is_floor_q(data: typing.List[typing.List[str]], x: int, y: int) -> int:
    value = char_at_point(data, x, y)
    if value == FLOOR:
        return True
    return False


def iterate(data: typing.List[typing.List[str]]) -> typing.List[typing.List[str]]:
    new_data = copy.deepcopy(data)
    for y, row in enumerate(data):
        for x, _ in enumerate(data[y]):
            if is_floor_q(data, x, y):
                # print(f"setting {data[y][x]} to floor")
                new_data[y][x] = FLOOR
            elif is_occupied_q(data, x, y) and count_occupied_around(data, x, y) >= 4:
                # print(f"setting {data[y][x]} to empty because {count_occupied_around(data, x, y)} >= 4")
                new_data[y][x] = EMPTY
            elif is_empty_q(data, x, y) and count_occupied_around(data, x, y) == 0:
                # print(f"setting {data[y][x]} to occupied because {count_occupied_around(data, x, y)} == 0")
                new_data[y][x] = OCCUPIED
            else:
                # print(f"not changing {data[y][x]} is_empty_q gives {is_empty_q(data, x, y)}"
                #       f" count_occupied_around(data, x, y) gives {count_occupied_around(data, x, y)}")
                new_data[y][x] = data[y][x]
    return new_data


def main() -> None:
    data = gather()
    # display(data)

    iterations = 0
    while True:
        iterations += 1
        new_data = iterate(data)
        # display(new_data)
        if new_data == data:
            tally = 0
            for y, row in enumerate(new_data):
                for x, _ in enumerate(new_data[y]):
                    if is_occupied_q(new_data, x, y):
                        tally += 1
            print(f"result: {tally}")
            break
        data = new_data


if __name__ == "__main__":
    main()
