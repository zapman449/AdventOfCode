#!/usr/bin/env python3

import collections
import fileinput
import itertools
import typing


def gather() -> typing.List[int]:
    result: typing.List[int] = []
    for line in fileinput.input():
        result.append(int(line.strip()))
    return result


def traverse(prologue: int, data: typing.List[int]) -> int:
    trailing = collections.deque(data[:prologue], prologue)
    for datum in data[prologue:]:
        found = False
        for x, y in itertools.combinations(trailing, 2):
            # print(f"DEBUG: looking for {datum} with {x} + {y} which is {x+y}")
            if x + y == datum:
                found = True
                break
        if not found:
            return datum
        trailing.append(datum)
    return -1


def main() -> None:
    data = gather()
    # print(traverse(5, data))
    print(traverse(25, data))


if __name__ == "__main__":
    main()