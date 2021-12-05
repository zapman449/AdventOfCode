#!/usr/bin/env python

import fileinput
import sys
import typing


class Slope(object):
    def __init__(self, right: int, down: int):
        self.slope: typing.List[typing.List[str]] = []
        self.current_location: typing.List[int] = [0, 0]
        self.down = down
        self.right = right
        self.trees_hit = 0
        self._read_file()
        self.right_max = len(self.slope[0])
        self.down_max = len(self.slope)

    def _read_file(self):
        idx = 0
        for line in fileinput.input():
            self.slope.append([])
            for char in line.strip():
                self.slope[idx].append(char)
            idx += 1
        # self.print_slope()

    def print_slope(self):
        for row in self.slope:
            print("".join(row))

    def _update_location(self):
        self.current_location[0] += self.right
        self.current_location[1] += self.down

    def _reconcile_location(self) -> bool:
        # print(f"reconciling. start {self.current_location} right_max {self.right_max} down_max {self.down_max}")
        if self.current_location[1] >= self.down_max:
            return False
        self.current_location[0] = self.current_location[0] % self.right_max
        # print(f"reconciling. end {self.current_location} right_max {self.right_max} down_max {self.down_max}")
        return True

    def _get_char(self) -> str:
        return self.slope[self.current_location[1]][self.current_location[0]]

    def _set_char(self, new_char: str):
        self.slope[self.current_location[1]][self.current_location[0]] = new_char

    def _on_tree(self) -> bool:
        # side_effect: marks spot
        location_char = self._get_char()
        if location_char == "#":
            self._set_char("X")
            return True
        elif location_char == "X":
            return True
        elif location_char == ".":
            self._set_char("O")
            return False
        elif location_char == "O":
            return False
        else:
            print("ERROR!!!")
            self.print_slope()
            sys.exit(1)

    def iterate(self) -> bool:
        # print(f"start location: {repr(self.current_location)}, trees_hit: {self.trees_hit}")
        self._update_location()
        if not self._reconcile_location():
            return False
        if self._on_tree():
            self.trees_hit += 1
        # print(f"end location: {repr(self.current_location)} trees_hit: {self.trees_hit}")
        # self.print_slope()
        return True

    def get_trees_hit(self) -> int:
        return self.trees_hit


def slope_for_angle(right: int, down: int) -> int:
    slope = Slope(right, down)
    while slope.iterate():
        pass
    return slope.get_trees_hit()


def main() -> None:
    trees_hit: typing.List[int] = []
    # for down, right in [(3,1), ]:
    for down, right in [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]:
        trees_hit.append(slope_for_angle(down, right))
    trees_sum = sum(trees_hit)
    trees_product = 1
    for hit in trees_hit:
        trees_product = trees_product * hit
    print(repr(trees_hit))
    print(f"sum trees hit {trees_sum} product trees hit {trees_product}")


if __name__ == "__main__":
    main()
