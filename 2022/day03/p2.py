#!/usr/bin/env python3

import fileinput
import string


def character2priority(c: str) -> int:
    v = string.ascii_lowercase.find(c) + 1
    if v == 0:
        v = string.ascii_uppercase.find(c) + 26 + 1
    return v


def main() -> None:
    group3 = []
    rolling_badge_priority = 0
    for line in fileinput.input():
        sline = line.strip()
        if len(group3) != 2:
            group3.append(sline)
            continue

        group3.append(sline)
        s1 = set(group3[0])
        s2 = set(group3[1])
        s3 = set(group3[2])
        isect = s1.intersection(s2).intersection(s3)
        for c in isect:
            # print(f"found c {c} with c2p {character2priority(c)}")
            rolling_badge_priority += character2priority(c)
        group3 = []

    print(f"scores are part1: {rolling_badge_priority} part2: {rolling_badge_priority}")


if __name__ == "__main__":
    main()
