#!/usr/bin/env python3

import collections
import itertools
import fileinput
import functools
import typing

def parse_input() -> typing.List[typing.Tuple[int, typing.Tuple[int, ...]]]:
    problems: typing.List[typing.Tuple[int, typing.Tuple[int, ...]]] = []
    for line in fileinput.input():
        ans_str, number_str = line.strip().split(": ", 1)
        ans = int(ans_str)
        numbers = tuple(map(int, number_str.split(" ")))
        problems.append((ans, numbers))
    return problems


def operator(operation:str, a:int, b:int) -> int:
    if operation == '+':
        return a + b
    elif operation == '*':
        return a * b
    elif operation == "||":
        return int(str(a)+str(b))
    else:
        raise ValueError(f"Unknown operator: {operator}")


def solvable(answer: int, numbers: typing.Tuple[int, ...], operators:typing.List[str]) -> int:
    solutions = 0
    for op_pattern in itertools.product(operators, repeat=len(numbers)-1):
        idx = 0
        solution = numbers[0]
        # print(solution, repr(op_pattern), numbers)
        for x in numbers[1:]:
            solution = operator(op_pattern[idx], solution, x)
            idx += 1
            if solution > answer:
                break
        if solution == answer:
            solutions += 1
            break
    return solutions


def main() -> None:
    p1_tally = 0
    p2_tally = 0
    problems = parse_input()
    for answer, numbers in problems:
        solutions = solvable(answer, numbers, ['+', '*'])
        if solutions > 0:
            p1_tally += answer
        solutions = solvable(answer, numbers, ['*', '||', '+'])
        if solutions > 0:
            p2_tally += answer
    print(f"{p1_tally=}")
    print(f"{p2_tally=}")


if __name__ == "__main__":
    main()
