#!/usr/bin/env python3

import collections
import fileinput

def main() -> None:
    # parse input
    col1, col2 = [], []
    for line in fileinput.input():
        n1, n2 = map(int, line.split())
        col1.append(n1)
        col2.append(n2)
    col1.sort()
    col2.sort()
    count_col2 = collections.Counter(col2)

    # part 1
    tally = 0
    for n1, n2 in zip(col1, col2):
        tally += abs(n1 - n2)
    print("part1: ", tally)

    # part 2
    tally = 0
    for n1 in col1:
        c = count_col2[n1]
        tally += (n1 * c)
    print("part2: ", tally)


if __name__ == '__main__':
    main()