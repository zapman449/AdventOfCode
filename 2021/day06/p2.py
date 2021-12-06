#!/usr/bin/env python3

import collections
import fileinput
import pprint
import sys
import typing


class FishGeneration(object):
    def __init__(self, age: int, count: int) -> None:
        self.age = age
        self.count = count

    def __repr__(self) -> str:
        return f"age {self.age} count {self.count}"

    def add_to(self, new_fish: int):
        self.count += new_fish

    def decrement(self) -> int:
        if self.age == 0:
            self.age = 6
            return self.count
        self.age -= 1
        return 0


def print_the_sea(state: typing.List[FishGeneration], count7, count8, final=False) -> str:
    result = []
    tally = count7 + count8
    for fg in state:
        tally += fg.count
        result.append(repr(fg))
    fmt = " - ".join(result)
    if final:
        return f"total {tally}"
    else:
        return f"total {tally} repr {fmt}"


def main() -> None:
    state: typing.List[FishGeneration] = []
    tstate: typing.List[int] = []
    for line in fileinput.input():
        tstate = [int(x) for x in line.strip().split(",")]
    for f in range(7):
        state.append(FishGeneration(f, tstate.count(f)))

    count8 = 0
    count7 = 0
    # print(f"day 00: total fish: {print_the_sea(state, count7, count8)}")
    # for day in range(1, 81):
    for day in range(1, 257):
        tally = 0
        for fg in state:
            tally += fg.decrement()
            if fg.age == 6:
                fg.add_to(count7)
        count7 = count8
        count8 = tally

        # if day < 19:
        #     print(f"day {str(day).zfill(2)}: total fish: {print_the_sea(state, count7, count8)}")
        # elif day > 76:
        #     print(f"day is {day} total fish: {print_the_sea(state, count7, count8, True)}")
        if day == 18:
            print(f"day 18 fish count: {print_the_sea(state, count7, count8, True)}")
    print(f"final fish count: {print_the_sea(state, count7, count8, True)}")


if __name__ == "__main__":
    main()
