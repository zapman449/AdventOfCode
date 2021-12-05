#!/usr/bin/env python3

import collections
import fileinput
import sys
import typing


def main() -> None:
    input_data: typing.List[int] = []
    parsed_data: typing.List[int] = []
    for line in fileinput.input():
        input_data.append(int(line.strip()))
    for idx in range(len(input_data) - 2):
        parsed_data.append(sum(input_data[idx:idx+3]))
    # print(f"parsed_data is {parsed_data}")
    previous = parsed_data[0]
    increase_counter = 0
    for parsed in parsed_data[1:]:
        if parsed > previous:
            increase_counter += 1
            # print(f"{num} (increased {increase_counter}, prev is {previous})")
        else:
            pass
            # print(f"{num} (other)")
        previous = parsed
    print(f"increased count is {increase_counter}")


if __name__ == "__main__":
    main()
