#!/usr/bin/env python3

import fileinput
import string


def main() -> None:
    fully_contains = 0
    overlap = 0
    for line in fileinput.input():
        nums = line.strip().replace(",", "-").split("-")
        a1s, a1e, a2s, a2e = map(int, nums)
        if a1s <= a2s and a1e >= a2e:
            fully_contains += 1
        elif a1s >= a2s and a1e <= a2e:
            fully_contains += 1
        s1 = {v for v in range(a1s, a1e+1)}
        for v in range(a2s, a2e+1):
            if v in s1:
                overlap += 1
                break

    print(f"part1: {fully_contains}, part2: {overlap}")


if __name__ == "__main__":
    main()
