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


def gather() -> typing.Dict[str, typing.Dict[str, typing.Any]]:
    current_tile: typing.List[str] = []
    current_id = ""
    result: typing.Dict[str, typing.Dict] = {}
    for line in fileinput.input():
        if line.startswith("Tile"):
            current_id = line.strip().split()[1][:-1]
        elif line == "\n":
            result[current_id] = {'tile': current_tile, 'edges': []}
            current_id = ""
            current_tile = []
        else:
            current_tile.append(line.strip())
    result[current_id] = {'tile': current_tile, 'edges': []}
    return result


def setup_edges(tiles: typing.Dict[str, typing.Dict[str, typing.Any]]):
    for tile_id in tiles:
        # top
        edge1 = tiles[tile_id]['tile'][0]
        edge2 = tiles[tile_id]['tile'][0][::-1]
        # left
        edge3 = "".join([r[0] for r in tiles[tile_id]['tile']])
        edge4 = edge3[::-1]
        # bottom
        edge5 = tiles[tile_id]['tile'][-1]
        edge6 = tiles[tile_id]['tile'][-1][::-1]
        # right
        edge7 = "".join([r[-1] for r in tiles[tile_id]['tile']])
        edge8 = edge7[::-1]
        tiles[tile_id]['edges'] = [edge1, edge2, edge3, edge4, edge5, edge6, edge7, edge8]


def find_left_candidates(start_tile_id: str,
                         right_edge_idx: int,
                         tiles: typing.Dict[str, typing.Dict[str, typing.Any]],
                         consumed: typing.Set[str]) -> typing.Tuple[str, int]:
    left_edge_idx = (right_edge_idx + 4) % 8
    left_edge = tiles[start_tile_id]['edges'][left_edge_idx]
    for tile_id in tiles:
        if tile_id in consumed or tile_id == start_tile_id:
            continue
        if left_edge in tiles[tile_id]['edges']:
            print(f"tile_id {start_tile_id} has possible left neighbor of tile_id {tile_id}")
            yield tile_id, tiles[tile_id]['edges'].index(left_edge)


def find_opposite_candidates(start_tile_id: str,
                             start_edge_idx: int,
                             tiles: typing.Dict[str, typing.Dict[str, typing.Any]],
                             consumed: typing.Set[str]) -> typing.Tuple[str, int]:
    opposite_edge_idx = (start_edge_idx + 4) % 8
    opposite_edge = tiles[start_tile_id]['edges'][opposite_edge_idx]
    for tile_id in tiles:
        if tile_id in consumed or tile_id == start_tile_id:
            continue
        if opposite_edge in tiles[tile_id]['edges']:
            print(f"tile_id {start_tile_id} has possible opposite neighbor of tile_id {tile_id} edge_idx {tiles[tile_id]['edges'].index(opposite_edge)}")
            yield tile_id, tiles[tile_id]['edges'].index(opposite_edge)


def find_x_left_candidates(tiles: typing.Dict[str, typing.Dict[str, typing.Any]], count: int) -> typing.List[str]:
    for tile_id in tiles:
        for edge_idx, edge in enumerate(tiles[tile_id]['edges']):
            finished = True
            consumed: typing.Set[str] = set()
            for x in range(count):
                for found_tile in find_left_candidates(tile_id, edge_idx, tiles, consumed):
                    consumed.add(tile_id)



def main() -> None:
    tiles = gather()
    setup_edges(tiles)
    # find_left_candidates("3079", 6, tiles, set())


if __name__ == "__main__":
    main()
