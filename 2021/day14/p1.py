#!/usr/bin/env python3

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
    pairs: typing.Dict[str, str] = {}
    for line in fileinput.input():
        if base is None:
            base = line.strip()
            continue
        if len(line.strip()) == 0:
            continue
        words = line.strip().split(" -> ")
        lhs = words[0]
        rhs = lhs[0] + words[1] + lhs[1]      # three letter
        # rhs = words[1]                          # single letter
        pairs[lhs] = rhs
    # print(f"start base      {base}")
    for step in range(10):
        new_base = ""
        for idx in range(len(base)):
            try:
                key = base[idx] + base[idx+1]
            except IndexError:
                continue
            val = pairs[key]
            if len(new_base) == 0:
                new_base = val
            else:
                new_base += val[1:]
        base = new_base
        # if step < 4:
        #     print(f"step {step} new base {base}")

    counting: typing.Dict[str, int] = collections.defaultdict(int)
    for l in base:
        counting[l] += 1
    max_l = max(counting, key=counting.get)
    min_l = min(counting, key=counting.get)
    max_l_val = counting[max_l]
    min_l_val = counting[min_l]
    print(f"max letter {max_l} -> {max_l_val} min letter {min_l} -> {min_l_val} result {max_l_val - min_l_val}")


if __name__ == "__main__":
    main()
