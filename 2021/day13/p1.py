#!/usr/bin/env python3

import collections
import copy
import fileinput
import pprint
import re
import statistics
import sys
import typing


class Fold(typing.NamedTuple):
    axis: str
    index: int


class Point(typing.NamedTuple):
    x: int
    y: int


def paper_printer(data: typing.Dict[Point, str]) -> None:
    xs = []
    ys = []
    for p in data:
        xs.append(p.x)
        ys.append(p.y)
    x_max = max(xs) + 1
    y_max = max(ys) + 1
    for y in range(y_max):
        row = []
        for x in range(x_max):
            p = Point(x, y)
            if p in data:
                row.append('x')
            else:
                row.append(' ')
        print("".join(reversed(row)))


def modulate(point_value: int, fold: Fold) -> int:
    # X fold
    # start: abcdeFghijk
    # end: ghijk 6789a -> 01234
    # end: edcba 01234 -> 43210
    # 4 3 2 1 0  if below axis_val, axis_val-1-x
    # 6 7 8 9 a  if above axis_val, x-axis_val+1
    if fold.axis == "x":
        if point_value < fold.index:
            return fold.index - 1 - point_value
        return point_value - (fold.index + 1)
    else:
        if point_value > fold.index:
            return fold.index - (point_value - fold.index)
        return point_value


def fold_point(point: Point, folds: typing.List[Fold]) -> typing.Optional[Point]:
    x = point.x
    y = point.y
    for fold in folds:
        if fold.axis == "x":
            if x == fold.index:
                return None
            x = modulate(x, fold)
        elif fold.axis == "y":
            if y == fold.index:
                return None
            y = modulate(y, fold)
    return Point(x, y)


def main() -> None:
    folds: typing.List[Fold] = []
    one_fold: typing.Dict[Point, str] = {}
    all_folds: typing.Dict[Point, str] = {}
    for line in fileinput.input():
        if line.startswith('fold along'):
            words = line.strip().split()
            f = words[2].split("=")
            folds.append(Fold(f[0], int(f[1])))
        else:
            x, y = line.strip().split(',')
            p = Point(int(x), int(y))
            p_prime = fold_point(p, folds[0:1])
            one_fold[p_prime] = "x"
            p2_prime = fold_point(p, folds)
            all_folds[p2_prime] = "x"
            # print(f"DEBUG: p {p}, folds {repr(folds)} p_prime {p_prime} p2_prime {p2_prime}")
    print(f"p1 answer: {len(one_fold)}")
    print(f"p1_prime answer: {len(all_folds)}")
    # print("printing one_fold:")
    # paper_printer(one_fold)
    paper_printer(all_folds)


if __name__ == "__main__":
    main()
