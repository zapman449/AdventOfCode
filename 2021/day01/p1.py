#!/usr/bin/env python3

import fileinput
import sys
import typing


def main() -> None:
    previous = None
    increase_counter = 0
    for line in fileinput.input():
        num = int(line.strip())
        if previous is None:
            pass
            # print(f"{num} (N/A)")
        elif num > previous:
            increase_counter += 1
            # print(f"{num} (increased {increase_counter}, prev is {previous})")
        else:
            pass
            # print(f"{num} (other)")
        previous = num
    print(f"increase counter is {increase_counter}")


if __name__ == "__main__":
    main()

