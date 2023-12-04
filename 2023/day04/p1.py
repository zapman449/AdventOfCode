#!/usr/bin/env python3

import argparse
import collections
import typing


def parseargs() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("input", help="input file")
    return parser.parse_args()


def get_input(in_file: str) -> typing.List[str]:
    with open(in_file) as f:
        return [line.strip() for line in f.readlines()]


def parse_row(row: str) -> typing.Tuple[int, int, int]:
    split1 = row.split(": ")
    card = split1[0].split()[1]
    split2 = split1[1].split(" | ")
    winners = split2[0].split()
    attempts = split2[1].split()
    tally = sum([1 for attempt in attempts if attempt in winners])
    my_winners = [attempt for attempt in attempts if attempt in winners]
    my_winners.sort()
    if tally == 0:
        result = 0
    else:
        result = 2 ** (tally - 1)
    # print(f"{card}: {winners} {attempts} {my_winners} {tally} {result}")
    return int(card), tally, result


# 1
# 2 1c
# 3 1c 2c
# 4 1c 2c 4c
# 5 1c    4c 8c
# 6

def main() -> None:
    args = parseargs()
    data = get_input(args.input)
    p1_tally = 0
    p2_tally = 0
    copies: typing.Dict[int, int] = collections.defaultdict(lambda: 1)
    copies[1] = 1
    for row in data:
        try:
            card, num_winners, winner_value = parse_row(row)
        except ValueError:
            print(f"failed to parse row {row}")
            raise
        p1_tally += winner_value

        card_count = copies[card]
        for t_card in range(card+1, card+num_winners+1):
            # ctc = copies[t_card]
            copies[t_card] += card_count
            # nctc = copies[t_card]
            # print(f"due to card {card} added {card_count} to card {t_card} - old value {ctc} new value {nctc}")
    for k, v in copies.items():
        # print(f"card {k}: {v}")
        p2_tally += v

    print(f"Solution: Part 1: {p1_tally} Part 2: {p2_tally}")


if __name__ == "__main__":
    main()
