#!/usr/bin/env python3

import fileinput
import pprint
import string


def main() -> None:
    stack_set = [
        [],
        [],
        [],
        [],
        [],
        [],
        [],
        [],
        [],
    ]
    char2idx = {
        1: 0,
        5: 1,
        9: 2,
        13: 3,
        17: 4,
        21: 5,
        25: 6,
        29: 7,
        33: 8,
    }
    state = 0
    moves = []
    for line in fileinput.input():
        # print(repr(line))
        if len(line) < 2:
            continue
        if line[1] == "1":
            state += 1
            continue
        if state == 0:
            for char, idx in char2idx.items():
                try:
                    if line[char] == " ":
                        continue
                    stack_set[idx].append(line[char])
                except IndexError:
                    continue
        if state == 1:
            words = line.strip().split(" ")
            moves.append((int(words[1]), int(words[3]), int(words[5])))
    for s in stack_set:
        s.reverse()
    # pprint.pprint(stack_set)
    for count, src, dst in moves:
        for x in range(count):
            x = stack_set[src-1].pop()
            stack_set[dst-1].append(x)
    result = []
    for s in stack_set:
        try:
            result.append(s.pop())
        except IndexError:
            break
    r = "".join(result)
    print(f"part1: {r}")


if __name__ == "__main__":
    main()
