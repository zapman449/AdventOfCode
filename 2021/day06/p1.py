#!/usr/bin/env python3

import collections
import fileinput
import pprint
import sys
import typing


def main() -> None:
    state: typing.List[int] = []
    for line in fileinput.input():
        state = [int(x) for x in line.strip().split(",")]
    print(f"day 00: sum: {sum(state)} {','.join(map(str, state))}")
    for day in range(1, 81):
        new: typing.List[int] = []
        for idx, fish in enumerate(state):
            if fish == 0:
                new.append(8)
                state[idx] = 6
            else:
                state[idx] -= 1
        state.extend(new)
        # if day < 19:
        #     print(f"day {str(day).zfill(2)}: total fish: {len(state)} {','.join(map(str, state))}")
        # elif day > 76:
        #     print(f"day is {day} total fish: {len(state)}")
    print(f"final fish count: {len(state)}")


if __name__ == "__main__":
    main()
