#!/usr/bin/env python3.9

# import collections
import re
import typing


class PasswordEntry(typing.NamedTuple):
    min_repeats: int
    max_repeats: int
    required_str: str
    passwd: str


def gather() -> typing.List[PasswordEntry]:
    result: typing.List[PasswordEntry] = []
    with open('input', 'r') as i:
        for line in i:
            words = line.strip().split()
            min_repeats, max_repeats = words[0].split("-")
            required_str = words[1].split(":")[0]
            passwd = words[2]
            result.append(PasswordEntry(
                int(min_repeats), int(max_repeats), required_str, passwd
            ))
    return result


def process(entry: PasswordEntry) -> bool:
    matches = re.findall(entry.required_str, entry.passwd)
    if entry.min_repeats <= len(matches) <= entry.max_repeats:
        return True
    return False


def main() -> None:
    entries = gather()
    valid = 0
    invalid = 0
    total = 0
    for entry in entries:
        if process(entry):
            valid += 1
        else:
            invalid += 1
        total += 1
    print(f"Total entries: {total}. Valid entries: {valid}, Invalid entries: {invalid}")


if __name__ == "__main__":
    main()
