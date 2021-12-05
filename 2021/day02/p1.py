#!/usr/bin/env python3

import fileinput
import sys
import typing


def main() -> None:
    horizontal = 0
    depth = 0
    for line in fileinput.input():
        direction, delta_str = line.strip().split()
        delta = int(delta_str)
        if direction == "forward":
            horizontal += delta
        elif direction == "up":
            depth = depth - delta
        elif direction == "down":
            depth = depth + delta
    print(f"horizontal: {horizontal} depth: {depth} product: {horizontal*depth}")


if __name__ == "__main__":
    main()

