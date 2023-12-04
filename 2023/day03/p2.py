#!/usr/bin/env python3

import argparse
import typing


MAX_X = 0
MAX_Y = 0
SYMBOLS: typing.List[str] = ["#", "$", "%", "&", "*", "+", "-", "/", "=", "@"]


def parseargs() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("input", help="input file")
    return parser.parse_args()


def get_input(in_file: str) -> typing.List[str]:
    with open(in_file) as f:
        return [line.strip() for line in f.readlines()]


class Point(typing.NamedTuple):
    x: int
    y: int


def move_up(p: typing.Optional[Point]) -> typing.Optional[Point]:
    if p is None:
        return None
    elif p.y == 0:
        return None
    return Point(p.x, p.y-1)


def move_down(p: Point) -> typing.Optional[Point]:
    if p is None:
        return None
    elif p.y == MAX_Y:
        return None
    return Point(p.x, p.y+1)


def move_left(p: Point) -> typing.Optional[Point]:
    if p is None:
        return None
    elif p.x == 0:
        return None
    return Point(p.x-1, p.y)


def move_right(p: Point) -> typing.Optional[Point]:
    if p is None:
        return None
    elif p.x == MAX_X:
        return None
    return Point(p.x+1, p.y)


def point_value(p: Point, data: typing.List[str]) -> str:
    if p is None:
        return "."
    elif p.x > MAX_X or p.y > MAX_Y:
        return "."
    elif p.x < 0 or p.y < 0:
        return "."
    return data[p.y][p.x]


def get_number_from_point(p: Point, data: typing.List[str]) -> int:
    if p is None:
        return 0
    row = data[p.y]
    x = p.x
    x_start = None
    x_end = None
    while x_start is None:
        if x == 0:
            x_start = 0
        elif row[x-1].isdigit():
            x -= 1
        else:
            x_start = x
    x = p.x
    while x_end is None:
        if x == MAX_X:
            x_end = MAX_X + 1
        elif row[x+1].isdigit():
            x += 1
        else:
            x_end = x + 1
    # print(f"point: {p} x_start: {x_start}, x_end: {x_end} value: {int(row[x_start:x_end])}")
    return int(row[x_start:x_end])


def get_ratio(p: Point, data: typing.List[str]) -> int:
    uppers = (move_up(p), move_up(move_left(p)), move_up(move_right(p)))
    lowers = (move_down(p), move_down(move_left(p)), move_down(move_right(p)))
    upper = -1
    lower = -1
    left = -1
    right = -1
    if all(point_value(tmp_p, data).isdigit() for tmp_p in uppers):
        upper = get_number_from_point(move_up(p), data)
    elif point_value(move_up(move_left(p)), data).isdigit() and point_value(move_up(move_right(p)), data).isdigit():
        # quick exit on nightmare case
        x = get_number_from_point(move_up(move_left(p)), data)
        y = get_number_from_point(move_up(move_right(p)), data)
        print(f"Gear Ratio nightmare case up: {x} * {y} = {x*y}")
        return x*y
    elif point_value(move_up(move_left(p)), data).isdigit():
        upper = get_number_from_point(move_up(move_left(p)), data)
    elif point_value(move_up(move_right(p)), data).isdigit():
        upper = get_number_from_point(move_up(move_right(p)), data)
    elif point_value(move_up(p), data).isdigit():
        upper = get_number_from_point(move_up(p), data)

    if all(point_value(tmp_p, data).isdigit() for tmp_p in lowers):
        lower = get_number_from_point(move_down(p), data)
    elif point_value(move_down(move_left(p)), data).isdigit() and point_value(move_down(move_right(p)), data).isdigit():
        # quick exit on nightmare case
        x = get_number_from_point(move_down(move_left(p)), data)
        y = get_number_from_point(move_down(move_right(p)), data)
        print(f"Gear Ratio nightmare case up: {x} * {y} = {x*y}")
        return x*y
    elif point_value(move_down(move_left(p)), data).isdigit():
        lower = get_number_from_point(move_down(move_left(p)), data)
    elif point_value(move_down(move_right(p)), data).isdigit():
        lower = get_number_from_point(move_down(move_right(p)), data)
    elif point_value(move_down(p), data).isdigit():
        lower = get_number_from_point(move_down(p), data)

    if point_value(move_left(p), data).isdigit():
        left = get_number_from_point(move_left(p), data)
    if point_value(move_right(p), data).isdigit():
        right = get_number_from_point(move_right(p), data)

    tlist = [upper, lower, left, right]
    unset_nums = sum([1 for t in tlist if t == -1])
    if unset_nums == 3:
        return 0
    return abs(upper * lower * left * right)


def parse_row(y: int, data: typing.List[str]) -> int:
    tally = 0
    for x, char in enumerate(data[y]):
        if char == "*":
            p = Point(x, y)
            gear_ratio = get_ratio(p, data)
            tally += gear_ratio
    # print(f"row {y} tally: {tally}")
    return tally


def main() -> None:
    global MAX_X, MAX_Y
    args = parseargs()
    tally = 0
    data = get_input(args.input)
    MAX_X = len(data[0]) - 1
    MAX_Y = len(data) - 1
    for row_num in range(len(data)):
        x = parse_row(row_num, data)
        # print(f"row {row_num}: {x}")
        tally += x

    print(tally)


if __name__ == "__main__":
    main()
