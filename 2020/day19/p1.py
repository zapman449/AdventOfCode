#!/usr/bin/env python3

"""

"""

import collections
import copy
import fileinput
import pprint
import re
import typing
import sys


def gather() -> typing.Tuple[typing.Dict[str, typing.Dict], typing.List[str]]:
    state = 0
    rules: typing.Dict[str, typing.Dict] = {}
    qstrings: typing.List[str] = []
    for line in fileinput.input():
        if line == "\n":
            state += 1
        elif state == 0:
            words1 = line.strip().split(": ")
            idx = words1[0]
            if '"' in words1[1]:
                rules[idx] = {'type': 'letter', 'value': words1[1][1], 'valid_regex': words1[1][1]}
            elif "|" in words1[1]:
                words2 = words1[1].split(" | ")
                words3 = words2[0].split()
                words4 = words2[1].split()
                rules[idx] = {'type': 'list_or_list', 'value': [words3, words4]}
            else:
                words2 = words1[1].split()
                rules[idx] = {'type': 'list', 'value': words2}
        elif state == 1:
            qstrings.append(line.strip())
    return rules, qstrings


def build_regex(rules: typing.Dict[str, typing.Dict], idx: str) -> str:
    rule = rules[idx]
    if rule['type'] == 'letter':
        return rule['valid_regex']
    elif rule['type'] == 'list':
        if 'valid_regex' in rule:
            return rule['valid_regex']
        regex = ""
        for sub_idx in rule['value']:
            regex += build_regex(rules, sub_idx)
        rule['valid_regex'] = regex
        return rule['valid_regex']
    elif rule['type'] == 'list_or_list':
        first = True
        regex = ""
        for sub_list in rule['value']:
            sub_regex = ""
            for sub_idx in sub_list:
                sub_regex += build_regex(rules, sub_idx)
            if first:
                first = False
                regex = "(" + sub_regex
            else:
                regex = regex + "|" + sub_regex
        regex += ")"
        rule['valid_regex'] = regex
        return rule['valid_regex']
    else:
        print("should not get here")


def main() -> None:
    rules, qstrings = gather()
    # pprint.pprint(rules)
    regex = build_regex(rules, "0")
    final_regex = "^" + regex + "$"
    print(f"regex is {final_regex}")
    rec = re.compile(final_regex)
    print(f"result: {sum([1 for candidate in qstrings if re.match(rec, candidate)])}")


if __name__ == "__main__":
    main()
