#!/usr/bin/env python3

"""

"""

import fileinput
import functools
import typing

EMPTY = "L"
OCCUPIED = "#"
FLOOR = "."


def gather() -> typing.List[typing.List[str]]:
    result = [list(line.strip()) for line in fileinput.input()]
    return result


def seat_list_to_tuple(data: typing.Iterable[typing.Iterable[str]]) -> typing.Tuple[typing.Tuple[str]]:
    new_data = []
    for row in data:
        new_data.append(tuple(row))
    return tuple(new_data)


def seat_list_to_list(data: typing.Iterable[typing.Iterable[str]]) -> typing.List[typing.List[str]]:
    new_data = []
    for row in data:
        new_data.append(list(row))
    return list(new_data)


def display(data: typing.Iterable[typing.Iterable[str]]) -> None:
    for row in data:
        print("".join(row))
    print()


# @functools.cache
def char_at_point(data: typing.Iterable[typing.Iterable[str]], x: int, y: int) -> typing.Optional[str]:
    if x < 0 or y < 0:
        return None
    elif x >= len(data[0]) or y >= len(data):
        return None
    # print(f"x {x} y {y} len(data[0] {len(data[0])} len(data) {len(data)}")
    return data[y][x]


@functools.cache
def occupied_up_q(data: typing.Iterable[typing.Iterable[str]], x: int, y: int) -> bool:
    # print(f"debug: {x}, {y}")
    for ys in range(y, -1, -1):
        if (x, ys) == (x, y):
            # print(f"debug2: continuing {x}, {ys}")
            continue
        # print(f"up char at point {x}, {ys} is {char_at_point(data, x, ys)}")
        if is_empty_q(data, x, ys):
            return False
        if is_occupied_q(data, x, ys):
            # print(f"{x}, {ys} occupied")
            return True
    return False


@functools.cache
def occupied_down_q(data: typing.Iterable[typing.Iterable[str]], x: int, y: int) -> bool:
    for ys in range(y, len(data)):
        if (x, ys) == (x, y):
            continue
        # print(f"down char at point {x}, {ys} is {char_at_point(data, x, ys)}")
        if is_empty_q(data, x, ys):
            return False
        if is_occupied_q(data, x, ys):
            # print(f"{x}, {ys} occupied")
            return True
    return False


@functools.cache
def occupied_left_q(data: typing.Iterable[typing.Iterable[str]], x: int, y: int) -> bool:
    for xs in range(x, -1, -1):
        if (xs, y) == (x, y):
            continue
        # print(f"left char at point {xs}, {y} is {char_at_point(data, xs, y)}")
        if is_empty_q(data, xs, y):
            return False
        if is_occupied_q(data, xs, y):
            # print(f"{xs}, {y} occupied")
            return True
    return False


@functools.cache
def occupied_right_q(data: typing.Iterable[typing.Iterable[str]], x: int, y: int) -> bool:
    for xs in range(x, len(data[0])):
        if (xs, y) == (x, y):
            continue
        # print(f"right char at point {xs}, {y} is {char_at_point(data, xs, y)}")
        if is_empty_q(data, xs, y):
            return False
        if is_occupied_q(data, xs, y):
            # print(f"{xs}, {y} occupied")
            return True
    return False


# @functools.cache
def occupied_up_left_q(data: typing.Iterable[typing.Iterable[str]], x: int, y: int) -> bool:
    xs = x - 1
    ys = y - 1
    while True:
        # print(f"up-left char at point {xs}, {ys} is {char_at_point(data, xs, ys)}")
        if char_at_point(data, xs, ys) is None:
            return False
        elif is_empty_q(data, xs, ys):
            return False
        elif is_occupied_q(data, xs, ys):
            return True
        xs = xs - 1
        ys = ys - 1


# @functools.cache
def occupied_up_right_q(data: typing.Iterable[typing.Iterable[str]], x: int, y: int) -> bool:
    xs = x + 1
    ys = y - 1
    while True:
        # print(f"up-right char at point {xs}, {ys} is {char_at_point(data, xs, ys)}")
        if char_at_point(data, xs, ys) is None:
            return False
        elif is_empty_q(data, xs, ys):
            return False
        elif is_occupied_q(data, xs, ys):
            return True
        xs = xs + 1
        ys = ys - 1


# @functools.cache
def occupied_down_right_q(data: typing.Iterable[typing.Iterable[str]], x: int, y: int) -> bool:
    xs = x + 1
    ys = y + 1
    while True:
        # print(f"down-right char at point {xs}, {ys} is {char_at_point(data, xs, ys)}")
        if char_at_point(data, xs, ys) is None:
            return False
        elif is_empty_q(data, xs, ys):
            return False
        elif is_occupied_q(data, xs, ys):
            return True
        xs = xs + 1
        ys = ys + 1


# @functools.cache
def occupied_down_left_q(data: typing.Iterable[typing.Iterable[str]], x: int, y: int) -> bool:
    xs = x - 1
    ys = y + 1
    while True:
        # print(f"down-right char at point {xs}, {ys} is {char_at_point(data, xs, ys)}")
        if char_at_point(data, xs, ys) is None:
            return False
        elif is_empty_q(data, xs, ys):
            return False
        elif is_occupied_q(data, xs, ys):
            return True
        xs = xs - 1
        ys = ys + 1


FUNCLIST = [
    occupied_up_q, occupied_down_q, occupied_left_q, occupied_right_q,
    occupied_up_left_q, occupied_up_right_q,
    occupied_down_right_q, occupied_down_left_q
]


