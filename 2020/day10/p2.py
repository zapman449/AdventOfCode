#!/usr/bin/env python3

"""
❯ ./p2.py input.short1
final result: 8
❯ ./p2.py input.short2
final result: 19208
❯ ./p2.py input.long
final result: 24803586664192
"""

import fileinput
import functools
import itertools
import typing


def gather() -> typing.List[int]:
    result = [int(line) for line in fileinput.input()]
    result.append(0)  # wall socket
    result.sort()
    result.append(result[-1] + 3)  # computer adapter
    return result


def traverse(data: typing.List[int], jumps=(1, 2, 3)) -> int:
    result = [0, ] * len(data)
    result[0] = 1
    print(repr(data))
    for idx, datum in enumerate(data):
        sub_idx = idx+1
        while True:
            if sub_idx >= len(data):
                break
            elif data[sub_idx] - datum > max(jumps):
                break
            result[sub_idx] += result[idx]
            sub_idx += 1
    return result[-1]


# def valid_path_q(sublist: typing.List[int], computer_joltage: int, jumps: typing.Tuple[int, int, int]) -> bool:
#     constrained_list = [0] + sublist + [computer_joltage]
#     first = True
#     for idx, datum in enumerate(constrained_list):
#         # print(f"datum {datum}, constrained_list[idx-1] is {constrained_list[idx - 1]}, jumps is {repr(jumps)}")
#         if first:
#             first = False
#             continue
#         elif datum - constrained_list[idx-1] not in jumps:
#             return False
#     return True
#
#
# def traverse(data: typing.List[int], jumps=(1, 2, 3)) -> int:
#     computer_joltage = data[-1] + 3
#     min_combination_len = int(len(data) / max(jumps))
#     result = 0
#     for combo_len in range(min_combination_len, len(data)):
#         print(f"DEBUG: combo_len is {combo_len}")
#         for path in itertools.combinations(data, combo_len):
#             if valid_path_q(list(path), computer_joltage, jumps):
#                 print(f"Debug: valid path is {path}")
#                 result += 1
#     return result


# def traverse(data: typing.List[int], jumps=(1, 2, 3)) -> typing.List[int]:
#     result = [0, ] * len(data)
#     top_idx = len(data)
#     print(f"DEBUG: data {repr(data)}")
#     for idx, datum in enumerate(data):
#         max_index = min((top_idx, idx + len(jumps) + 1))
#         if idx == max_index:
#             continue
#         sublist = data[idx+1:max_index]
#         print(f"DEBUG: idx {idx} datum {datum} sublist {repr(sublist)}")
#         possible_jumps = [1 for entry in sublist if entry-datum in jumps]
#         sum_possible = sum(possible_jumps)
#         result[idx] = sum_possible
#         # result[idx] = sum([1 for entry in sublist if entry in jumps])
#         print(f"DEBUG: idx {idx}, possible_jumps {repr(possible_jumps)} sum_possible {sum_possible} result {repr(result)}")
#     result[-1] = 1
#     return result


def main() -> None:
    data = gather()
    result = traverse(data)
    # product = functools.reduce(lambda a, b: a*b, result)
    print(f"final result: {result}")


if __name__ == "__main__":
    main()
