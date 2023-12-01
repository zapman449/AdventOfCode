#!/usr/bin/env python3

import collections
import copy
import fileinput
import pprint
import re
import statistics
import sys
import typing


SHORT = "target area: x=20..30, y=-10..-5"
REAL = "target area: x=240..292, y=-90..-57"


class Candidate(object):
    def __init__(self, x: int, steps: typing.List[int], zeros: bool) -> None:
        self.x = x
        self.steps_to_zone = steps
        self.zeros_within_bounds = zeros

    def __repr__(self):
        short_bool = "F"
        if self.zeros_within_bounds:
            short_bool = "T"
        return f"{self.x} -> {repr(self.steps_to_zone)} {short_bool}"


class XYHeight(typing.NamedTuple):
    x: int
    y: int
    height: int


def split_dim(input_data: str) -> typing.Tuple[int, int]:
    first = input_data.split("=")
    second = first[1].replace(",", "").split("..")
    return int(second[0]), int(second[1])


def find_delta_x(x_min: int, x_max: int) -> typing.Tuple[typing.List[Candidate], typing.Set[int]]:
    result: typing.List[Candidate] = []
    possible_step_counts: typing.Set[int] = set()
    for x in range(1, 300):
        if x > x_max:
            break
        current = 0
        steps = []
        x_valid = False
        counter = 0
        for x_prime in range(x, -1, -1):
            counter += 1
            current += x_prime
            if x_min <= current <= x_max:
                x_valid = True
                steps.append(counter)
                possible_step_counts.add(counter)
            if x_prime == 0 and x_min <= current <= x_max:
                result.append(Candidate(x, steps, True))
            if current > x_max and x_valid:
                result.append(Candidate(x, steps, False))
                break
    return result, possible_step_counts


def find_delta_y(y_min: int, y_max: int, candidate_xs: typing.List[Candidate], max_possible_steps: int) -> typing.List[int]:
    result: typing.List[int] = []

    return result


def main(input_data: str) -> None:
    words = input_data.split()
    x_min, x_max = split_dim(words[2])
    y_min, y_max = split_dim(words[3])
    candidate_xs, possible_step_counts = find_delta_x(x_min, x_max)
    print(repr(candidate_xs))
    print(repr(possible_step_counts))


if __name__ == "__main__":
    main(SHORT)
    # main(REAL)
