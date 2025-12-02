#!/usr/bin/env python3

# import collections
import fileinput
# import functools
# import sys
# import typing

class Dial(object):
    def __init__(self, start: int):
        self._index = start
        self._zero_count: int = 0
        self._cross_zero: int = 0

    @property
    def zero_count(self):
        return self._zero_count

    @property
    def cross_zero(self):
        return self._cross_zero

    ##################

    def turn_slow(self, input_str: str):
        direction = 1
        if input_str[0] == "L":
            direction = -1
        distance = int(input_str[1:])
        start_index = self._index
        for _ in range(0, distance):
            self._index += direction
            if self._index == 0:
                self._cross_zero += 1
            elif self._index == 100:
                self._cross_zero += 1
                self._index = 0
            elif self._index == -1:
                self._index = 99

        if self._index == 0:
            self._zero_count += 1

        # print(f"{start_index=} {input_str=} {self._index=}")

    ##################

    def turn_fast(self, input_str: str):
        direction = 1
        if input_str[0] == "L":
            direction = -1
        distance = int(input_str[1:])
        start_index = self._index

        negative_travel_distance = -1
        if direction == 1:
            idx = self._index + distance # * direction
            if idx % 100 == 0:
                self._index = 0
                self._zero_count += 1
            else:
                self._index = 0
                self._index = idx % 100
            self._cross_zero += idx // 100
        else: # direction == -1
            if distance < self._index:
                self._index -= distance
            else: # distance > self._index
                negative_travel_distance = -1 * (distance - self._index)
                if self._index == 0:
                    self._cross_zero += (negative_travel_distance // -100)
                else:
                    self._cross_zero += (negative_travel_distance // -100) + 1

                # NOW that our hacking is done, we can safely modify self._index
                self._index = (self._index - distance) % 100
                if self._index == 0:
                    self._zero_count += 1

        # print(f"{start_index=} {input_str=} {self._index=} {distance=} {negative_travel_distance=} {self._cross_zero=}")


def main() -> None:
    dial = Dial(50)
    dial_fast = Dial(50)

    for line in fileinput.input():
        # dial.turn_slow(line.strip())
        dial_fast.turn_fast(line.strip())
        # if dial.cross_zero != dial_fast.cross_zero:
        #     sys.exit(f"cross_zero mismatch {dial.cross_zero} != {dial_fast.cross_zero}")

    p1_tally = dial_fast.zero_count
    p2_tally = dial_fast.cross_zero
    print(f"final {p1_tally=}")
    print(f"final {p2_tally=}")

if __name__ == "__main__":
    main()
