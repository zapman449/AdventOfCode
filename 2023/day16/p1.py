#!/usr/bin/env python3

import argparse
import collections
import copy
import itertools
import hashlib
import pprint
import sys
import typing


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("input", help="input file")
    return parser.parse_args()


def get_input(in_file: str) -> typing.List[str]:
    with open(in_file) as f:
        return f.read().splitlines()


class Point(typing.NamedTuple):
    x: int
    y: int


class Map:
    def __init__(self, data: typing.List[str]) -> None:
        self.data: typing.List[typing.List[str]] = [list(row) for row in data]
        self.max_x = len(data[0])
        self.max_y = len(data)
        self.min_x = 0
        self.min_y = 0
        self.energized: typing.Set[Point] = set()
        self.energized_cycle_cache: typing.Set[typing.Tuple[Point, str]] = set()
        self.period_dict = {
            "N": self._point_south,
            "S": self._point_north,
            "W": self._point_east,
            "E": self._point_west,
        }
        self.slash_dict = {
            "N": (self._point_west, "E"),
            "S": (self._point_east, "W"),
            "E": (self._point_south, "N"),
            "W": (self._point_north, "S"),
        }
        self.backslash_dict = {
            "N": (self._point_east, "W"),
            "S": (self._point_west, "E"),
            "E": (self._point_north, "S"),
            "W": (self._point_south, "N"),
        }

    def deenergize(self) -> None:
        self.energized = set()
        self.energized_cycle_cache = set()

    def print_map(self, energized=True) -> None:
        for y in range(self.min_y, self.max_y):
            for x in range(self.min_x, self.max_x):
                point = Point(x, y)
                if energized and point in self.energized:
                    print("#", end="")
                else:
                    print(self.get_value(point), end="")
            print()
        print()

    def __str__(self) -> str:
        return "".join("".join(row) for row in self.data)

    def get_value(self, point: Point) -> typing.Optional[str]:
        if point is None:
            return None
        return self.data[point.y][point.x]

    def _point_north(self, point: Point) -> typing.Optional[Point]:
        new_point = Point(point.x, point.y - 1)
        if new_point.y < self.min_y:
            return None
        return new_point

    def _point_south(self, point: Point) -> typing.Optional[Point]:
        new_point = Point(point.x, point.y + 1)
        if new_point.y >= self.max_y:
            return None
        return new_point

    def _point_west(self, point: Point) -> typing.Optional[Point]:
        new_point = Point(point.x - 1, point.y)
        if new_point.x < self.min_x:
            return None
        return new_point

    def _point_east(self, point: Point) -> typing.Optional[Point]:
        new_point = Point(point.x + 1, point.y)
        if new_point.x >= self.max_x:
            return None
        return new_point

    def parse_reflect(self, point: Point, source_direction: str) -> typing.Tuple[typing.Optional[Point], str]:
        value = self.get_value(point)
        if value == "/":
            fp, d = self.slash_dict[source_direction]
            return fp(point), d
        elif value == "\\":
            fp, d = self.backslash_dict[source_direction]
            return fp(point), d

    def parse_split(self, point: Point, source_direction: str) -> typing.Tuple[typing.Tuple[typing.Optional[Point], str], typing.Tuple[typing.Optional[Point], str]]:
        value = self.get_value(point)
        if value == "|":
            if source_direction == "N":
                return (self._point_south(point), source_direction), (None, "")
            elif source_direction == "S":
                return (self._point_north(point), source_direction), (None, "")
            elif source_direction == "E" or source_direction == "W":
                return (self._point_north(point), "S"), (self._point_south(point), "N")
        elif value == "-":
            if source_direction == "E":
                return (self._point_west(point), source_direction), (None, "")
            elif source_direction == "W":
                return (self._point_east(point), source_direction), (None, "")
            elif source_direction == "N" or source_direction == "S":
                return (self._point_east(point), "W"), (self._point_west(point), "E")

    def traverse(self, point: Point, source_direction: str) -> typing.Optional[Point]:
        if point is None:
            return None
        if (point, source_direction) in self.energized_cycle_cache:
            return None
        self.energized.add(point)
        self.energized_cycle_cache.add((point, source_direction))
        value = self.get_value(point)
        if value == ".":
            np = self.period_dict[source_direction](point)
            return self.traverse(np, source_direction)
        elif value == "/" or value == "\\":
            np, nd = self.parse_reflect(point, source_direction)
            return self.traverse(np, nd)
        elif value == "|" or value == "-":
            d1, d2 = self.parse_split(point, source_direction)
            self.traverse(d1[0], d1[1])
            self.traverse(d2[0], d2[1])

    def calculate_score(self) -> int:
        return len(self.energized)

    def best_origin(self) -> int:
        highest = 0
        print(f"testing from N")
        for x in range(self.min_x, self.max_x):
            self.traverse(Point(x, self.min_y), "N")
            score = self.calculate_score()
            self.deenergize()
            if score > highest:
                highest = score

        print(f"testing from W")
        for y in range(self.min_y, self.max_y):
            self.traverse(Point(self.min_x, y), "W")
            score = self.calculate_score()
            self.deenergize()
            if score > highest:
                highest = score

        print(f"testing from S")
        for x in range(self.min_x, self.max_x):
            self.traverse(Point(x, self.max_y-1), "S")
            score = self.calculate_score()
            self.deenergize()
            if score > highest:
                highest = score

        print(f"testing from E")
        for y in range(self.min_y, self.max_y):
            self.traverse(Point(self.max_x-1, y), "E")
            score = self.calculate_score()
            self.deenergize()
            if score > highest:
                highest = score

        return highest


def main() -> None:
    sys.setrecursionlimit(10000)
    args = parse_args()
    data = get_input(args.input)
    contraption = Map(data)
    contraption.traverse(Point(0, 0), "W")
    # contraption.print_map()
    print(f"p1: {contraption.calculate_score()}")
    contraption.deenergize()
    p2 = contraption.best_origin()
    print(f"p2: {p2}")


if __name__ == "__main__":
    main()
