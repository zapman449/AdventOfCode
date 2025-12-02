#!/usr/bin/env python3

# import collections
import fileinput
# import functools
import sys
# import typing


def p1_parse_num(num: int) -> bool:
    num_str = str(num)
    l = len(num_str)
    # print(f"{num=} {l=}")
    h1 = num_str[0:l//2]
    h2 = num_str[l//2:]
    return h1 == h2


def p2_parse_num(num: int) -> bool:
    num_str = str(num)
    for i in range(0, len(num_str)//2):
        partial = num_str[0:i+1]
        for j in range(1,15):
            test = partial*j
            # print(f"{num=}, i={i+1}, {partial=}, {test=}")
            if test == num_str:
                return True
            if test not in num_str:
                break
    return False


def run_tests():
    success = True
    valids = (11, 22, 99, 111, 999, 1010)
    for n in valids:
        if not p2_parse_num(n):
            print(f"{n} should be true")
            success = False
    if not success:
        sys.exit(1)


def main() -> None:
    run_tests()
    ls = []
    for line in fileinput.input():
        ls = line.strip().split(",")
        break

    p1_tally = 0
    p2_tally = 0
    for se in ls:
        start_str, end_str = se.split("-")
        start_int = int(start_str)
        end_int = int(end_str)
        found = []
        for num in range(start_int, end_int+1):
            if p1_parse_num(num):
                p1_tally += num
            if p2_parse_num(num):
                p2_tally += num
                found.append(num)
        # print(f"{se} -> {found}")

    print(f"final {p1_tally=}")
    print(f"final {p2_tally=}")

if __name__ == "__main__":
    main()
