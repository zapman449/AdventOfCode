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


def recurse(search_bag: str, current_bag: str,
            rules: typing.Dict[str, typing.Dict[str, int]],
            cache: typing.Set[str]) -> bool:
    if current_bag not in rules:
        return False
    elif search_bag in rules[current_bag]:
        cache.add(current_bag)
        return True
    for inner_bag in rules[current_bag]:
        if recurse(search_bag, inner_bag, rules, cache):
            cache.add(current_bag)
            return True
    return False


def traverse(search_bag: str, rules: typing.Dict[str, typing.Dict[str, int]]) -> int:
    cache: typing.Set[str] = set()
    # pprint.pprint(rules)
    for outer_bag in rules:
        recurse(search_bag, outer_bag, rules, cache)
    return len(cache)


def main() -> None:
    rules = gather()
    print(traverse("shiny gold", rules))


if __name__ == "__main__":
    main()
