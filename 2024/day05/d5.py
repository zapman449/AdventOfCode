#!/usr/bin/env python3

import collections
import fileinput
import functools
import typing

def parse_input():
    state = 0
    must_before: typing.Dict[int, typing.List[int]] = collections.defaultdict(list)
    must_after: typing.Dict[int, typing.List[int]] = collections.defaultdict(list)
    print_orders: typing.List[typing.List[int]] = []
    for line in fileinput.input():
        if line.strip() == "":
            state += 1
        elif state == 0:
            first, second = map(int, line.strip().split("|"))
            must_before[first].append(second)
            must_after[second].append(first)
        elif state == 1:
            print_orders.append(list(map(int, line.strip().split(","))))

    return must_before, must_after, print_orders


def test_print_order(must_before, must_after, print_order):
    for idx, page in enumerate(print_order):
        for later_page in print_order[idx + 1:]:
            if later_page in must_after[page]:
                return False
        for earlier_page in print_order[:idx]:
            if earlier_page in must_before[page]:
                return False
    return True


def sort_po(po, must_before) -> typing.List[int]:
    return sorted(po, key=functools.cmp_to_key(lambda x, y: 1 if y in must_before[x] else -1 if x in must_before[y] else 0))


def main() -> None:
    p1_tally = 0
    p2_tally = 0
    must_before, must_after, print_orders = parse_input()
    for po in print_orders:
        if test_print_order(must_before, must_after, po):
            l = len(po) // 2
            p1_tally += po[l]
        else:
            new_po = sort_po(po, must_before)
            l = len(new_po) // 2
            p2_tally += new_po[l]
    print(f"{p1_tally=}")
    print(f"{p2_tally=}")

if __name__ == "__main__":
    main()
