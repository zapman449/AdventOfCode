#!/usr/bin/env python

import fileinput


def gather() -> int:
    result, new_group, sub_result = 0, True, set()
    for line in fileinput.input():
        if line == "\n":
            result += len(sub_result)
            new_group = True
        elif new_group:
            new_group = False
            sub_result = {char for char in line.strip()}
        else:
            sub_result = sub_result & {char for char in line.strip()}
    result += len(sub_result)
    return result


def main() -> None:
    print(gather())


if __name__ == "__main__":
    main()
