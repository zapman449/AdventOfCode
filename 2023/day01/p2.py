#!/usr/bin/env python3

import argparse
import typing


def parseargs() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("input", help="input file")
    return parser.parse_args()


def spelled_digits(s: str) -> typing.List[int]:
    rdict: typing.Dict[str, str] = {
        "zero": "0",
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
    }
    result: typing.List[int] = []
    for idx in range(len(s)):
        if s[idx].isdigit():
            result.append(int(s[idx]))
        else:
            for k, v in rdict.items():
                t = s[idx:]
                if t.startswith(k):
                    result.append(int(v))
    return result


def main() -> None:
    args = parseargs()
    tally = 0
    with open(args.input) as f:
        for line in f.readlines():
            digits = spelled_digits(line.strip())
            try:
                x = int(digits[0]) * 10
            except:
                x = 0
            try:
                y = int(digits[-1])
            except:
                y = 0
            tally += x + y
    print(tally)


if __name__ == "__main__":
    main()
