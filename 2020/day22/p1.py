#!/usr/bin/env python3

"""

"""

import collections
import copy
import fileinput
import pprint
import re
import typing
import sys


def gather() -> typing.Dict[str, typing.Deque[int]]:
    result: typing.Dict[str, typing.Deque[int]] = {}
    result_key = ""
    for line in fileinput.input():
        if line.startswith("Player"):
            result_key = line.strip()
        elif line == "\n":
            continue
        else:
            result.setdefault(result_key, collections.deque()).append(int(line.strip()))
    return result


def play_round(count: int, decks: typing.Dict[str, typing.Deque[int]]) -> None:
    # print()
    # print(f"-- Round {count} --")
    # for p in decks.keys():
    #     print(f"{p}'s deck: {decks[p]}")
    cards = []
    for p in decks.keys():
        v = decks[p].popleft()
        # print(f"{p} plays: {v}")
        card = (p, v)
        cards.append(card)
    cards.sort(key=lambda x: x[1], reverse=True)
    winner = cards[0][0]
    # print(f"{winner} wins the round")
    for card in cards:
        decks[winner].append(card[1])


def total_cards(decks: typing.Dict[str, typing.Deque[int]]) -> int:
    return sum([len(decks[p]) for p in decks.keys()])


def play(decks: typing.Dict[str, typing.Deque[int]]) -> typing.Deque[int]:
    card_count = total_cards(decks)
    turn = 0
    while True:
        turn += 1
        if turn % 10 == 0:
            print(f"playing round {turn}")
        for p in decks:
            if len(decks[p]) == card_count:
                return decks[p]
        play_round(turn, decks)


def score_deck(deck: typing.Deque[int]) -> int:
    deck.reverse()
    tally = 0
    for idx, card in enumerate(deck):
        tally += (idx + 1) * card
    return tally


def main() -> None:
    decks = gather()
    winning_deck = play(decks)
    print(winning_deck)
    print(f"score is {score_deck(winning_deck)}")


if __name__ == "__main__":
    main()
