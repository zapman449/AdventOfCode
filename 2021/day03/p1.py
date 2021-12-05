#!/usr/bin/env python3

import fileinput
import pprint
import sys
import typing


def flip(d):
    if d == "1":
        return "0"
    elif d == "0":
        return "1"
    else:
        print(f"wat. d is {d}")
        sys.exit()


def main() -> None:
    data = [digits.strip() for digits in fileinput.input()]
    # pprint.pprint(data)
    transposed = list(map(list, zip(*data)))
    # pprint.pprint(transposed)
    sums = [sum(map(int, l)) for l in transposed]
    half_len_data = len(data) / 2
    most_common = []
    for s in sums:
        if s > half_len_data:
            most_common.append('1')
        else:
            most_common.append('0')
    binary = ''.join(most_common)
    inverse = ''.join([flip(d) for d in most_common])
    gamma = int(binary, 2)
    epsilon = int(inverse, 2)

    print(f"gamma: {binary} epsilon: {inverse} product: {gamma*epsilon}")


if __name__ == "__main__":
    main()
