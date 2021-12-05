#!/usr/bin/env python

import typing
import itertools


def gather() -> typing.List[int]:
    result: typing.List[int] = []
    with open('input', 'r') as i:
        for line in i:
            result.append(int(line.strip()))
    return result


def process(numbers: typing.List[int]) -> typing.List[typing.Tuple[int, int, int]]:
    return [(x, y, z) for x, y, z in itertools.combinations(numbers, 3) if x+y+z == 2020]


def main() -> None:
    numbers = gather()
    for result in process(numbers):
        product = result[0] * result[1] * result[2]
        print(f"found trio: {result[0]} + {result[1]} + {result[2]} == 2020. Product is {product}")


if __name__ == "__main__":
    main()
