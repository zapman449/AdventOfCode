#!/usr/bin/env python3

import fileinput
import typing


def parse(entry: str) -> int:
    row_str = entry[:7]
    seat_str = entry[7:]
    row_b_str = "0b" + row_str.replace("F", "0").replace("B", "1")
    seat_b_str = "0b" + seat_str.replace("L", "0").replace("R", "1")
    # print(f"DEBUG: entry is {entry}")
    # print(f"DEBUG: row_str   is   {row_str} seat_str   is   {seat_str}")
    # print(f"DEBUG: row_b_str is {row_b_str} seat_b_str is {seat_b_str}")
    return int(row_b_str, 2) * 8 + int(seat_b_str, 2)


def parse2(entry: str) -> int:
    """create int from faux binary string"""
    return int('0b' + entry.replace("F", "0").replace("B", "1").replace("L", "0").replace("R", "1"), 2)


def main() -> None:
    seat_ids = [parse2(line.strip()) for line in fileinput.input()]
    seat_ids.sort()
    print([seat_id - 1 for idx, seat_id in enumerate(seat_ids) if seat_ids[idx] - seat_ids[idx-1] == 2])


if __name__ == "__main__":
    main()
