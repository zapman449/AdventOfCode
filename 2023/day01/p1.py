#!/usr/bin/env python3

import argparse


def parseargs() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("input", help="input file")
    return parser.parse_args()


def main() -> None:
    args = parseargs()
    tally = 0
    with open(args.input) as f:
        for line in f.readlines():
            digits = [d for d in line.strip() if d.isdigit()]
            try:
                x = int(digits[0]) * 10
            except ValueError:
                x = 0
            try:
                y = int(digits[-1])
            except ValueError:
                y = 0
            tally += x + y
    print(tally)


if __name__ == "__main__":
    main()
