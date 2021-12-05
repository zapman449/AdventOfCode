#!/usr/bin/env python3

"""
part 1: do it like day 1. queue for previous m elements, hashmap (k = element in previous m,
v = how many times it appears in previous m). O(n) times * (O(1) update of both, then O(m),
to check each element in the queue for whether its pair exists in the hashmap)

part 2: compute cumulative sum table in O(n) time, where each element CS[i] is sum of elements
strictly to the left of input[i]. sliding window over CS, track sum externally. expand window
to the right by 1 element if sum is too small (add the new element to the tracked sum), shrink
window from the left by 1 element if sum is too large (subtract the just-removed element from
the tracked sum). both of the aforementioned take O(1) time and will be done no more than O(n)
times each. when sum matches target, left and right window boundary correspond exactly to the
window in the original input that sum to the target (edited)

For Part 2, there is a linear solution that generalizes to negative numbers.
Let pre[i] = pre[i-1] + list[i]
That gives you prefix sums in linear time.
Next, use a hashmap and let sum_loc[pre[i]] = i

(caveat: need to handle collisions between indices but this is straightforward, just store an array at each instead).
Consider: each subarray has sum pre[j] - pre[i] which means if we're looking at pre[i] we just need to know if there's any pre[j] to the right of it with value exactly Target - pre[i]

That can be determined in constant time by lookup in the hashmap (the last item in the array will be rightmost so use that index if there's more than one)
"""

import collections
import fileinput
import itertools
import typing


def gather() -> typing.List[int]:
    result: typing.List[int] = []
    for line in fileinput.input():
        result.append(int(line.strip()))
    return result


def find_break(prologue: int, data: typing.List[int]) -> int:
    trailing = collections.deque(data[:prologue], prologue)
    for datum in data[prologue:]:
        found = False
        for x, y in itertools.combinations(trailing, 2):
            # print(f"DEBUG: looking for {datum} with {x} + {y} which is {x+y}")
            if x + y == datum:
                found = True
                break
        if not found:
            return datum
        trailing.append(datum)
    return -1


def find_sublist(looked_for_sum, data: typing.List[int]) -> typing.List[int]:
    for idx in range(len(data)):
        for sub_idx in range(idx, len(data)):
            tally = sum(data[idx:sub_idx])
            if tally == looked_for_sum:
                return data[idx:sub_idx]
            elif tally > looked_for_sum:
                break
    return [0, ]


def main() -> None:
    data = gather()
    # looked_for_sum = find_break(5, data)
    looked_for_sum = find_break(25, data)
    sublist = find_sublist(looked_for_sum, data)
    print(f"looked_for_sum {looked_for_sum} min: {min(sublist)} max: {max(sublist)} total: {min(sublist) + max(sublist)} sublist: {sublist}")


if __name__ == "__main__":
    main()
