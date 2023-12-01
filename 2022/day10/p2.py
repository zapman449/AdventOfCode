#!/usr/bin/env python3

import collections
import copy
import fileinput
import pprint
import string
import sys
import typing


def main() -> None:
    r = 1
    cycle = 0
    commands = []
    for line in fileinput.input():
        commands.append(line.strip().split(" "))
    current_command = commands.pop(0)
    debug = current_command
    active_addx = False
    rolling_ss = 0
    pixel_row = []
    while True:
        cycle += 1
        add_me = 0
        if len(commands) == 0 and not active_addx:
            break
        if cycle > 240:
            break
        if current_command is None and not active_addx:
            current_command = commands.pop(0)
            debug = current_command
        if current_command[0] == "noop":
            current_command = None
        elif current_command[0] == "addx" and active_addx:
            add_me = int(current_command[1])
            current_command = None
            active_addx = False
        elif current_command[0] == "addx":
            active_addx = True

        # print(f"current command is {debug} --- cycle {cycle} register {r}")

        if cycle % 20 == 0 and (cycle / 20) % 2 == 1:
            # print("ss cycle", cycle, r, cycle * r)
            rolling_ss += cycle * r

        sprite = set([r, r+1, r+2])
        c = "."
        if cycle % 40 in sprite:
            c = "#"
        elif cycle % 40 == 0 and 40 in sprite:
            c = "#"
        pixel_row.append(c)
        rc = "".join(pixel_row)
        # if 195 <= cycle <= 205:
        #     print(f"cycle {cycle} sprite {sprite} register {r} c is {c} row {rc}")

        if cycle % 40 == 0:
            print("".join(pixel_row))
            pixel_row = []

        r += add_me

    print(f"p1 {rolling_ss}, p2 {rolling_ss}")


if __name__ == "__main__":
    main()
