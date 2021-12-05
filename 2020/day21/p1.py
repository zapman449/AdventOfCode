#!/usr/bin/env python3

"""

"""

import collections
import copy
import fileinput
import pprint
import typing
import sys


def gather() -> typing.Dict[str, str]:
    cache = {}
    final: typing.Dict[str, typing.Set[str]] = {}
    allergen_free = set()
    for line in fileinput.input():
        pline = line.strip().replace("(", "").replace(")", "").replace(",", "").split()
        state = 0
        ingredients = []
        allergens = set()
        for word in pline.split():
            if word == "contains":
                state += 1
            elif state == 0:
                ingredients.append(word)
            else:
                allergens.add(word)
        for word in ingredients:
            if word in cache:
                if allergens.isdisjoint(cache[word]):
                    allergen_free.add(word)
                else:
                    final[word] = allergens.union(cache[word])
            else:


def main() -> None:
    eqn_list = gather()
    print(f"result is {sum([solve(eqn) for eqn in eqn_list])}")


if __name__ == "__main__":
    main()
