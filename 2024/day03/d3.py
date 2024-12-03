#!/usr/bin/env python3

import fileinput
import re

# xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))
# 161 (2*4 + 5*5 + 11*8 + 8*5)
# 48 (2*4 + 8*5)


def calc_subline(subline: str) -> int:
    tally: int = 0
    mul = re.compile(r"mul\((\d+),(\d+)\)")
    matches = mul.findall(subline)
    for match in matches:
        x, y = map(int, match)
        tally += x * y
    return tally


def main() -> None:
    p1_tally: int = 0
    p2_tally: int = 0
    do: bool = True
    dostr = "do()"
    dontstr = "don't()"
    for line in fileinput.input():
        p1_tally += calc_subline(line)

        while True:
            if do:
                off_idx = line.find(dontstr)
                if off_idx == -1:
                    p2_tally += calc_subline(line)
                    break
                else:
                    p2_tally += calc_subline(line[:off_idx])
                    line = line[off_idx + len(dontstr) :]
                    do = False
            else:
                on_idx = line.find(dostr)
                if on_idx == -1:
                    break
                else:
                    line = line[on_idx + len(dostr) :]
                    do = True

    print("p1: ", p1_tally)
    print("p2: ", p2_tally)


if __name__ == "__main__":
    main()
