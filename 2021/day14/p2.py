#!/usr/bin/env python3

"""
ugh. this has an "off by one" error somewhere... the max string value is +/- 1
"""

import collections
import copy
import fileinput
import pprint
import re
import statistics
import sys
import typing


def main() -> None:
    base = None
    pair_changes: typing.Dict[str, str] = {}
    for line in fileinput.input():
        if base is None:
            base = line.strip()
            continue
        if len(line.strip()) == 0:
            continue
        words = line.strip().split(" -> ")
        lhs = words[0]
        rhs = lhs[0] + words[1] + lhs[1]
        pair_changes[lhs] = rhs

    current_pairs: typing.Dict[str, int] = collections.defaultdict(int)
    for idx, letter in enumerate(base):
        try:
            pair = letter + base[idx+1]
        except IndexError:
            continue
        current_pairs[pair] += 1
    for step in range(40):
        print(f"step {step + 1}")
        new_pairs: typing.Dict[str, int] = collections.defaultdict(int)
        for pair in list(current_pairs):
            three_letter = pair_changes[pair]
            new_pairs[three_letter[0:2]] += current_pairs[pair]
            new_pairs[three_letter[1:3]] += current_pairs[pair]
        if step in (0, 1):
            print(f"base {base}")
            print(f"current_pairs {repr(current_pairs)}")
            print(f"new_pairs {repr(new_pairs)}")
        current_pairs = new_pairs

    counting: typing.Dict[str, int] = collections.defaultdict(int)
    for pair in current_pairs:
        counting[pair[0]] += current_pairs[pair]

    max_l = max(counting, key=counting.get)
    min_l = min(counting, key=counting.get)
    max_l_val = counting[max_l]
    min_l_val = counting[min_l]
    print(f"max letter {max_l} -> {max_l_val} min letter {min_l} -> {min_l_val} result {max_l_val - min_l_val}")


if __name__ == "__main__":
    main()
