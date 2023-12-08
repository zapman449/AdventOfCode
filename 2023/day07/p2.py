#!/usr/bin/env python3

import argparse
import collections
import itertools
import pprint
import sys
import typing

CARDS = ["A", "K", "Q", "T", "9", "8", "7", "6", "5", "4", "3", "2", "J"]
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
    five_of_kind = 7
    four_of_kind = 6
    full_house = 5
    three_of_kind = 4
    two_pair = 3
    pair = 2
    high_card = 1
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
        j_count = self.card_collection["J"]
        cards_no_j = self.cards.replace("J", "")
        cards_no_j_collection = collections.Counter(cards_no_j)
        t = collections.Counter(cards_no_j_collection.values())
        if 5 in self.card_collection.values():
            self.hand_type = Hand.five_of_kind
        elif j_count == 1 and 4 in cards_no_j_collection.values():
            self.hand_type = Hand.five_of_kind
        elif j_count == 2 and 3 in cards_no_j_collection.values():
            self.hand_type = Hand.five_of_kind
        elif j_count == 3 and 2 in cards_no_j_collection.values():
            self.hand_type = Hand.five_of_kind
        elif j_count == 4:
            self.hand_type = Hand.five_of_kind
        ###
        elif j_count == 0 and 4 in self.card_collection.values():
            self.hand_type = Hand.four_of_kind
        elif j_count == 1 and 3 in cards_no_j_collection.values():
            self.hand_type = Hand.four_of_kind
        elif j_count == 2 and 2 in cards_no_j_collection.values():
            self.hand_type = Hand.four_of_kind
        elif j_count == 3:
            self.hand_type = Hand.four_of_kind

        if self.hand_type != 0:
            return
        ###
        if j_count == 0 and 2 in self.card_collection.values() and 3 in self.card_collection.values():
            self.hand_type = 5  # full house
        # a pair + pair of jokers == 4 of kind
        elif j_count == 1 and t[2] == 2:
            self.hand_type = Hand.full_house
        ###
        elif j_count == 0 and 3 in cards_no_j_collection.values():
            self.hand_type = Hand.three_of_kind
        elif j_count == 1 and 2 in cards_no_j_collection.values():
            self.hand_type = Hand.three_of_kind
        elif j_count == 2 and 1 in cards_no_j_collection.values():
            self.hand_type = Hand.three_of_kind
        ###
        elif j_count == 0 and t[2] == 2:
            self.hand_type = Hand.two_pair
        # a pair + a joker = 3 of a kind
        ###
        elif j_count == 0 and t[2] == 1:
            self.hand_type = Hand.pair
        elif j_count == 1:
            self.hand_type = Hand.pair
        elif j_count == 0:
            self.hand_type = Hand.high_card
        else:
            print(f"debug: WAT: {self.cards} j_count: {j_count}")
        return


def test(h1: Hand, h2: Hand, winner: Hand) -> bool:
    l = [h1, h2]
    l.sort()
    if winner.cards == l[1].cards:
        return True
    print(f"test failed {h1.cards} should be < {h2.cards}")
    return False


def run_tests() -> None:
    h1 = Hand("32T3K", "765")  # 1
    h2 = Hand("T55J5", "684")  # 3
    h3 = Hand("KK677", "28")   # 2
    h4 = Hand("KTJJT", "220")  # 5
    h5 = Hand("QQQJA", "483")  # 4
    succeeded = True
    succeeded = test(h1, h2, h2) & succeeded  # test pair vs 3 of kind
    succeeded = test(h1, h3, h3) & succeeded  # test pair vs 2 pair
    succeeded = test(h2, h5, h5) & succeeded  # test 2x 3 of kind
    succeeded = test(h4, h2, h4) & succeeded  # test 2pair vs 3 of kind
    h6 = Hand("JKKKK", "580")
    h7 = Hand("K8888", "387")
    succeeded = test(h6, h7, h6) & succeeded  # two x 4 of kind
    h8 = Hand("KKKQQ", "580")
    succeeded = h8.hand_type == 5 and succeeded
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
    p2_tally = 0
    for idx, hand in enumerate(hands):
        hand.rank = idx + 1
        p2_tally += hand.bid * hand.rank
        # print(repr(hand))

    print(f"Solution: Part 2: {p2_tally}")
    # print("DEBUG2")
    # x = Hand("JKKKK", "580", True)
    # y = Hand("K8888", "387", True)
    # z = [x, y]
    # z.sort()
    # for a in z:
    #     print(repr(a))


if __name__ == "__main__":
    main()
