#!/usr/bin/env python3

"""

"""

import collections
import copy
import fileinput
import pprint
import typing
import sys


def ticket_valid_q(ticket: typing.List[int], all_valid_numbers: typing.Set[int]) -> typing.Tuple[bool, int]:
    tally = 0
    result = True
    # print(f"DEBUG: in ticket_valid_q ticket is {ticket}")
    # print(f"DEBUG: in ticket_valid_q all_valid_numbers is {all_valid_numbers}")
    for value in ticket:
        if value not in all_valid_numbers:
            result = False
            tally += value
    # print(f"DEBUG: in ticket_valid_q returning {result} & {tally}")
    return result, tally


def gather() -> typing.Tuple[typing.Dict[str, typing.Set[int]],
                             typing.List[int],
                             typing.List[typing.List[int]],
                             int]:
    all_valid_numbers: typing.Set[int] = set()
    constraints: typing.Dict[str, typing.Set[int]] = {}
    your_ticket: typing.List[int] = []
    nearby_valid_tickets: typing.List[typing.List[int]] = []
    error_rate = 0
    stage = 1
    for line in fileinput.input():
        if line == "\n":
            continue
        elif line in ("your ticket:\n", "nearby tickets:\n"):
            stage += 1
            continue
        elif stage == 1:
            fields = line.strip().split(": ")
            int_ranges = fields[1].split(" or ")
            constr = fields[0]
            for int_range in int_ranges:
                x, y = int_range.split("-")
                constraints[constr] = {z for z in range(int(x), int(y)+1)}
                all_valid_numbers.update(constraints[constr])
        elif stage == 2:
            your_ticket = [int(i) for i in line.strip().split(',')]
        elif stage == 3:
            ticket = [int(i) for i in line.strip().split(',')]
            valid, sub_tally = ticket_valid_q(ticket, all_valid_numbers)
            if valid:
                nearby_valid_tickets.append(ticket)
            else:
                error_rate += sub_tally

    return constraints, your_ticket, nearby_valid_tickets, error_rate


def main() -> None:
    constraints, your_ticket, nearby_valid_tickets, error_rate = gather()
    # print("constraints:")
    # pprint.pprint(constraints)
    print(f"error rate is {error_rate}")


if __name__ == "__main__":
    main()
