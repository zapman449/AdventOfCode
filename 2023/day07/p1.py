#!/usr/bin/env python3

import argparse
import collections
import itertools
import pprint
import sys
import typing

CARDS = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]
CARDS.reverse()


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("input", help="input file")
    return parser.parse_args()


def get_input(in_file: str) -> typing.List[str]:
    with open(in_file) as f:
        return f.read().splitlines()


def card_lt(c1: str, c2: str, debug=False) -> bool:
    # c1 == c2 handled by caller
    c1idx = CARDS.index(c1)
    c2idx = CARDS.index(c2)
    if debug:
        print(f"c1: {c1} c2: {c2} c1idx: {c1idx} c2idx: {c2idx} result {c1idx < c2idx}")
    return c1idx < c2idx


class Hand(object):
    def __init__(self, cards: str, bid: str, debug=False):
        self.bid = int(bid)
        self.cards = cards
        self.rank = -1
        self.card_collection = collections.Counter(self.cards)
        self.hand_type = 0
        self._set_hand_type()
        self.debug = debug

    def __repr__(self):
        return f"{self.cards} bid: {self.bid} ht: {self.hand_type} rank: {self.rank}"

    def __lt__(self, other):
        if self.hand_type < other.hand_type:
            return True
        elif self.hand_type > other.hand_type:
            return False
        else:
            for idx in range(5):
                if self.cards[idx] == other.cards[idx]:
                    if self.debug:
                        print(f"cards equal - idx: {idx} self.cards[idx]: {self.cards[idx]} other.cards[idx]: {other.cards[idx]}")
                    continue
                return card_lt(self.cards[idx], other.cards[idx], self.debug)

    def _set_hand_type(self) -> None:
        # print(self.card_collection)
        if 5 in self.card_collection.values():
            self.hand_type = 7  # 5 of kind
        elif 4 in self.card_collection.values():
            self.hand_type = 6  # 4 of kind
        elif 3 in self.card_collection.values() and 2 in self.card_collection.values():
            self.hand_type = 5  # full house
        elif 3 in self.card_collection.values():
            self.hand_type = 4  # 3 of kind
        if self.hand_type != 0:
            return
        t = collections.Counter(self.card_collection.values())
        # print(t)
        if t[2] == 2:
            self.hand_type = 3  # 2 pair
        elif 2 in self.card_collection.values():
            self.hand_type = 2  # 1 pair
        else:
            self.hand_type = 1
        return


def test(h1: Hand, h2: Hand, winner: Hand) -> bool:
    l = [h1, h2]
    l.sort()
    if winner.cards == l[1].cards:
        return True
    print(f"test failed {h1.cards} should be < {h2.cards}")
    return False


def run_tests() -> None:
    h1 = Hand("32T3K", "765")
    h2 = Hand("T55J5", "684")
    h3 = Hand("KK677", "28")
    h4 = Hand("KTJJT", "220")
    h5 = Hand("QQQJA", "483")
    succeeded = True
    succeeded = test(h1, h2, h2) & succeeded  # test pair vs 3 of kind
    succeeded = test(h1, h3, h3) & succeeded  # test pair vs 2 pair
    succeeded = test(h2, h5, h5) & succeeded  # test 2x 3 of kind
    succeeded = test(h4, h2, h2) & succeeded  # test 2pair vs 3 of kind
    h6 = Hand("JKKKK", "580")
    h7 = Hand("K8888", "387")
    succeeded = test(h6, h7, h7) & succeeded  # two x 4 of kind
    if not succeeded:
        print("Tests failed")
        sys.exit(1)


def main() -> None:
    args = parse_args()
    data = get_input(args.input)
    run_tests()
    hands: typing.List[Hand] = []
    for line in data:
        cards, bid = line.split()
        hands.append(Hand(cards, bid))
    hands.sort()
    for idx, hand in enumerate(hands):
        hand.rank = idx + 1
        # print(repr(hand))

    p1_tally = 0
    for hand in hands:
        p1_tally += hand.bid * hand.rank

    print(f"Solution: Part 1: {p1_tally}")
    # print("DEBUG2")
    # x = Hand("JKKKK", "580", True)
    # y = Hand("K8888", "387", True)
    # z = [x, y]
    # z.sort()
    # for a in z:
    #     print(repr(a))


if __name__ == "__main__":
    main()
