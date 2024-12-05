#!/usr/bin/env python3

import fileinput
import sys
import typing


class Point(typing.NamedTuple):
    x: int
    y: int


def parse_input() -> typing.Tuple[typing.List[str], typing.Dict[Point, str], int, int]:
    puzzle: typing.List[str] = []
    points: typing.Dict[Point, str] = {}
    y = 0
    for line in fileinput.input():
        puzzle.append(line.strip())
        for x, char in enumerate(line.strip()):
            points[Point(x, y)] = char
        y += 1
    max_x = len(puzzle[0]) - 1
    max_y = len(puzzle) - 1
    return puzzle, points, max_x, max_y


def find_surrounding(p: Point, how_far: int, max_x: int, max_y: int) -> typing.List[typing.List[Point]]:
    result: typing.List[typing.List[Point]] = []
    # eight directions
    if p.x - how_far >= 0: # left
        result.append([Point(x, p.y) for x in range(p.x -1, p.x - how_far - 1, -1)])
    if p.x + how_far <= max_x: # right
        result.append([Point(x, p.y) for x in range(p.x + 1, p.x + how_far + 1, 1)])
    if p.y - how_far >= 0: # up
        result.append([Point(p.x, y) for y in range(p.y -1, p.y - how_far - 1, -1)])
    if p.y + how_far <= max_y: # down
        result.append([Point(p.x, y) for y in range(p.y + 1, p.y + how_far + 1, 1)])

    if p.x - how_far >= 0 and p.y - how_far >= 0: # up left
        result.append([Point(x, y) for x, y in zip(range(p.x - 1, p.x - how_far - 1, -1), range(p.y - 1, p.y - how_far - 1, -1))])
    if p.x + how_far <= max_x and p.y - how_far >= 0: # up right
        result.append([Point(x, y) for x, y in zip(range(p.x + 1, p.x + how_far + 1, 1), range(p.y - 1, p.y - how_far - 1, -1))])
    if p.x - how_far >= 0 and p.y + how_far <= max_y: # down left
        result.append([Point(x, y) for x, y in zip(range(p.x - 1, p.x - how_far - 1, -1), range(p.y + 1, p.y + how_far + 1, 1))])
    if p.x + how_far <= max_x and p.y + how_far <= max_y: # down right
        result.append([Point(x, y) for x, y in zip(range(p.x + 1, p.x + how_far + 1, 1), range(p.y + 1, p.y + how_far + 1, 1))])

    return result


def test_point(p: Point, letter: str, points: typing.Dict[Point, str]) -> bool:
    if p in points and points[p] == letter:
        return True
    return False


def test_ray(ray: typing.List[Point], points: typing.Dict[Point, str]) -> bool:
    if len(ray) != 3:
        sys.exit(f"ray {ray} is not 3 long")
    if points[ray[0]] == 'M':
        if points[ray[1]] == 'A':
            if points[ray[2]] == 'S':
                return True
    return False


def string_ray(ray: typing.List[Point], points: typing.Dict[Point, str]) -> str:
    result = ""
    for p in ray:
        result += points[p]
    return result


def print_ray(ray: typing.List[Point], x_point: Point, points: typing.Dict[Point, str]) -> None:
    print(x_point, string_ray(ray, points))


def find_points(letter: str, puzzle: typing.List[str]) -> typing.List[Point]:
    result_points: typing.List[Point] = []
    for y, row in enumerate(puzzle):
        for x, char in enumerate(row):
            if char == letter:
                result_points.append(Point(x, y))
    return result_points


def gen_squares(puzzle: typing.List[str], size: int) -> typing.Generator[typing.List[str], None, None]:
    for y, row in enumerate(puzzle):
        for x, char in enumerate(row):
            if x + size <= len(row) and y + size <= len(puzzle):
                yield [row[y:y+size] for row in puzzle[x:x+size]]

def test_square(square: typing.List[str]) -> bool:
    if square[1][1] == "A":
        if square[0][0] == "M" and square[0][2] == "M":
            if square[2][0] == "S" and square[2][2] == "S":
                return True
        if square[0][0] == "M" and square[0][2] == "S":
            if square[2][0] == "M" and square[2][2] == "S":
                return True
        if square[0][0] == "S" and square[0][2] == "S":
            if square[2][0] == "M" and square[2][2] == "M":
                return True
        if square[0][0] == "S" and square[0][2] == "M":
            if square[2][0] == "S" and square[2][2] == "M":
                return True
    return False

def main() -> None:
    p1_tally: int = 0
    p2_tally: int = 0
    puzzle, points, max_x, max_y = parse_input()
    for x_point in find_points("X", puzzle):
        surrounding = find_surrounding(x_point, 3, max_x, max_y)
        for ray in surrounding:
            if test_ray(ray, points):
                p1_tally += 1
    print("p1: ", p1_tally)

    for square in gen_squares(puzzle, 3):
        if test_square(square):
            p2_tally += 1
    print("p2: ", p2_tally)


if __name__ == "__main__":
    main()
