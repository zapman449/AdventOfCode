#!/usr/bin/env python3

import argparse
import typing


def parseargs() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("input", help="input file")
    return parser.parse_args()


def parse_game(game: str) -> typing.Tuple[str, bool, int]:
    r_max = 12
    g_max = 13
    b_max = 14
    result = True
    r_game_max = 0
    g_game_max = 0
    b_game_max = 0
    for pull in game.split("; "):
        r = 0
        g = 0
        b = 0
        for color_count in pull.split(", "):
            count, color = color_count.split(" ")
            if color == "red":
                r += int(count)
                r_game_max = max(r_game_max, r)
            elif color == "green":
                g += int(count)
                g_game_max = max(g_game_max, g)
            elif color == "blue":
                b += int(count)
                b_game_max = max(b_game_max, b)
        if r > r_max:
            result = False
        if g > g_max:
            result = False
        if b > b_max:
            result = False
    return "", result, r_game_max*g_game_max*b_game_max


def main() -> None:
    args = parseargs()
    p1_tally = 0
    p2_tally = 0
    with open(args.input) as f:
        for line in f.readlines():
            idblock, games = line.strip().split(": ")
            game_id = int(idblock.split(" ")[1])
            msg, possible, power = parse_game(games)
            # print(f"debug: game {game_id} possible {possible} msg: {msg}")
            if possible:
                p1_tally += game_id
            p2_tally += power

    print(p1_tally, p2_tally)


if __name__ == "__main__":
    main()
