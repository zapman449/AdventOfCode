#!/usr/bin/env python3

"""

"""

import collections
import copy
import fileinput
import functools
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


def traverse_broken(trimmed: typing.List[Datum]) -> int:
    multiple = trimmed[0].value
    current_departure_max = multiple
    true_departure_offset = min([d.idx_offset_from_max for d in trimmed])
    while True:
        valid = True
        for d in trimmed[1:]:
            if (current_departure_max + d.idx_offset_from_max) % d.value != 0:
                valid = False
                break
        if valid:
            return current_departure_max + true_departure_offset
        current_departure_max = current_departure_max + multiple


def traverse3(data: typing.List[Datum], start=0) -> int:
    if start <= data[0].value:
        current = data[0].value
    else:
        current = ((start // data[0].value) + 1) * data[0].value
    base = data[0].value
    itercount = 0
    while True:
        itercount += 1
        if itercount % 100000 == 0:
            print(f"DEBUG: start is {start} current is {current}, itercount is {itercount}, base is {base}")
        valid = True
        for d in data[1:]:
            if (current + d.idx_offset_from_max) % d.value != 0:
                valid = False
        if valid:
            print("Success!")
            return current - data[0].original_idx
        current += base


def traverse_naive(data: typing.List[int], start=0) -> int:
    while True:
        valid = True
        # if start % 10000 == 0:
        #     print(f"DEBUG: start is {start}")
        # print(f"DEBUG: data is {repr(data)}")
        for idx, bus in enumerate(data):
            # print(f"DEBUG: idx {idx} bus {bus} start {start} start+idx {start+idx} (start+idx)%bus {(start+idx)%bus}")
            if bus == 1:
                continue
            elif (start + idx) % bus != 0:
                valid = False
                break
        if valid:
            return start
        start += 1


def main() -> None:
    print(1)
    start_time, data = gather()
    print(2)
    trimmed = trim_input(data)
    print(3)
    print(repr(trimmed))
    # departure = traverse(trimmed)
    # departure = traverse_naive(data, start=0)
    # departure = traverse3(trimmed, start=100000000000000)
    # print(f"departure is {departure}")


def test1():
    print(f"traverse {traverse_naive([7,13,1,1,59,1,31,19])} should be 1068781")
    print(f"traverse {traverse_naive([17,1,13,19])} should be 3417")
    print(f"traverse {traverse_naive([67,7,59,61])} should be 754018")
    print(f"traverse {traverse_naive([67,1,7,59,61])} should be 779210")
    print(f"traverse {traverse_naive([67,7,1,59,61])} should be 1261476")
    print(f"traverse {traverse_naive([1789,37,47,1889])} should be 1202161486")


def test2():
    print(f"traverse {traverse3(trim_input([7,13,1,1,59,1,31,19]))} should be 1068781")
    print(f"traverse {traverse3(trim_input([17,1,13,19]))} should be 3417")
    print(f"traverse {traverse3(trim_input([67,7,59,61]))} should be 754018")
    print(f"traverse {traverse3(trim_input([67,1,7,59,61]))} should be 779210")
    print(f"traverse {traverse3(trim_input([67,7,1,59,61]))} should be 1261476")
    print(f"traverse {traverse3(trim_input([1789,37,47,1889]))} should be 1202161486")


if __name__ == "__main__":
    # test2()
    main()
