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
        # print(f"expect {repr(expect)} current {current} line_remains {line_remains}")
        if len(expect) == 0:
            expect.append(current)
            continue
        previous = expect[-1]
        if current == ')' and previous in   (     '[', '{', '<'):
            return 3
        elif current == ']' and previous in ('(',      '{', '<'):
            return 57
        elif current == '}' and previous in ('(', '[',      '<'):
            return 1197
        elif current == '>' and previous in ('(', '[', '{',    ):
            return 25137
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
    return 0


def main() -> None:
    scores = []
    total = 0
    for line in fileinput.input():
        score = stack_math(line.strip())
        total += score
        # print(f"line {line.strip()} = score {score}")
    print(f"total is {total}")


if __name__ == "__main__":
    # l = '{([(<{}[<>[]}>{[]{[(<()>'
    # s = stack_math(l)
    # print(f"line {l} score {s}")
    main()
