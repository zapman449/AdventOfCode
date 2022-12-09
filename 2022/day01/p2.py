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

    elfmax = []
    for elf in elves:
        s = sum(elves[elf])
        elfmax.append(s)
    elfmax.sort()
    print(sum(elfmax[-3:]))


if __name__ == "__main__":
    main()

