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

    def above(self) -> typing.Tuple[int, int]:
        return self.x, self.y-1

    def beside(self) -> typing.Tuple[int, int, int, int]:
        return self.x-1, self.y, self.x+1, self.y


def parse_input() -> typing.Tuple[typing.Dict[Point, str], int, int]:
    data: typing.Dict[Point, str] = collections.defaultdict(str)
    y = 0
    max_x = 0
    max_y = 0
    for line in fileinput.input():
        if y > max_y:
            max_y = y
        for x, c in enumerate(line.strip()):
            data[Point(x,y)] = c
            if x > max_x:
                max_x = x
        y += 1
    return data, max_x, max_y


def run_tests():
    success = True
    if not success:
        sys.exit(1)


def p1(data: typing.Dict[Point, str], max_x, max_y: int) -> int:
    tally = 0
    for y in range(1, max_y):
        for x in range(max_x):
            p = Point(x, y)
            xpa, ypa = p.above()
            pa = Point(xpa, ypa)
            if data[pa] == "S":
                data[p] = "|"
            elif data[p] == "^" and data[pa] == "|":
                a, b, c, d = p.beside()
                pl = Point(a, b)
                pr = Point(c, d)
                data[pl] = "|"
                data[pr] = "|"
                tally += 1
                # print(f"{p} {data[pl]}, {data[p]}, {data[pr]}")
            elif data[pa] == "|":
                data[p] = "|"
    return tally


def p2(data: typing.Dict[Point, str], max_x, max_y: int) -> int:
    count_list = [0] * (max_x+1)
    for y in range(max_y):
        for x in range(max_x):
            p = Point(x,y)
            c = data[p]
            if c == "S":
                count_list[x] = 1
            elif c == "^":
                try:
                    t = count_list[x]
                    count_list[x] = 0
                    count_list[x-1] += t
                    count_list[x+1] += t
                except:
                    print(f"{count_list=} {x=}, {y=} {c=}")
                    raise
    return sum(count_list)


def main() -> None:
    data, max_x, max_y = parse_input()

    run_tests()

    p1_tally = p1(data, max_x, max_y)
    p2_tally = p2(data, max_x, max_y)

    print(f"p1 final {p1_tally}")
    print(f"p2 final {p2_tally}")

if __name__ == "__main__":
    main()
