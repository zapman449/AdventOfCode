#!/usr/bin/env python3

"""

"""

import collections
import copy
import fileinput
import pprint
import re
import typing
import sys


def permute(input: typing.List[int], idx: int) -> int:
    idx_value = input[idx]
    low_slice = idx + 1
    high_slice = idx + 4
    sub_input: typing.List[int]
    if low_slice < len(input) and high_slice < len(input):
        sub_input = input[low_slice:high_slice]
    elif low_slice < len(input) <= high_slice:
        sub_input = input[low_slice:] + input[:high_slice%len(input)]
    else:
        sub_input = input[low_slice%len(input):high_slice%len(input)]
    print(f"input {input}, idx {idx} idx_value {idx_value} sub_input {sub_input}")


def main() -> None:
    input = [int(x) for x in list("389125467")]
    # input = [int(x) for x in list("156794823")]
    turns = 10
    # turns = 100
    idx = 0
    for x in range(turns):
        idx = permute(input, idx)
        print("".join(str(x) for x in input))


if __name__ == "__main__":
    main()
