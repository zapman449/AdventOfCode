#!/usr/bin/env python3

"""
❯ ./p2help.py input.long
primes holds: [601, 577, 41, 37, 29, 23, 19, 17, 13]
remainders holds: [541, 548, 22, -60, 29, -29, -29, -26, -29]
780601154795940
"""

import collections
import copy
import fileinput
import functools
import math
import typing
import sys


class Datum(typing.NamedTuple):
    value: int
    idx_offset_from_max: int
    original_idx: int


def gather() -> typing.Tuple[int, typing.List[int]]:
    first = True
    start_time = 0
    unprocessed = ""
    for line in fileinput.input():
        if first:
            first = False
            start_time = int(line.strip())
        else:
            unprocessed = line.strip()
    data: typing.List[int] = []
    for entry in unprocessed.split(','):
        if entry == "x":
            data.append(1)
        else:
            data.append(int(entry))
    return start_time, data


def trim_input(data: typing.List[int]) -> typing.List[Datum]:
    dmax = max(data)
    dmax_idx = data.index(dmax)
    result: typing.List[Datum] = []
    for i, d in enumerate(data):
        if d == 1:
            continue
        result.append(Datum(d, i-dmax_idx, i))
    result.sort(key=lambda ds: ds.value, reverse=True)
    return result


# 577 29
# 41 19
# 37 97
# 29  0
# 23 52
# 19 40
# 17 43
# 13 42


def chinese_remainder(n, a):
    sum = 0
    prod = functools.reduce(lambda a, b: a*b, n)
    for n_i, a_i in zip(n, a):
        p = prod // n_i
        sum += a_i * mul_inv(p, n_i) * p
    return sum % prod


def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1: return 1
    while a > 1:
        q = a // b
        a, b = b, a%b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0: x1 += b0
    return x1


# 692754432903757
# 100000000000000

def cr_wrap(trim: typing.List[Datum]) -> int:
    primes = []
    remainders = []
    for d in trim:
        primes.append(d.value)
        remainders.append(d.value - d.original_idx)
    print(f"primes holds: {primes}")
    print(f"remainders holds: {remainders}")
    return chinese_remainder(primes, remainders)


def main() -> None:
    start_time, data = gather()
    trimmed = trim_input(data)
    # departure = traverse(trimmed)
    # departure = traverse_naive(data, start=0)
    # departure = traverse3(trimmed, start=100000000000000)
    # print(f"departure is {departure}")
    print(cr_wrap(trimmed))


def test1():
    print(f"traverse {traverse_naive([7,13,1,1,59,1,31,19])} should be 1068781")
    print(f"traverse {traverse_naive([17,1,13,19])} should be 3417")
    print(f"traverse {traverse_naive([67,7,59,61])} should be 754018")
    print(f"traverse {traverse_naive([67,1,7,59,61])} should be 779210")
    print(f"traverse {traverse_naive([67,7,1,59,61])} should be 1261476")
    print(f"traverse {traverse_naive([1789,37,47,1889])} should be 1202161486")


# 29,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,41,x,x,x,x,x,x,x,x,x,577,x,x,x,x,x,x,x,x,x,x,x,x,13,17,x,x,x,x,19,x,x,x,23,x,x,
# x,x,x,x,x,601,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,37
# [
#   Datum(value=601, idx_offset_from_max=0, original_idx=60),   601 60
#   Datum(value=577, idx_offset_from_max=-31, original_idx=29), 577 29
#   Datum(value=41, idx_offset_from_max=-41, original_idx=19),   41 19
#   Datum(value=37, idx_offset_from_max=37, original_idx=97),    37 97
#   Datum(value=29, idx_offset_from_max=-60, original_idx=0),    29  0
#   Datum(value=23, idx_offset_from_max=-8, original_idx=52),    23 52
#   Datum(value=19, idx_offset_from_max=-12, original_idx=48),   19 40
#   Datum(value=17, idx_offset_from_max=-17, original_idx=43),   17 43
#   Datum(value=13, idx_offset_from_max=-18, original_idx=42)    13 42
# ]
def test2():
    print(f"traverse {traverse3(trim_input([7,13,1,1,59,1,31,19]))} should be 1068781")
    print(f"traverse {traverse3(trim_input([17,1,13,19]))} should be 3417")
    print(f"traverse {traverse3(trim_input([67,7,59,61]))} should be 754018")
    print(f"traverse {traverse3(trim_input([67,1,7,59,61]))} should be 779210")
    print(f"traverse {traverse3(trim_input([67,7,1,59,61]))} should be 1261476")
    print(f"traverse {traverse3(trim_input([1789,37,47,1889]))} should be 1202161486")


def test3():
    print(chinese_remainder([3, 5, 7], [2, 3, 2]))


def test4():
    primes = [3, 5, 7]
    remainders = [2, 3, 2]
    print(f"primes {primes} remainders {remainders} cr: {chinese_remainder(primes, remainders)}")
    raw = [7, 13, 1, 1, 59, 1, 31, 19]
    print(f"traverse {raw} yields {cr_wrap(trim_input(raw))} should be 1068781")
    raw = [17, 1, 13, 19]
    print(f"traverse {raw} yields {cr_wrap(trim_input(raw))} should be 3417")
    raw = [67, 7, 59, 61]
    print(f"traverse {raw} yields {cr_wrap(trim_input(raw))} should be 754018")
    raw = [67, 1, 7, 59, 61]
    print(f"traverse {raw} yields {cr_wrap(trim_input(raw))} should be 779210")
    raw = [67, 7, 1, 59, 61]
    print(f"traverse {raw} yields {cr_wrap(trim_input(raw))} should be 1261476")
    raw = [1789, 37, 47, 1889]
    print(f"traverse {raw} yields {cr_wrap(trim_input(raw))} should be 1202161486")


if __name__ == "__main__":
    # test4()
    main()