def count_occupied_around(data: typing.Iterable[typing.Iterable[str]], x: int, y: int) -> int:
    # return sum([1 for func in FUNCLIST if func(data, x, y)])
    result = []
    for func in FUNCLIST:
        result.append(func(data, x, y))
    # print(f"counts: {repr(result)}")
    return sum([1 for r in result if r])


def is_empty_q(data: typing.Iterable[typing.Iterable[str]], x: int, y: int) -> int:
    value = char_at_point(data, x, y)
    if value == EMPTY:
        return True
    return False


def is_occupied_q(data: typing.Iterable[typing.Iterable[str]], x: int, y: int) -> int:
    value = char_at_point(data, x, y)
    if value == OCCUPIED:
        return True
    return False


def is_floor_q(data: typing.Iterable[typing.Iterable[str]], x: int, y: int) -> int:
    value = char_at_point(data, x, y)
    if value == FLOOR:
        return True
    return False


def iterate(data: typing.Tuple[typing.Tuple[str]]) -> typing.List[typing.List[str]]:
    new_data = seat_list_to_list(data)
    for y, row in enumerate(data):
        for x, _ in enumerate(data[y]):
            if is_floor_q(data, x, y):
                # print(f"setting {data[y][x]} to floor")
                new_data[y][x] = FLOOR
            elif is_occupied_q(data, x, y) and count_occupied_around(data, x, y) >= 5:
                # print(f"setting {data[y][x]} to empty because {count_occupied_around(data, x, y)} >= 4")
                new_data[y][x] = EMPTY
            elif is_empty_q(data, x, y) and count_occupied_around(data, x, y) == 0:
                # print(f"setting {data[y][x]} to occupied because {count_occupied_around(data, x, y)} == 0")
                new_data[y][x] = OCCUPIED
            else:
                # print(f"not changing {data[y][x]} is_empty_q gives {is_empty_q(data, x, y)}"
                #       f" count_occupied_around(data, x, y) gives {count_occupied_around(data, x, y)}")
                new_data[y][x] = data[y][x]
    return new_data


def main() -> None:
    data = gather()
    # display(data)

    iterations = 0
    while True:
        iterations += 1
        tdata = seat_list_to_tuple(data)
        new_data = iterate(tdata)
        # display(new_data)
        if new_data == data:
            tally = 0
            for y, row in enumerate(new_data):
                for x, _ in enumerate(new_data[y]):
                    if is_occupied_q(new_data, x, y):
                        tally += 1
            print(f"result: {tally}")
            break
        data = new_data


def test1():
    data = """.......#.
...#.....
.#.......
.........
..#L....#
....#....
.........
#........
...#....."""
    result = [list(line) for line in data.splitlines()]
    display(result)
    if count_occupied_around(result, 3, 4) != 8:
        print(f"first test failed. Should be 8, got {count_occupied_around(result, 3, 4)}")


def test2():
    data = """.............
.L.L.#.#.#.#.
............."""
    result = [list(line) for line in data.splitlines()]
    display(result)
    if count_occupied_around(result, 1, 1) != 1:
        print(f"second test failed. Should be 1, got {count_occupied_around(result, 1, 1)}")


def test3():
    data = """.##.##.
#.#.#.#
##...##
...L...
##...##
#.#.#.#
.##.##."""
    result = [list(line) for line in data.splitlines()]
    display(result)
    if count_occupied_around(result, 3, 3) != 0:
        print(f"third test failed. Should be 0, got {count_occupied_around(result, 3, 3)}")


def test4():
    data = """#.##.##.##
#######.##
#.#.#..#..
####.##.##
#.##.##.##
#.#####.##
..#.#.....
##########
#.######.#
#.#####.##"""
    result = [list(line) for line in data.splitlines()]
    display(result)
    if count_occupied_around(result, 9, 1) != 5:
        print(f"fourth-1 test failed. Should be 5, got {count_occupied_around(result, 9, 1)}")
    if count_occupied_around(result, 2, 0) != 5:
        print(f"fourth-2 test failed. Should be 5, got {count_occupied_around(result, 2, 0)}")


def test5():
    data = """#.LL.LL.L#
#LLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLL#
#.LLLLLL.L
#.LLLLL.L#"""
    result = [list(line) for line in data.splitlines()]
    display(result)
    if count_occupied_around(result, 3, 0) != 2:
        print(f"fifth-1 test failed. Should be 2, got {count_occupied_around(result, 3, 0)}")
    if count_occupied_around(result, 5, 0) != 2:
        print(f"fifth-2 test failed. Should be 2, got {count_occupied_around(result, 5, 0)}")
    if count_occupied_around(result, 6, 1) != 1:
        print(f"fourth-3 test failed. Should be 1, got {count_occupied_around(result, 6, 1)}")


def test6():
    """broken???"""
    data = """#.LL.LL.L#
#LLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLL#
#.LLLLLL.L
#.LLLLL.L#"""
    result = [list(line) for line in data.splitlines()]
    display(result)
    new_result = iterate(result)
    display(result)
    display(new_result)
    if count_occupied_around(result, 3, 0) != 2:
        print(f"fifth-1 test failed. Should be 2, got {count_occupied_around(result, 3, 0)}")
    if count_occupied_around(result, 5, 0) != 2:
        print(f"fifth-2 test failed. Should be 2, got {count_occupied_around(result, 5, 0)}")
    if count_occupied_around(result, 6, 1) != 1:
        print(f"fourth-3 test failed. Should be 1, got {count_occupied_around(result, 6, 1)}")


if __name__ == "__main__":
    # test1()
    # test2()
    # test3()
    # test4()
    # test5()
    # test6()
    main()
    print("done")
