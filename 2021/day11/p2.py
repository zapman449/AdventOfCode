#!/usr/bin/env python3

import collections
import copy
import fileinput
import pprint
import statistics
import sys
import typing

Point = collections.namedtuple("Point", 'x y')


class Octopus(object):
    def __init__(self, start: int) -> None:
        self.value = start
        self.flashed = False

    def __str__(self) -> str:
        if self.flashed:
            return "x"
        return str(self.value)

    def increment_flash(self) -> bool:
        if self.value < 9:
            self.value += 1
            return False
        elif self.flashed is False:
            self.flashed = True
            return True
        else:
            return False

    def clear_flash(self) -> None:
        if self.flashed:
            self.value = 0
            self.flashed = False


def inbounds(point: Point) -> bool:
    if point.x < 0 or point.y < 0:
        return False
    if point.x > 9 or point.y > 9:
        return False
    return True


def surrounding_points(point: Point) -> typing.Set[Point]:
    points = set()
    for x in (point.x-1, point.x, point.x+1):
        for y in (point.y - 1, point.y, point.y + 1):
            if x == point.x and y == point.y:
                continue
            potential = Point(x, y)
            if inbounds(potential):
                points.add(potential)
    return points


def print_grid(data: typing.List[typing.List[Octopus]]) -> None:
    for row in data:
        print("".join([str(c) for c in row]))


def flash_recurse(master_flash: typing.Set[Point], need_to_flash: typing.Set[Point], data: typing.List[typing.List[Octopus]]) -> None:
    next_level_flashers: typing.Set[Point] = set()
    for flash_point in need_to_flash:
        surrounding = surrounding_points(flash_point)
        for s_point in surrounding:
            if data[s_point.y][s_point.x].increment_flash():
                master_flash.add(s_point)
                next_level_flashers.add(s_point)
    if len(next_level_flashers) > 0:
        flash_recurse(master_flash, next_level_flashers, data)
    return


def main() -> None:
    data: typing.List[typing.List[Octopus]] = []
    row = 0
    for line in fileinput.input():
        data.append([])
        for idx, c in enumerate(line.strip()):
            data[row].append(Octopus(int(c)))
        row += 1
    # print("initial grid")
    # print_grid(data)
    # print()
    # total_flashes = 0
    step = 0
    while True:
        step += 1
        flashers: typing.Set[Point] = set()
        for y, row in enumerate(data):
            for x, octopus in enumerate(row):
                if octopus.increment_flash():
                    flashers.add(Point(x, y))
        flashers_copy = copy.copy(flashers)
        flash_recurse(flashers, flashers_copy, data)
        # total_flashes += len(flashers)
        for flash in flashers:
            data[flash.y][flash.x].clear_flash()
        if len(flashers) == 100:
            print(f"step where all flash is {step}")
            break
        if step > 300:
            print("failure")
            break


if __name__ == "__main__":
    main()
