#!/usr/bin/env python

"""
❯ ./p2.py input.short
8
❯ ./p2.py input.long
1375
"""

import copy
import fileinput
import typing


class Instruction(typing.NamedTuple):
    function: typing.Callable
    value: int


def acc(value: int, accumulator: int, stack_ptr: int, changed_one_instruction: bool,
        seen: typing.Set[int], instructions: typing.List[Instruction]) -> int:
    return traverse(accumulator+value, stack_ptr+1, changed_one_instruction, seen, instructions)


def nop(value: int, accumulator: int, stack_ptr: int, changed_one_instruction: bool,
        seen: typing.Set[int], instructions: typing.List[Instruction]) -> int:
    non_corrupt = traverse(accumulator, stack_ptr+1, changed_one_instruction, seen, instructions)
    if non_corrupt == 0 and changed_one_instruction is False:
        # try jump instead
        return jmp(value, accumulator, stack_ptr, True, seen, instructions)
    return non_corrupt


def jmp(value: int, accumulator: int, stack_ptr: int, changed_one_instruction: bool,
        seen: typing.Set[int], instructions: typing.List[Instruction]) -> int:
    non_corrupt = traverse(accumulator, stack_ptr+value, changed_one_instruction, seen, instructions)
    if non_corrupt == 0 and changed_one_instruction is False:
        # try nop instead
        return nop(value, accumulator, stack_ptr, True, seen, instructions)
    return non_corrupt


FUNCTDICT = {
    "acc": acc,
    "nop": nop,
    "jmp": jmp,
}


def traverse(accumulator: int, stack_ptr: int, changed_one_instruction: bool,
             seen: typing.Set[int], instructions: typing.List[Instruction]) -> int:
    if len(instructions)-1 < stack_ptr:
        return accumulator
    elif stack_ptr in seen:
        return 0
    inst = instructions[stack_ptr]
    new_seen = copy.copy(seen)
    new_seen.add(stack_ptr)
    return inst.function(inst.value, accumulator, stack_ptr, changed_one_instruction, new_seen, instructions)


def gather() -> typing.List[Instruction]:
    instructions: typing.List[Instruction] = []
    for line in fileinput.input():
        words = line.strip().split()
        instructions.append(Instruction(FUNCTDICT[words[0]], int(words[1])))
    return instructions


def g2() -> typing.List[Instruction]:
    return [Instruction(FUNCTDICT[op], int(val)) for line in fileinput.input() for op, val in [line.strip().split()]]


def main() -> None:
    # instructions = gather()
    instructions = g2()
    print(traverse(0, 0, False, set(), instructions))


if __name__ == "__main__":
    main()
