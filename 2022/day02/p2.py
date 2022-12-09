#!/usr/bin/env python3

import fileinput

# a, x rock      1 - loose
# b, y paper     2 - draw
# c, z scissors  3 - win


def calc_score(theirs: str, mine: str) -> int:
    if theirs == "A" and mine == "X":
        return 3 + 0
    elif theirs == "B" and mine == "Y":
        return 2 + 3
    elif theirs == "C" and mine == "Z":
        return 1 + 6
    elif theirs == "B" and mine == "X":
        return 1 + 0
    elif theirs == "C" and mine == "Y":
        return 3 + 3
    elif theirs == "A" and mine == "Z":
        return 2 + 6
    elif theirs == "C" and mine == "X":
        return 2 + 0
    elif theirs == "A" and mine == "Y":
        return 1 + 3
    elif theirs == "B" and mine == "Z":
        return 3 + 6
    print(f"unknown. {theirs} {mine}")
    return 0


def calc_new(theirs: str, mine: str) -> int:
    mi, ti, outcome = 0, 0, 0
    if theirs == "A":
        ti = 0
    elif theirs == "B":
        ti = 1
    elif theirs == "C":
        ti = 2
    if mine == "X":    # loose
        mi = (ti + 2) % 3
        outcome = 0
    elif mine == "Y":    # draw
        mi = ti
        outcome = 3
    elif mine == "Z":    # win
        mi = (ti + 1) % 3
        outcome = 6
    myval = mi + 1
    return outcome + myval


def main() -> None:
    score = 0
    score_new = 0
    for line in fileinput.input():
        theirs, mine = line.strip().split(" ")
        score += calc_score(theirs, mine)
        score_new += calc_new(theirs, mine)
    print(f"score is {score} {score_new}")


if __name__ == "__main__":
    main()
