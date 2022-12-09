#!/usr/bin/env python3

import fileinput
import pprint
import string


def chunk_not_equal(length: int, iput: str) -> bool:
    if len(iput) != length:
        print(f"length of iput is wrong. expected {length} got {len(iput)} for iput {iput}")
        return False
    return len(set(iput)) == length


def main() -> None:
    line_counter = 0
    for line in fileinput.input():
        if line.startswith("# "):
            continue
        line_counter += 1
        found_som, found_sop = False, False
        for start in range(len(line.strip())):
            if not found_sop and start + 4 < len(line.strip()) and chunk_not_equal(4, line[start:start+4]):
                print(f"SoP marker for line {line_counter} is {start + 4}")
                found_sop = True
            if not found_som and start + 14 < len(line.strip()) and chunk_not_equal(14, line[start:start+14]):
                print(f"SoM marker for line {line_counter} is {start + 14}")
                found_som = True


if __name__ == "__main__":
    main()
