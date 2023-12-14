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
        self.turns = 0
        self.rotation_cache: typing.Dict[int, int] = {hash(self): self.turns}
        self.rotation_scores: typing.Dict[int, int] = {self.turns: self.calculate_score()}

    def print_map(self) -> None:
        for row in self.data:
            print("".join(row))
        print()

    def __str__(self) -> str:
        return "".join("".join(row) for row in self.data)

    def __hash__(self) -> int:
        return hash(str(self))

    def get_value(self, point: Point) -> typing.Optional[str]:
        if point is None:
            return None
        return self.data[point.y][point.x]

    def set_value(self, point: Point, value: str) -> None:
        self.data[point.y][point.x] = value

    def swap_values(self, p1: Point, p2: Point) -> None:
        if p1 is None or p2 is None:
            return
        v1 = self.get_value(p1)
        v2 = self.get_value(p2)
        self.set_value(p1, v2)
        self.set_value(p2, v1)

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

    def _direction_swap(self, point: Point, fp):
        if self.get_value(point) != "O":
            return None
        up = fp(point)
        if up is None:
            return None
        elif self.get_value(up) != ".":
            return None
        upup = fp(up)
        if upup is None or self.get_value(upup) != ".":
            self.swap_values(point, up)
            return None
        while self.get_value(upup) == ".":
            up = fp(up)
            upup = fp(up)
        self.swap_values(point, up)

    def tilt_north(self):
        for y in range(self.min_y, self.max_y):
            for x in range(self.min_x, self.max_x):
                point = Point(x, y)
                self._direction_swap(point, self._point_north)

    def tilt_south(self):
        for y in range(self.max_y - 1, self.min_y - 1, -1):
            for x in range(self.min_x, self.max_x):
                point = Point(x, y)
                self._direction_swap(point, self._point_south)

    def tilt_east(self):
        for x in range(self.max_x - 1, self.min_x - 1, -1):
            for y in range(self.min_y, self.max_y):
                point = Point(x, y)
                self._direction_swap(point, self._point_east)

    def tilt_west(self):
        for x in range(self.min_x, self.max_x):
            for y in range(self.min_y, self.max_y):
                point = Point(x, y)
                self._direction_swap(point, self._point_west)

    def keep_rotating(self, full_rotations: int) -> int:
        fps = [self.tilt_north, self.tilt_west, self.tilt_south, self.tilt_east]
        while True:
            fp = fps[self.turns % 4]
            fp()
            self.turns += 1
            if hash(self) in self.rotation_cache:
                break
            self.rotation_cache[hash(self)] = self.turns
            self.rotation_scores[self.turns] = self.calculate_score()

        cycle_start = self.rotation_cache[hash(self)]
        cycle_length = self.turns - cycle_start
        idx = (full_rotations*4 - cycle_start) % cycle_length
        print(f"DEBUG: turns {self.turns} cycle_start {cycle_start}, cycle_length {cycle_length}, idx {idx}")
        score = self.rotation_scores[cycle_start + idx]
        return score

    def calculate_score(self) -> int:
        score = 0
        for y in range(self.min_y, self.max_y):
            multiplier = self.max_y - y
            for x in range(self.min_x, self.max_x):
                point = Point(x, y)
                if self.get_value(point) == "O":
                    score += multiplier
        return score


def main() -> None:
    args = parse_args()
    data = get_input(args.input)
    p2_data = copy.deepcopy(data)
    platform = Map(data)
    platform.tilt_north()
    print(f"p1: {platform.calculate_score()}")
    platform = Map(p2_data)
    score = platform.keep_rotating(1000000000)
    print(f"p2: {score}")


if __name__ == "__main__":
    main()
