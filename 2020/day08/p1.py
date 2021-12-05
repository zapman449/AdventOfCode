#!/usr/bin/env python

"""
❯ ./p1.py input.short
5
❯ ./p1.py input.long
1548
"""

import fileinput
import typing


class Instruction(typing.NamedTuple):
    function: typing.Callable
    value: int


def acc(value: int, accumulator: int, stack_ptr: int,
        seen: typing.Set[int], instructions: typing.List[Instruction]) -> int:
    return traverse(accumulator+value, stack_ptr+1, seen, instructions)


def nop(value: int, accumulator: int, stack_ptr: int,
        seen: typing.Set[int], instructions: typing.List[Instruction]) -> int:
    return traverse(accumulator, stack_ptr+1, seen, instructions)


def jmp(value: int, accumulator: int, stack_ptr: int,
        seen: typing.Set[int], instructions: typing.List[Instruction]) -> int:
    return traverse(accumulator, stack_ptr+value, seen, instructions)


FUNCTDICT = {
    "acc": acc,
    "nop": nop,
    "jmp": jmp,
}


def traverse(accumulator: int, stack_ptr: int, seen: typing.Set[int], instructions: typing.List[Instruction]) -> int:
    if stack_ptr in seen:
        return accumulator
    inst = instructions[stack_ptr]
    seen.add(stack_ptr)
    return inst.function(inst.value, accumulator, stack_ptr, seen, instructions)


def gather() -> typing.List[Instruction]:
    instructions: typing.List[Instruction] = []
    for line in fileinput.input():
        words = line.strip().split()
        instructions.append(Instruction(FUNCTDICT[words[0]], int(words[1])))
    return instructions


def main() -> None:
    instructions = gather()
    print(traverse(0, 0, set(), instructions))


if __name__ == "__main__":
    main()
