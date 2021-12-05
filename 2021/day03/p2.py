#!/usr/bin/env python3

import fileinput
import pprint
import sys
import typing


def most_common(idx: int, diag: typing.List[typing.List[int]], most: bool) -> typing.List[typing.List[int]]:
    ones, zeros = 0, 0
    list_ones, list_zeros = [], []
    for diag_row in diag:
        if diag_row[idx] == 1:
            ones += 1
            list_ones.append(diag_row)
        else:
            zeros += 1
            list_zeros.append(diag_row)
    if most is True:
        if ones >= zeros:
            return list_ones
        return list_zeros
    else:
        if ones >= zeros:
            return list_zeros
        return list_ones


def to_decimal(diag: typing.List[int]) -> int:
    bin_str = ''.join(map(str, diag))
    return int(bin_str, 2)


def main() -> None:
    data = [list(map(int, list(digits.strip()))) for digits in fileinput.input()]
    # pprint.pprint(data)
    breaker = len(data[0])
    o2_rating_consideration = data
    co2_scrubber_consideration = data
    for idx in range(breaker):
        if len(o2_rating_consideration) > 1:
            current_o2 = most_common(idx, o2_rating_consideration, True)
            o2_rating_consideration = current_o2
        if len(co2_scrubber_consideration) > 1:
            current_co2 = most_common(idx, co2_scrubber_consideration, False)
            co2_scrubber_consideration = current_co2
    o2_rating = to_decimal(o2_rating_consideration[0])
    co2_scrubber = to_decimal(co2_scrubber_consideration[0])
    print(f"o2_rating {o2_rating} co2_scrubber {co2_scrubber} product {o2_rating*co2_scrubber}")


if __name__ == "__main__":
    main()
