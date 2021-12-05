#!/usr/bin/env python3

"""

"""

import collections
import copy
import fileinput
import math
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
                constraints.setdefault(constr, set()).update({z for z in range(int(x), int(y)+1)})
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


def field_finder(constraints: typing.Dict[str, typing.Set[int]], nearby_valid_tickets: typing.List[typing.List[int]]):
    possible_len = len(nearby_valid_tickets[0])
    result: typing.Dict[str, typing.Set[int]] = {}
    for key in constraints:
        result[key] = set()
        for x in range(possible_len):
            result[key].add(x)
    # print("Constraints:")
    # pprint.pprint(constraints)
    # print("Tickets:")
    # pprint.pprint(nearby_valid_tickets)
    # print("Results:")
    # pprint.pprint(result)
    for ticket in nearby_valid_tickets:
        for idx, value in enumerate(ticket):
            for constr in result:
                if idx in result[constr]:
                    # print(f"idx {idx} value {value} constr {constr} result[constr] {result[constr]} constraints[constr] {constraints[constr]}")
                    if value not in constraints[constr]:
                        # print(f"removing idx {idx} from result[{constr}] {result[constr]}")
                        result[constr].remove(idx)
            # print("New Results:")
            # pprint.pprint(result)
    # print("result after stage 1")
    # pprint.pprint(result)
    done = set()
    for x in range(len(result)):
        for constr in result:
            if len(result[constr]) == 1 and constr not in done:
                done.add(constr)
                to_remove = result[constr].pop()
                result[constr].add(to_remove)
                for candidate in result:
                    if candidate == constr:
                        continue
                    if to_remove in result[candidate]:
                        result[candidate].remove(to_remove)
    # print("result after stage 2")
    # pprint.pprint(result)
    print(result)
    final = {}
    for key in result.keys():
        # print(f"result for key {key} is {result[key]}")
        final[key] = result[key].pop()
    return final


def main() -> None:
    constraints, your_ticket, nearby_valid_tickets, error_rate = gather()
    str_idx_dict = field_finder(constraints, nearby_valid_tickets)
    # print(f"error rate is {error_rate}")
    # p = math.prod([v for k, v in str_idx_dict if k.startswith("departure")])
    track = []
    for key in str_idx_dict:
        if key.startswith("departure"):
            idx = str_idx_dict[key]
            track.append(your_ticket[idx])
    print(f"result: {track} gives {math.prod(track)}")


if __name__ == "__main__":
    main()
