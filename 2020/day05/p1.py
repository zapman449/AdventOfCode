#!/usr/bin/env python3

# BFFFBBFRRR: row 70, column 7, seat ID 567.
# FFFBBBFRRR: row 14, column 7, seat ID 119.
# BBFFBBFRLL: row 102, column 4, seat ID 820.

import fileinput
import typing


def gen_id(entry: typing.Tuple[int, int]) -> int:
    return entry[0] * 8 + entry[1]


def parse(entry: str) -> typing.Tuple[int, int]:
    row_str = entry[:7]
    seat_str = entry[7:]
    row_b_str = "0b" + row_str.replace("F", "0").replace("B", "1")
    seat_b_str = "0b" + seat_str.replace("L", "0").replace("R", "1")
    # print(f"DEBUG: entry is {entry}")
    # print(f"DEBUG: row_str   is   {row_str} seat_str   is   {seat_str}")
    # print(f"DEBUG: row_b_str is {row_b_str} seat_b_str is {seat_b_str}")
    return int(row_b_str, 2), int(seat_b_str, 2)


def gather() -> typing.List[typing.Tuple[int, int]]:
    result: typing.List[typing.Tuple[int, int]] = []
    for line in fileinput.input():
        uline = line.strip()
        result.append(parse(uline))
    return result


def main() -> None:
    # t = parse('BBFFBBFRLL')
    # i = gen_id(t)
    # print(f"row {t[0]}, column {t[1]}, seat ID {i}")
    entries = gather()
    ids = [gen_id(entry) for entry in entries]
    print(f"max is {max(ids)}")


if __name__ == "__main__":
    main()