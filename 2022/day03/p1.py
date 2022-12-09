#!/usr/bin/env python3

import fileinput
import string


def character2priority(c: str) -> int:
    v = string.ascii_lowercase.find(c) + 1
    if v == 0:
        v = string.ascii_uppercase.find(c) + 26 + 1
    return v


def main() -> None:
    rolling_priority = 0
    for line in fileinput.input():
        sline = line.strip()
        l = len(sline) // 2
        c1 = sline[:l]
        c2 = sline[l:]
        s1 = set(list(c1))
        s2 = set(list(c2))
        isect = s1.intersection(s2)
        # print(f"l {l} c1 {c1} c2 {c2} isect {isect}")
        for c in isect:
            # print(f"found c {c} with c2p {character2priority(c)}")
            rolling_priority += character2priority(c)

    print(f"scores are part1: {rolling_priority} part2: {rolling_priority}")


if __name__ == "__main__":
    main()
