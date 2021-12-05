#!/usr/bin/env python3

"""

"""

import collections
import copy
import fileinput
import typing
import sys


def calc(start: typing.List[int], end: int) -> int:
    turn = len(start) - 1
    memory = collections.defaultdict(int)
    current: int = 0
    previous: int = 0
    for start_turn, value in enumerate(start):
        memory[value] = start_turn + 1
        current = value
    del(memory[current])
    # print(f"boundary: memory is {memory} turn is {turn} current is {current}")
    while turn < end:
        turn += 1
        if current not in memory:
            # print(f"turn {turn} current {current} not in memory.  setting memory[{current}] to {turn}, and 'next' will be 0")
            memory[current] = turn
            previous = current
            current = 0
        else:
            # print(f"turn {turn} current {current} in memory at {memory[current]}.  setting memory[{current}] to {turn}, and 'next' will be {turn - memory[current]}")
            tmp = memory[current]
            memory[current] = turn
            previous = current
            current = turn - tmp
        # print(f"end of turn {turn} spoken number is {previous} memory is {memory}")
    # print(f"DONE: turn {turn} previous is {previous} current is {current}")
    return previous


def main() -> None:
    for line in fileinput.input():
        words = [int(x) for x in line.strip().split(',')]
        # result = calc(words, 10)
        # result = calc(words, 2020)
        result = calc(words, 30000000)
        print(f"result for {words} is {result}")


if __name__ == "__main__":
    main()
