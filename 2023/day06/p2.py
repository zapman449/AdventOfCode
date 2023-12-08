#!/usr/bin/env python3

import argparse
import collections
import itertools
import pprint
import typing


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("input", help="input file")
    return parser.parse_args()


def get_input(in_file: str) -> typing.List[str]:
    with open(in_file) as f:
        return f.read().splitlines()


def main() -> None:
    args = parse_args()
    data = get_input(args.input)

    data2 = [data[0].replace(" ", "").split(":"),
             data[1].replace(" ", "").split(":")]
    p1_product = 1
    for idx in range(1, len(data2[0])):
        tally = 0
        t = int(data2[0][idx])
        best_distance = int(data2[1][idx])
        for ms in range(1, t):
            mx = t - ms
            d = mx * ms
            if d > best_distance:
                # print(f"t: {t}, ms: {ms} mx {mx} d: {d} best: {best_distance}")
                tally += 1
        p1_product *= tally

    print(f"Solution: Part 1: {p1_product}")


if __name__ == "__main__":
    main()
