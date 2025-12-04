#!/usr/bin/env python3

# import collections
import fileinput
import functools
import itertools
import sys
import typing


def p2_find_max(bank:str, start:int, end:int) -> typing.Tuple[str, int]:
    # I don't love the double iteration here...  could fix with enumerate()...
    found_max: str = max(bank[start:end])
    index: int = bank[start:end].find(found_max)
    return found_max, start+index+1


def p2_parse_bank(bank: str, battery_count: int) -> int:
    maxen: typing.List[str] = [""] * battery_count
    index = 0
    for i in range(0, battery_count):
        m, index_tmp = p2_find_max(bank, index, len(bank)-(battery_count-i-1))
        # print(f"for {i=} called p2_find_max({bank}, {index}, {len(bank)-(battery_count-i-1)}) -- got {m}, {index_tmp}")
        index = index_tmp
        maxen[i] = m
    return int("".join(maxen))


def run_tests():
    success = True
    inouts = {
        "987654321111111": (98, 987654321111),
        "811111111111119": (89, 811111111119),
        "234234234234278": (78, 434234234278),
    }
    for given, want in inouts.items():
        want_p1, want_p2 = want
        got = p2_parse_bank(given, 2)
        if got != want_p1:
            print(f"{given} want {want_p1}, got {got} ")
            success = False
        got = p2_parse_bank(given, 12)
        if got != want_p2:
            print(f"{given} want {want_p2}, got {got} ")
            success = False
    if not success:
        sys.exit(1)


def main() -> None:
    run_tests()
    ls = []
    for line in fileinput.input():
        ls.append(line.strip())

    p1_tally = sum(map(functools.partial(p2_parse_bank, battery_count=2), ls))
    p2_tally = sum(map(functools.partial(p2_parse_bank, battery_count=12), ls))

    print(f"final {p1_tally=}")
    print(f"final {p2_tally=}")

if __name__ == "__main__":
    main()
