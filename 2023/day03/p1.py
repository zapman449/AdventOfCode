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
    elif p.x <= 0 or p.y <= 0:
        return "."
    return data[p.y][p.x]


def get_input(in_file: str) -> typing.List[str]:
    with open(in_file) as f:
        return [line.strip() for line in f.readlines()]


def get_surrounding_points(p: Point) -> typing.List[Point]:
    return [
        move_up(move_left(p)),
        move_up(p),
        move_up(move_right(p)),
        move_left(p),
        move_right(p),
        move_down(move_left(p)),
        move_down(p),
        move_down(move_right(p)),
    ]


def digit_points_near_symbol(points: typing.List[Point], data: typing.List[str]) -> bool:
    for p in points:
        surrounding_points = get_surrounding_points(p)
        # print(f"surrounding_points: {surrounding_points}")
        for sp in surrounding_points:
            if point_value(sp, data) in SYMBOLS:
                return True
    return False


def parse_row(y: int, data: typing.List[str]) -> int:
    in_number = False
    digit_points: typing.List[Point] = []
    digits: str = ""
    row_tally: int = 0
    for x, char in enumerate(data[y]):
        # cases:
        #   - char is digit and in_number is False -> start of number, in_number becomes True
        #   - char is digit and in_number is True -> continue number, in_number stays true
        #   - char is not digit and in_number is True -> end of number, in_number becomes False, work the number
        #   - char is not digit and in_number is False -> continue
        if char.isdigit():
            in_number = True
            digit_points.append(Point(x, y))
            digits += char
        elif in_number:
            in_number = False
            # print(f"number: {int(digits)}, digit_points: {digit_points}")
            if digit_points_near_symbol(digit_points, data):
                row_tally += int(digits)
            digits = ""
            digit_points = []

        if x == MAX_X and char.isdigit():
            # print(f"number: {int(digits)}, digit_points: {digit_points}")
            if digit_points_near_symbol(digit_points, data):
                row_tally += int(digits)
    return row_tally


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
