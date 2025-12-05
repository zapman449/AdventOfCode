#!/usr/bin/env python3

# import collections
# import collections
import fileinput
# import functools
# import itertools
import sys
import typing


def parse_input() ->  typing.Tuple[typing.List[typing.Tuple[int, int]], typing.List[int]]:
    fresh_ids: typing.List[typing.Tuple[int, int]] = []
    questionable_ids: typing.List[int] = []
    pairs = True
    for line in fileinput.input():
        if len(line.strip()) == 0:
            pairs = False
        elif pairs:
            x, y = map(int, line.strip().split("-"))
            fresh_ids.append((x,y))
        else:
            questionable_ids.append(int(line.strip()))

    return fresh_ids, questionable_ids


def run_tests():
    success = True
    fresh_ids = [
        (3,5),
        (10,14),
        (16,20),
        (12,18),
    ]
    questionable_ids = [
        (1, 0),
        (5, 1),
        (8, 0),
        (11, 1),
        (17, 1),
        (32, 0),
    ]
    for id, want in questionable_ids:
        got = p1(fresh_ids, [id,])
        if got != want:
            success = False
            print(f"{id=} {want=} {got=}")
    fresh_ids_2 = [
        ((3,5), 3),
        ((10,14), 8),
        ((16,20), 13),
        ((12,18), 14),
    ]
    fi = []
    for pair, want_tally in fresh_ids_2:
        fi.append(pair)
        got_tally = p2(fi)
        if got_tally != want_tally:
            success = False
            print(f"{fi=} {want_tally=}, {got_tally=}")

    if not success:
        sys.exit(1)


def p1(fresh_ids: typing.List[typing.Tuple[int, int]], questionable_ids: typing.List[int]) -> int:
    tally = 0
    for id in questionable_ids:
        for x, y in fresh_ids:
            if x <= id <= y:
                tally += 1
                break
    return tally


def overlapping_range(x1, y1, x2, y2: int) -> bool:
    if x1 <= x2 <= y1:
        return True
    elif x1 <= y2 <= y1:
        return True
    return False


def expand_range(x1, y1, x2, y2: int) -> typing.Tuple[int, int]:
    if x2 > y2:
        return x1, y1
    x = min(x1, x2)
    y = max(y1, y2)
    return x, y


def find_overlap(consolidated_ids: typing.List[typing.Tuple[int, int]], x, y) -> int:
    for idx, pair in enumerate(consolidated_ids):
        cx, cy = pair
        if overlapping_range(cx, cy, x, y):
            return idx
    return -1


def p2(fresh_ids: typing.List[typing.Tuple[int, int]]) -> int:
    # this will blow up in the face of pathological input (like 3-1)
    fis = sorted(fresh_ids, key=lambda a: a[0])
    consolidated_ids: typing.List[typing.Tuple[int, int]] = [fis[0]]
    for fx, fy in fis[1:]:
        overlap = False
        overlap_idx = -1
        for idx, ids in enumerate(consolidated_ids):
            cx, cy = ids
            overlap = overlapping_range(cx, cy, fx, fy)
            if overlap:
                overlap_idx = idx
                break
        if overlap:
            cx, cy = consolidated_ids[overlap_idx]
            new_x, new_y = expand_range(cx, cy, fx, fy)
            consolidated_ids[overlap_idx] = (new_x, new_y)
        else:
            consolidated_ids.append((fx, fy))
    tally = 0
    for x, y in consolidated_ids:
        tally += y - x + 1
    return tally


def main() -> None:
    run_tests()
    fresh_ids, questionable_ids = parse_input()
    p1_tally = p1(fresh_ids, questionable_ids)
    p2_tally = p2(fresh_ids)

    print(f"final {p1_tally=}")
    print(f"final {p2_tally=}")

if __name__ == "__main__":
    main()
