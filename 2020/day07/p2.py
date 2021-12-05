#!/usr/bin/env python

import fileinput
import typing


def chunks(lst: typing.List, n: int):
    """Yield successive n-sized chunks from lst."""
    for i in range(0, len(lst), n):
        yield lst[i:i + n]


def gather() -> typing.Dict[str, typing.Dict[str, int]]:
    rules: typing.Dict[str, typing.Dict[str, int]] = {}
    for line in fileinput.input():
        words = line.strip().split()
        outer_bag = " ".join(words[0:2])
        for inner_bag_def in chunks(words[4:], 4):
            if inner_bag_def[0] == "no":
                break
            count = int(inner_bag_def[0])
            inner_bag = " ".join(inner_bag_def[1:3])
            rules.setdefault(outer_bag, {})[inner_bag] = count
    return rules


def recurse(search_bag: str, rules: typing.Dict[str, typing.Dict[str, int]]) -> int:
    if search_bag not in rules:
        return 0
    sub_total = 0
    for inner_bag in rules[search_bag]:
        sub_result = recurse(inner_bag, rules)
        if sub_result == 0:
            sub_total += rules[search_bag][inner_bag]
        else:
            sub_total += sub_result * rules[search_bag][inner_bag] + rules[search_bag][inner_bag]
    return sub_total


def main() -> None:
    rules = gather()
    print(recurse("shiny gold", rules))


if __name__ == "__main__":
    main()
