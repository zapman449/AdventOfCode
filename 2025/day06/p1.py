#!/usr/bin/env python3

# import collections
# import collections
import fileinput
# import functools
# import itertools
import math
import sys
import typing


def parse_input() -> typing.Tuple[typing.List[typing.List[int]], typing.List[typing.List[int]], typing.List[str]]:
    p1_problems: typing.List[typing.List[int]] = list()
    p2_problems: typing.List[typing.List[int]] = list()
    p2_tmp: typing.List[str] = list()
    operators: typing.List[str] = list()
    first = True
    for line in fileinput.input():
        entries = line.strip().split()
        if first:
            first = False
            l = len(entries)
            p1_problems = [[] for _ in range(l)]
            p2_problems = [[] for _ in range(l)]
        if "+" in entries or "*" in entries:
            operators = entries
            # finalize p2 parsing:
            # transpose across the diagonal axis
            transposed = ["".join(row) for row in zip(*p2_tmp)]
            idx = 0
            # transposed looks like
            # ['1  ', '24 ', '356', '   ', '369', '248', '8  ', '   ', ' 32', '581', '175', '   ', '623', '431', '  4']
            # so, strip the strings, turn to int unless it's empty. empty designates the problem boundary
            for e in transposed:
                es = e.strip()
                if len(es) == 0:
                    idx += 1
                else:
                    p2_problems[idx].append(int(es))
        else:
            for idx, num in enumerate(entries):
                p1_problems[idx].append(int(num))
            # grab the whole string and stash it for later
            p2_tmp.append(line.strip("\n"))
    return p1_problems, p2_problems, operators


def run_tests():
    success = True
    if not success:
        sys.exit(1)


def p1(problems: typing.List[typing.List[int]], operators: typing.List[str]) -> int:
    tally = 0
    for idx, oper in enumerate(operators):
        if oper == "+":
            tally += sum(problems[idx])
        elif oper == "*":
            tally += math.prod(problems[idx])
    return tally


def main() -> None:
    run_tests()
    p1_problems, p2_problems, operators = parse_input()
    p1_tally = p1(p1_problems, operators)
    p2_tally = p1(p2_problems, operators)

    print(f"final p1_tally = {p1_tally}")
    print(f"final p2_tally = {p2_tally}")

if __name__ == "__main__":
    main()
