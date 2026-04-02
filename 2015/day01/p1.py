#!/usr/bin/env python3

import fileinput
import sys
import typing

def process_files(data: str) -> typing.Tuple[int, int]:
    floors = 0
    basement_position = None
    for idx, char in enumerate(data):
        if char == "(":
            floors += 1
        elif char == ")":
            floors -= 1
            if floors == -1 and basement_position is None:
                basement_position = idx + 1
        elif char == "\n":
            break
        else:
            sys.exit("invalid char")
    if basement_position is None:
        sys.exit("basement_position not found")
    return floors, basement_position


def main() -> None:
    floors, basement_position = 0,0
    for line in fileinput.input():
        floors, basement_position = process_files(line.strip())
        break
    print(f"p1 result: {floors}")
    print(f"p2 result: {basement_position}")


if __name__ == "__main__":
    main()
