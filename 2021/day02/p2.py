#!/usr/bin/env python3

import fileinput
import sys
import typing


def main() -> None:
    horizontal = 0
    depth = 0
    aim = 0
    for line in fileinput.input():
        direction, delta_str = line.strip().split()
        delta = int(delta_str)
        if direction == "forward":
            horizontal += delta
            depth += aim * delta
        elif direction == "up":
            aim = aim - delta
        elif direction == "down":
            aim += delta
    print(f"horizontal: {horizontal} depth: {depth} aim: {aim} product (h*d): {horizontal*depth}")


if __name__ == "__main__":
    main()

