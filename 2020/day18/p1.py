#!/usr/bin/env python3

"""

"""

import collections
import copy
import fileinput
import pprint
import typing
import sys


def gather() -> typing.List[str]:
    return [l.strip() for l in fileinput.input()]


def find_close(eqn: str, idx: int) -> str:
    paren_count = 0
    for sub_idx, char in enumerate(eqn[idx:]):
        true_idx = idx + sub_idx
        # print(f"char {char} true_idx {true_idx} paren_count {paren_count}")
        if char == "(":
            paren_count += 1
        elif char == ")":
            if paren_count == 0:
                return eqn[idx:true_idx]
            else:
                paren_count -= 1


def one_step(v1: int, v2: int, oper: str) -> int:
    if oper == "*":
        return int(v1) * int(v2)
    elif oper == "+":
        return int(v1) + int(v2)
    else:
        print("uh, should NOT be here")
        return 1


def solve(eqn: str, start=0) -> int:
    result = start
    next_oper = "+"
    # print(f"solve starting with eqn {eqn}")
    for idx, char in enumerate(eqn):
        if char == "(":
            sub_eqn = find_close(eqn, idx+1)
            sub_eqn_result = solve(sub_eqn)
            partial_result = one_step(result, sub_eqn_result, next_oper)
            close_paren_idx = idx + len(sub_eqn) + 1
            # print(f"solve paren sub_eqn {sub_eqn}, sub_eqn_result {sub_eqn_result}, partial_result {partial_result} close_idx {close_paren_idx}")
            return solve(eqn[close_paren_idx:], partial_result)
        elif char == "+" or char == "*":
            next_oper = char
        elif char == " " or char == ")":
            continue
        else:
            result = one_step(result, char, next_oper)

    return result


def main() -> None:
    eqn_list = gather()
    print(f"result is {sum([solve(eqn) for eqn in eqn_list])}")


if __name__ == "__main__":
    main()
