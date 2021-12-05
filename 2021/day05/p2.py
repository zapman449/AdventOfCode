#!/usr/bin/env python3

import collections
import fileinput
import numpy
import pprint
import sys
import typing


class Map(object):
    def __init__(self) -> None:
        self.map = numpy.array([[0, 0],
                                [0, 0]])
        self.dmap = collections.defaultdict(int)

    def get_points(self, x1: int, y1: int, x2: int, y2: int) -> typing.Union[typing.List[typing.Tuple[int, int]], None]:
        orig = f"{x1}, {y1} -> {x2}, {y2}"
        # if x1 != x2 and y1 != y2:
        #     print(f"skipping diagonal line {x1},{y1} -> {x2},{y2}")
        #     return None
        if x1 == x2:
            xs = (abs(y1 - y2)+1) * [x1, ]
            if y1 > y2:
                ystep = -1
                y2 -= 1
            else:
                ystep = 1
                y2 += 1
            points = zip(xs, range(y1, y2, ystep))
        elif y1 == y2:
            ys = (abs(x1 - x2)+1) * [y1, ]
            if x1 > x2:
                xstep = -1
                x2 -= 1
            else:
                xstep = 1
                x2 += 1
            points = zip(range(x1, x2, xstep), ys)
            # print(f"DEBUG: {orig} ys {ys} xstep {xstep} x1 {x1} x2 {x2}")
        else:
            if x1 < x2:
                xstep = 1
                x2 += 1
            else:
                xstep = -1
                x2 -= 1
            if y1 < y2:
                ystep = 1
                y2 += 1
            else:
                ystep = -1
                y2 -= 1
            points = zip(range(x1, x2, xstep), range(y1, y2, ystep))
        # print(f"{orig} has points {repr(list(points))}")
        return list(points)

    # def resize(self, x1: int, y1: int, x2: int, y2: int) -> None:
    #     current_max_y, current_max_x = numpy.shape(self.map)
    #     new_max_x_delta = abs(max(x1, x2, current_max_x) - current_max_x)
    #     new_max_y_delta = abs(max(y1, y2, current_max_y) - current_max_y)
    #     self.map = numpy.pad(self.map, ((0, new_max_y_delta), (0, new_max_x_delta)), 'constant', constant_values=(0, 0))

    def add_line(self, x1: int, y1: int, x2: int, y2: int) -> None:
        # self.resize(x1, y1, x2, y2)
        points = self.get_points(x1, y1, x2, y2)
        if points is None:
            return None
        for point in points:
            self.dmap[point] += 1

    def count_intersections(self) -> int:
        counter = 0
        for key, value in self.dmap.items():
            if value >= 2:
                counter += 1
        return counter


def main() -> None:
    map = Map()
    for line in fileinput.input():
        words = line.strip().split()
        p1 = words[0].split(',')
        p2 = words[2].split(',')
        map.add_line(int(p1[0]), int(p1[1]), int(p2[0]), int(p2[1]))

    print(f"intersection count is {map.count_intersections()}")


if __name__ == "__main__":
    main()
