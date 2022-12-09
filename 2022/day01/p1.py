#!/usr/bin/env python3

import fileinput


def main() -> None:
    elves = {}
    counter = 0
    for line in fileinput.input():
        # print(f"elfnum is {counter} len(line) is {len(line)} line is: {repr(line)}")
        if len(line) < 2:
            counter += 1
            # print("skipping")
            continue
        if counter not in elves:
            elves[counter] = []
            # print("new elf")
        elves[counter].append(int(line.strip()))
        # print(f"end of line, elves[counter] is {repr(elves[counter])}")

    elfmax = 0
    for elf in elves:
        s = sum(elves[elf])
        if s > elfmax:
            elfmax = s
    print(elfmax)


if __name__ == "__main__":
    main()

