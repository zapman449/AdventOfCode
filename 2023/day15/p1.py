#!/usr/bin/env python3

import argparse
import collections
import copy
import itertools
import hashlib
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


def parse_step(step: str) -> int:
    tally = 0
    for c in step:
        tally = ((tally + ord(c)) * 17) % 256
    # print(f"step {step} -> {tally}")
    return tally


def main() -> None:
    args = parse_args()
    data = get_input(args.input)
    p1 = sum([parse_step(step) for step in data[0].split(",")])
    print(f"part 1: {p1}")
    boxes: typing.Dict[int, typing.Dict[str, int]] = {n: collections.OrderedDict() for n in range(256)}
    for cmd in data[0].split(","):
        if cmd[-1] == "-":
            oper = cmd[-1]
            slot = None
            lbl = cmd[:-1]
        elif cmd[-2] == "=":
            oper = cmd[-2]
            slot = int(cmd[-1])
            lbl = cmd[:-2]
        else:
            sys.exit(f"failed to parse {cmd}")
        hs = parse_step(lbl)
        # print(f"{lbl} -> {hs} {oper} {slot}")
        if oper == "-":
            try:
                del boxes[hs][lbl]
            except KeyError:
                continue
        elif oper == "=":
            boxes[hs][lbl] = slot

    tally = 0
    for box, lenses in boxes.items():
        lens_counter = 1
        for lbl, slot in lenses.items():
            tally += (box+1) * lens_counter * slot
            lens_counter += 1
    print(f"part 2: {tally}")


if __name__ == "__main__":
    main()
