#!/usr/bin/env python3

import argparse
import collections
import itertools
import pprint
import sys
import typing


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("input", help="input file")
    return parser.parse_args()


def get_input(in_file: str) -> typing.List[str]:
    with open(in_file) as f:
        return f.read().splitlines()


def run_tests() -> None:
    pass


class NodeVectors(typing.NamedTuple):
    left: str
    right: str


def p1(nodes: typing.Dict[str, NodeVectors], left_or_right: str) -> None:
    steps = 0
    node = "AAA"
    while True:
        if node == "ZZZ":
            break
        d = left_or_right[steps % len(left_or_right)]
        steps += 1
        if d == "L":
            node = nodes[node].left
        else:
            node = nodes[node].right
    print(f"p1 solution: {steps}")


def main() -> None:
    args = parse_args()
    data = get_input(args.input)
    run_tests()
    left_or_right: str = data[0]
    nodes: typing.Dict[str, NodeVectors] = {}
    for path in data[2:]:
        key = path[0:3]
        left = path[7:10]
        right = path[12:15]
        nodes[key] = NodeVectors(left, right)
    p1(nodes, left_or_right)


if __name__ == "__main__":
    main()
