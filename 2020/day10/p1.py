#!/usr/bin/env python3

import collections
import fileinput
import typing


def gather() -> typing.List[int]:
    result = [int(line) for line in fileinput.input()]
    result.sort()
    return result


def traverse(data: typing.List[int], start_joltage=0, final_joltage_delta=3, jumps=(1, 2, 3)) -> typing.Dict[int, int]:
    result = collections.defaultdict(int)
    first = True
    for idx, datum in enumerate(data):
        if first:
            first = False
            continue
        jump_delta = datum - data[idx-1]
        for jump in jumps:
            if jump_delta == jump:
                result[jump] += 1
    result[data[0] - start_joltage] += 1
    result[final_joltage_delta] += 1
    return result


def main() -> None:
    data = gather()
    result = traverse(data)
    print(result)
    print(f"final product: {result[1] * result[3]}")


if __name__ == "__main__":
    main()