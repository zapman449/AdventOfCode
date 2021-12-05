#!/usr/bin/env python3

"""

"""

import collections
import copy
import fileinput
import typing
import sys


# valu 101010101
# mask 111110000
#   or 111110101

# valu 101010101
# mask 111110000
#  and 101010101


def parse(bstr: str, mask: str) -> int:
    result = []
    for v, m in zip(bstr, mask):
        if m == "0":
            result.append("0")
        elif m == "1":
            result.append("1")
        else:
            result.append(v)
    tally = "".join(result)
    # print(f"DEBUG: bstr  {bstr}")
    # print(f"DEBUG: mask  {mask}")
    # print(f"DEBUG: tally {tally}")
    # print(f"DEBUG: final {int(tally, 2)}")
    return int(tally, 2)


def main() -> None:
    mask = ""
    addr = 0
    value = ""
    memory = collections.defaultdict(int)
    for line in fileinput.input():
        words = line.strip().split(" = ")
        if words[0] == "mask":
            mask = words[1]
        else:
            addr = words[0][4:-1]
            value = bin(int(words[1]))[2:]
            prefix = "0" * (36 - len(value))
            value = prefix + value
            memory[addr] = parse(value, mask)
    # print(f"memory: {memory}")
    print(f"result: {sum(memory.values())}")


if __name__ == "__main__":
    main()
