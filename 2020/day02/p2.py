#!/usr/bin/env python

import typing


class PasswordEntry(typing.NamedTuple):
    position1: int
    position2: int
    required_str: str
    passwd: str


def gather() -> typing.List[PasswordEntry]:
    result: typing.List[PasswordEntry] = []
    with open('input', 'r') as i:
        for line in i:
            words = line.strip().split()
            position1, position2 = words[0].split("-")
            required_str = words[1].split(":")[0]
            passwd = words[2]
            result.append(PasswordEntry(
                int(position1), int(position2), required_str, passwd
            ))
    return result


def process(entry: PasswordEntry) -> bool:
    p1 = entry.passwd[entry.position1 - 1] == entry.required_str
    p2 = entry.passwd[entry.position2 - 1] == entry.required_str
    return p1 ^ p2


def main() -> None:
    entries = gather()
    valid = 0
    invalid = 0
    total = 0
    for entry in entries:
        try:
            if process(entry):
                valid += 1
            else:
                invalid += 1
            total += 1
        except:
            print(repr(entry))
            raise
    print(f"Total entries: {total}. Valid entries: {valid}, Invalid entries: {invalid}")


if __name__ == "__main__":
    main()
