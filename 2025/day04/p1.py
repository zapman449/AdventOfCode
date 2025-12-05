#!/usr/bin/env python3
import collections
# import collections
import fileinput
import functools
import itertools
import sys
import typing


class Point(typing.NamedTuple):
    x: int
    y: int

    def surrounding(self) -> typing.Iterator[typing.Tuple[int, int]]:
        yield self.x-1, self.y-1
        yield self.x, self.y-1
        yield self.x+1, self.y-1
        yield self.x-1, self.y
        # yield self.x, self.y
        yield self.x+1, self.y
        yield self.x-1, self.y+1
        yield self.x, self.y+1
        yield self.x+1, self.y+1


def parse_input() -> typing.Tuple[typing.Dict[Point, str], int, int]:
    data: typing.Dict[Point, str] = collections.defaultdict(str)
    y = 0
    max_x = 0
    max_y = 0
    for line in fileinput.input():
        for x, c in enumerate(line.strip()):
            data[Point(x,y)] = c
        y += 1
    return data, max_x, max_y


def run_tests():
    success = True
    if not success:
        sys.exit(1)


def p1(data: typing.Dict[Point, str]) -> int:
    tally = 0
    points = list(data.keys())
    for p in points:
        if data[p] != "@":
            continue
        p_tally = 0
        for xs, ys in p.surrounding():
            ps = Point(xs,ys)
            if data[ps] == "@":
                p_tally += 1
        if p_tally < 4:
            tally += 1
            data[p] = "."
    return tally


def p2(data: typing.Dict[Point, str]) -> int:
    tally = 0
    c = 0
    while True:
        c += 1
        t = p1(data)
        tally += t
        if t == 0:
            break
    return tally


def main() -> None:
    data, max_x, max_y = parse_input()
    d2 = collections.defaultdict(str)
    for p in data.keys():
        d2[p] = data[p]

    run_tests()

    p1_tally = p1(data)
    p2_tally = p2(d2)

    print(f"final {p1_tally=}")
    print(f"final {p2_tally=}")

if __name__ == "__main__":
    main()
