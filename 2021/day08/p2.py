#!/usr/bin/env python3

import collections
import fileinput
import pprint
import statistics
import sys
import typing

# top : 023456789
# middle : 2345689
# lower horizontal: 023568
# upper left vertical: 045689
# upper right vertical: 01234789
# lower left vertical: 0268
# lower right vertical: 012346789

# zero:  len(6): top, bottom, upper right, upper left, lower right, lower left
# one:   len(2): upper right, upper left
# two:   len(5): top, middle, bottom, upper right, lower left
# three: len(5): top, middle, bottom, upper right, upper left
# four:  len(4): top, middle, upper left, upper right, lower right
# five:  len(5): top, middle, bottom, upper left, lower right
# six:   len(6): top, middle, bottom, upper left, lower left, lower right
# seven: len(3): top, upper left, lower left
# eight: len(7): all
# nine:  len(6): top, middle, upper left, upper right, lower right

# len(2) -> 1
# len(3) -> 7
# len(4) -> 4
# len(5) -> 2, 3, 5
# len(6) -> 0, 6, 9
# len(7) -> 8


def letter_sort(words: typing.List[str]) -> typing.List[str]:
    out: typing.List[str] = []
    for word in words:
        out.append("".join(sorted(list(word))))
    return out


def solver(puzzle_in_sorted, puzzle_out_sorted) -> typing.Dict[str, str]:
    answers: typing.Dict[str, str] = {}
    reverse_answers: typing.Dict[str, str] = {}
    partial_answers: typing.Dict[str, typing.Set[str]] = {}
    for key in ('a', 'b', 'c', 'd', 'e', 'f', 'g'):
        partial_answers[key] = {'top', 'middle', 'bottom', 'UL', 'UR', 'LL', 'LR'}
    for entry in puzzle_in_sorted:
        if len(entry) == 2:
            answers[entry] = "1"
            reverse_answers["1"] = entry
            for letter in entry:
                partial_answers[letter] = partial_answers[letter] & {'UR', 'LR'}
        elif len(entry) == 3:
            answers[entry] = "7"
            reverse_answers["7"] = entry
            for letter in entry:
                partial_answers[letter] = partial_answers[letter] & {'top', 'UR', 'LR'}
        elif len(entry) == 4:
            answers[entry] = "4"
            reverse_answers["4"] = entry
            for letter in entry:
                partial_answers[letter] = partial_answers[letter] & {'middle', 'UL', 'UR', 'LR'}
        elif len(entry) in (5, 6):
            # 2, 3, 5 vs 6, 9
            pass
        elif len(entry) == 7:
            answers[entry] = "8"
            reverse_answers["8"] = entry

    for entry in puzzle_in_sorted:
        if entry in answers:
            continue
        if len(entry) == 6:
            # 6 or 9 or 0
            four_set = set(reverse_answers["4"])
            one_set = set(reverse_answers["1"])
            if set(entry).issuperset(four_set):
                answers[entry] = "9"
                reverse_answers["9"] = entry
                extra_letter_set = set(entry) - four_set
                extra = extra_letter_set.pop()
                partial_answers[extra] = {'top'}
                for letter in partial_answers:
                    if letter in entry:
                        partial_answers[letter].discard('LL')
                    else:
                        partial_answers[letter] = {'LL'}
            elif set(entry).issuperset(one_set):
                answers[entry] = "0"
                reverse_answers["0"] = entry
                for letter in partial_answers:
                    if letter not in entry:
                        partial_answers[letter] = {'middle'}
            else:
                answers[entry] = "6"
                reverse_answers["6"] = entry
                for letter in partial_answers:
                    if letter in entry:
                        partial_answers[letter].discard('UR')
                    else:
                        partial_answers[letter] = {'UR'}

    for entry in puzzle_in_sorted:
        if entry in answers:
            continue
        # 2, 3 or 5
        one_set = set(reverse_answers["1"])
        if set(entry).issuperset(one_set):
            answers[entry] = "3"
            for letter in entry:
                partial_answers[letter].discard('UL')
                partial_answers[letter].discard('LL')

    for entry in puzzle_in_sorted:
        if entry in answers:
            continue
        # 2 or 5
        meta_partial = set()
        for letter in entry:
            for diode in partial_answers[letter]:
                meta_partial.add(diode)
        if 'UL' in meta_partial and 'LR' in meta_partial:
            answers[entry] = "5"
            reverse_answers['5'] = entry
        else:
            answers[entry] = "2"
            reverse_answers['2'] = entry

    # print(f"after filter4 partial answers are:")
    # pprint.pprint(partial_answers)
    # print()
    # print(f"after filter4 answers are:")
    # pprint.pprint(answers)
    # print()
    # print(f"{repr(puzzle_in_sorted)} | {repr(puzzle_out_sorted)}")
    try:
        digits = "".join([answers[x] for x in puzzle_out_sorted])
        print(f"out {puzzle_out_sorted} {digits}")
    except KeyError:
        print("will fail")
        sys.exit(0)
    return answers


def main() -> None:
    tally = 0
    for line in fileinput.input():
        x = line.strip().split(" | ")
        puzzle_in = x[0].split()
        puzzle_out = x[1].split()
        puzzle_in_sorted = letter_sort(puzzle_in)
        puzzle_out_sorted = letter_sort(puzzle_out)
        line_answers = solver(puzzle_in_sorted, puzzle_out_sorted)
        digits = []
        for digit in puzzle_out_sorted:
            digits.append(line_answers[digit])
        line_number = int("".join(digits))
        tally += line_number
        # print(f"line answer is {line_number} current tally is {tally}")
    print(f"final tally is {tally}")


if __name__ == "__main__":
    main()
