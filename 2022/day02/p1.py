#!/usr/bin/env python3

import fileinput

solutions = {
    "A X": (1+3, 3+0),
    "B Y": (2+3, 2+3),
    "C Z": (3+3, 1+6),
    "B X": (1+0, 1+0),
    "C Y": (2+0, 3+3),
    "A Z": (3+0, 2+6),
    "C X": (1+6, 2+0),
    "A Y": (2+6, 1+3),
    "B Z": (3+6, 3+6),
}


def main() -> None:
    score_p1 = 0
    score_p2 = 0
    for line in fileinput.input():
        l = line.strip()
        score_p1 += solutions[l][0]
        score_p2 += solutions[l][1]
    print(f"scores are part1: {score_p1} part2: {score_p2}")


if __name__ == "__main__":
    main()

# a, x rock      1 0
# b, y paper     2 1
# c, z scissors  3 2

# 0 - 2 win
# 1 - 0 win
# 2 - 1 win
# win if +1 or -2

# if 0, draw
# 2 - 0
# 0 - 1
# 1 - 2
# loose if +2 or -1


# def calc_score(theirs: str, mine: str) -> int:
#     if theirs == "A" and mine == "X":
#         return 1 + 3
#     elif theirs == "B" and mine == "Y":
#         return 2 + 3
#     elif theirs == "C" and mine == "Z":
#         return 3 + 3
#     elif theirs == "B" and mine == "X":
#         return 1 + 0
#     elif theirs == "C" and mine == "Y":
#         return 2 + 0
#     elif theirs == "A" and mine == "Z":
#         return 3 + 0
#     elif theirs == "C" and mine == "X":
#         return 1 + 6
#     elif theirs == "A" and mine == "Y":
#         return 2 + 6
#     elif theirs == "B" and mine == "Z":
#         return 3 + 6
#     print(f"unknown. {theirs} {mine}")
#     return 0



# def calc_new(theirs: str, mine: str) -> int:
#     mi, ti, myval, outcome = 0, 0, 0, 0
#     if theirs == "A":
#         ti = 0
#     elif theirs == "B":
#         ti = 1
#     elif theirs == "C":
#         ti = 2
#     if mine == "X":
#         mi = 0
#         myval = 1
#     elif mine == "Y":
#         mi = 1
#         myval = 2
#     elif mine == "Z":
#         mi = 2
#         myval = 3
#     result = mi - ti
#     if result == 1 or result == -2:
#         outcome = 6
#     elif result == 2 or result == -1:
#         outcome = 0
#     else:   # result = 0
#         outcome = 3
#     return outcome + myval


# def main_old() -> None:
#     score = 0
#     score_new = 0
#     score_three_one = 0
#     score_three_two = 0
#     for line in fileinput.input():
#         theirs, mine = line.strip().split(" ")
#         score += calc_score(theirs, mine)
#         score_new += calc_new(theirs, mine)
#         l = line.strip()
#         score_three_one += solutions[l][0]
#         score_three_two += solutions[l][1]
#     print(f"score is {score} {score_new} {score_three_one} {score_three_two}")



