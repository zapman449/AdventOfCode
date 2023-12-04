#!/usr/bin/env python3

import argparse
import collections
import typing


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("input", help="input file")
    return parser.parse_args()


def get_input(in_file: str) -> typing.List[str]:
    with open(in_file) as f:
        return f.read().splitlines()


def parse_row(row: str) -> typing.Tuple[int, int, int]:
    split1 = row.split(": ")
    card = split1[0].split()[1]
    split2 = split1[1].split(" | ")
    winners = split2[0].split()
    attempts = split2[1].split()
    num_winners = sum([1 for attempt in attempts if attempt in winners])
    # my_winners = [attempt for attempt in attempts if attempt in winners]
    # my_winners.sort()
    if num_winners == 0:
        winner_value = 0
    else:
        winner_value = 2 ** (num_winners - 1)
    # print(f"{card}: {winners} {attempts} {my_winners} {tally} {result}")
    return int(card), num_winners, winner_value


def main() -> None:
    args = parse_args()
    data = get_input(args.input)
    p1_tally = 0
    p2_tally = 0
    copies: typing.Dict[int, int] = collections.defaultdict(lambda: 1)
    copies[1] = 1
    for row in data:
        card, num_winners, winner_value = parse_row(row)
        p1_tally += winner_value

        card_count = copies[card]
        for t_card in range(card+1, card+num_winners+1):
            # ctc = copies[t_card]
            copies[t_card] += card_count
            # nctc = copies[t_card]
            # print(f"due to card {card} added {card_count} to card {t_card} - old value {ctc} new value {nctc}")
    for k, v in copies.items():
        p2_tally += v

    print(f"Solution: Part 1: {p1_tally} Part 2: {p2_tally}")


if __name__ == "__main__":
    main()
