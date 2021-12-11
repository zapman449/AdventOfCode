#!/usr/bin/env python3

import collections
import fileinput
import pprint
import statistics
import sys
import typing


# options: complete, incomplete, or corrupted
# values for first, illegal:
# ): 3 points.
# ]: 57 points.
# }: 1197 points.
# >: 25137 points.


def stack_math(line_remains: str) -> int:
    expect: typing.List[str] = []
    for current in line_remains:
        if len(expect) == 0:
            expect.append(current)
            continue
        previous = expect[-1]
        if current == ')' and previous in   (     '[', '{', '<'):
            return 0
        elif current == ']' and previous in ('(',      '{', '<'):
            return 0
        elif current == '}' and previous in ('(', '[',      '<'):
            return 0
        elif current == '>' and previous in ('(', '[', '{',    ):
            return 0
        elif previous == '(' and current == ')':
            del(expect[-1])
        elif previous == '[' and current == ']':
            del (expect[-1])
        elif previous == '{' and current == '}':
            del (expect[-1])
        elif previous == '<' and current == '>':
            del (expect[-1])
        else:
            expect.append(current)
    expect.reverse()
    score = 0
    for char in expect:
        score = score * 5
        if char == '(':
            score += 1
        elif char == '[':
            score += 2
        elif char == '{':
            score += 3
        elif char == '<':
            score += 4
    return score


def main() -> None:
    scores = []
    for line in fileinput.input():
        score = stack_math(line.strip())
        if score == 0:
            continue
        scores.append(score)
        print(f"line {line.strip()} = score {score}")
    scores.sort()
    mid = len(scores) // 2
    print(f"mid score is {scores[mid]}")


if __name__ == "__main__":
    # l = '{([(<{}[<>[]}>{[]{[(<()>'
    # s = stack_math(l)
    # print(f"line {l} score {s}")
    main()
