#!/usr/bin/env python3

import argparse
import collections
import copy
import itertools
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
    def __init__(self, empty_increment: int, data: typing.List[str]) -> None:
        self.data = data
        self.max_x = len(data[0])
        self.max_y = len(data)
        self.empty_increment = empty_increment
        self.empty_rows: typing.List[int] = []
        self.empty_columns: typing.List[int] = []
        self._inflate()
        self.galaxy_indicies: typing.Dict[int, Point] = {}
        self._find_galaxies()

    def _inflate(self) -> None:
        for idx, row in enumerate(self.data):
            if len(row.replace(".", "")) > 0:
                continue
            self.empty_rows.append(idx)

        for idx in range(self.max_x):
            ray = "".join([row[idx] for row in self.data])
            if len(ray.replace(".", "")) > 0:
                continue
            self.empty_columns.append(idx)

    def _find_galaxies(self) -> None:
        idx = 1
        for y, row in enumerate(self.data):
            for x, char in enumerate(row):
                if char == "#":
                    self.galaxy_indicies[idx] = Point(x, y)
                    self.data[y] = self.data[y][:x] + str(idx)[-1] + self.data[y][x+1:]
                    idx += 1

    def find_galactic_distance(self, g1: Point, g2: Point, msg="", debug=False) -> int:
        steps = 0
        step_log = ""
        interval = 1
        if g1.x > g2.x:
            interval = -1
        for x_prime in range(g1.x, g2.x, interval):
            if x_prime in self.empty_columns:
                steps += self.empty_increment
                step_log += "+mx"
            else:
                steps += 1
                step_log += "+1x"
        dx = steps
        steps = 0
        interval = 1
        if g1.y > g2.y:
            interval = -1
        for y_prime in range(g1.y, g2.y, interval):
            if y_prime in self.empty_rows:
                steps += self.empty_increment
                step_log += "+my"
            else:
                steps += 1
                step_log += "+1y"
        dy = steps
        if debug:
            if msg == "":
                print(f"galaxy_pair: {g1}, {g2}, dx: {dx}, dy: {dy}, distance: {dx + dy} log: {step_log}")
            else:
                print(f"galaxy_pair: msg {msg} - {g1}, {g2}, dx: {dx}, dy: {dy}, distance: {dx + dy} log: {step_log}")
        return dx + dy

    def find_galactic_distances(self) -> int:
        tally = 0
        for galaxy_pair in itertools.combinations(self.galaxy_indicies.values(), 2):
            g1, g2 = galaxy_pair
            tally += self.find_galactic_distance(g1, g2)
        return tally

    def print(self) -> None:
        for row in range(self.max_y):
            print(self.data[row])


def debug(idx1: int, idx2: int, galaxy_map: Map) -> None:
    p1 = galaxy_map.galaxy_indicies[idx1]
    p2 = galaxy_map.galaxy_indicies[idx2]
    galaxy_map.find_galactic_distance(p1, p2, msg=f"{idx1}->{idx2}", debug=True)


def main() -> None:
    args = parse_args()
    data = get_input(args.input)
    d2 = copy.deepcopy(data)
    galactic_map = Map(2, data)
    galactic_distances = galactic_map.find_galactic_distances()
    print(f"galactic_distances (p1 answer): {galactic_distances}")

    galactic_map = Map(1000000, d2)
    galactic_distances = galactic_map.find_galactic_distances()
    print(f"galactic_distances (p2 - 1,000,000 answer): {galactic_distances}")


if __name__ == "__main__":
    main()
