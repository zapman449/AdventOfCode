#!/usr/bin/env python3.9

import fileinput
import re
import typing

# byr (Birth Year)
# iyr (Issue Year)
# eyr (Expiration Year)
# hgt (Height)
# hcl (Hair Color)
# ecl (Eye Color)
# pid (Passport ID)
# cid (Country ID)
REQUIRED_FIELDS = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
OPTIONAL_FIELDS = ['cid']
ALL_FIELDS = REQUIRED_FIELDS + OPTIONAL_FIELDS


def gather() -> typing.List[typing.Dict]:
    result: typing.List[typing.Dict] = []
    current = {}
    for line in fileinput.input():
        if line == "\n" and current != {}:
            result.append(current)
            current = {}
        kvs = line.strip().split()
        for kv in kvs:
            key, value = kv.split(":")
            if key in current:
                print(f"WARNING. key {key} already exists in current {current}")
            current[key] = value
    if current != {}:
        result.append(current)
    return result


def verify(entry: dict) -> bool:
    if 1920 <= int(entry['byr']) <= 2002:
        pass
    else:
        print(f"DEBUG: entry fails byr {entry}")
        return False

    if 2010 <= int(entry['iyr']) <= 2020:
        pass
    else:
        print(f"DEBUG: entry fails iyr {entry}")
        return False

    if 2020 <= int(entry['eyr']) <= 2030:
        pass
    else:
        print(f"DEBUG: entry fails eyr {entry}")
        return False

    if entry['hgt'].endswith("cm"):
        value = entry['hgt'][0:-2]
        if 150 <= int(value) <= 193:
            pass
        else:
            print(f"DEBUG: entry fails hgt cm {entry}")
            return False
    elif entry['hgt'].endswith("in"):
        value = entry['hgt'][0:-2]
        if 59 <= int(value) <= 76:
            pass
        else:
            print(f"DEBUG: entry fails hgt in {entry}")
            return False
    else:
        return False

    if re.match(r"^#[0-9a-f]{6}$", entry['hcl']) is None:
        print(f"DEBUG: entry fails hcl in {entry}")
        return False

    if entry['ecl'] not in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
        print(f"DEBUG: entry fails ecl in {entry}")
        return False

    if re.match(r"^\d{9}$", entry['pid']) is None:
        print(f"DEBUG: entry fails pid in {entry}")
        return False

    return True


def process(entry: dict) -> bool:
    fields = entry.keys()
    min_fields = len(REQUIRED_FIELDS)
    max_fields = len(REQUIRED_FIELDS) + len(OPTIONAL_FIELDS)
    for key in REQUIRED_FIELDS:
        if key not in entry:
            return False
    for key in entry:
        if key not in ALL_FIELDS:
            return False
    if min_fields <= len(fields) <= max_fields:
        # print(f"DEBUG: entry is {entry}")
        # print(f"DEBUG: len(fields) is {len(fields)}, min/max is {min_fields}/{max_fields}")
        try:
            return verify(entry)
        except ValueError:
            return False
    return False


def main() -> None:
    entries = gather()
    valid, invalid, total = 0, 0, 0
    for entry in entries:
        if process(entry):
            valid += 1
        else:
            invalid += 1
        total += 1
    print(f"total {total}, valid {valid}, invalid {invalid}")


if __name__ == "__main__":
    main()
