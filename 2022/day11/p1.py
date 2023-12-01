#!/usr/bin/env python3

import collections
import copy
import fileinput
import pprint
import string
import sys
import typing


class Item(object):
    def __init__(self, worry_level: str):
        self._worry_level: int = int(worry_level)

    def __str__(self) -> str:
        return str(self._worry_level)

    def worry_level_int(self):
        return self._worry_level

    def inspect(self, operation: str) -> int:
        v1, instruction, v2 = operation.split(" ")
        if v1 == "old":
            v1i = self._worry_level
        else:
            v1i = int(v1)
        if v2 == "old":
            v2i = self._worry_level
        else:
            v2i = int(v2)
        if instruction == "+":
            self._worry_level = (v1i + v2i) // 3
        elif instruction == "*":
            self._worry_level = (v1i * v2i) // 3
        else:
            print(f"failed to parse operation {operation}")
            sys.exit()
        return self._worry_level


class Monkey(object):
    def __init__(self, items: typing.List[Item], operation: str, div_test: str, div_true: str, div_false: str, idx: int):
        self.items: typing.List[Item] = items
        self.operation = operation
        self.div_test = int(div_test)
        self.div_true = int(div_true)
        self.div_false = int(div_false)
        self.idx = idx
        self.inspect_count = 0

    def throws_to(self) -> typing.Tuple[typing.Union[Item, None], int]:
        if len(self.items) == 0:
            return None, -1
        i = self.items.pop(0)
        i.inspect(self.operation)
        self.inspect_count += 1
        if i.worry_level_int() % self.div_test == 0:
            return i, self.div_true
        return i, self.div_false

    def catch(self, item: Item):
        self.items.append(item)

    def __str__(self) -> str:
        return ", ".join(str(item) for item in self.items) + " -- " + str(self.inspect_count)

    def __int__(self) -> int:
        return self.inspect_count


def main() -> None:
    monkeys: typing.List[Monkey] = []
    scratch_items: typing.List[Item]
    scratch_operation: str
    scratch_div_test: str
    scratch_div_true: str
    scratch_div_false: str
    for line in fileinput.input():
        sline = line.strip()
        if sline.startswith("Monkey"):
            continue
        elif "Starting items:" in sline:
            words = sline.replace(",", "").split(" ")
            scratch_items = list(map(Item, words[2:]))
        elif "Operation:" in sline:
            scratch_operation = " ".join(sline.split(" ")[3:])
        elif "Test:" in sline:
            words = sline.split(" ")
            scratch_div_test = words[3]
        elif "If true:" in sline:
            scratch_div_true = sline.split(" ")[5]
        elif "If false:" in sline:
            scratch_div_false = sline.split(" ")[5]
            m = Monkey(scratch_items, scratch_operation, scratch_div_test, scratch_div_true, scratch_div_false, len(monkeys))
            monkeys.append(m)
        else:
            continue

    for idx, m in enumerate(monkeys):
        print(f"Monkey {idx}: {m}")

    for round_num in range(1, 21):
        for monkey in monkeys:
            while True:
                i, target = monkey.throws_to()
                if i is None:
                    break
                monkeys[target].catch(i)

    for idx, m in enumerate(monkeys):
        print(f"Monkey {idx}: {m}")
    print()
    for idx, m in enumerate(monkeys):
        print(f"Monkey {idx} inspected items {int(m)} times")

    # print(f"p1 {rolling_ss}, p2 {rolling_ss}")


if __name__ == "__main__":
    main()
