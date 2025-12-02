#!/usr/bin/env python3

import collections
import fileinput
import functools
import typing

class Turn(typing.NamedTuple):
    direction: int
    distance: int

    def value(self, prev: int) -> int:
        v = prev + (self.direction * self.distance)
        if v < 0:
            while v < 0:
                v = v + 100
        else:
            while v > 99:
                v = v - 100
        return v

def parse_input() -> typing.List[Turn]:
    out = []
    for line in fileinput.input():
        uline = line.strip()
        direction = 1
        if line[0] == "L":
            direction = -1
        distance = int(uline[1:])
        t = Turn(direction, distance)
        out.append(t)
    return out


def main() -> None:
    p1_tally = 0
    turns = parse_input()
    idx = 50
    for turn in turns :
        pidx = idx
        idx = turn.value(idx)
        if idx == 0:
            p1_tally += 1
        # print(f"{pidx=} -> {idx=} -- {p1_tally=}")
    print(f"final {p1_tally=}")

if __name__ == "__main__":
    main()
