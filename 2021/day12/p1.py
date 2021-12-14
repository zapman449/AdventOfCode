#!/usr/bin/env python3

import collections
import copy
import fileinput
import pprint
import re
import statistics
import sys
import typing


counter = 0


def multi_visit(input: str) -> bool:
    if re.match(r"[A-Z][A-Z]*", input):
        return True
    return False


def dfs(visited: typing.List[str], graph: typing.Dict[str, typing.Set[str]], node: str, terminus: str):
    global counter
    if node == terminus:
        print(f"{repr(visited + [node])}")
        counter += 1
    elif node not in visited or multi_visit(node):
        temp_visited = copy.copy(visited)
        temp_visited.append(node)
        for neighbor in graph[node]:
            dfs(temp_visited, graph, neighbor, terminus)


def main() -> None:
    global counter
    graph: typing.Dict[str, typing.Set[str]] = collections.defaultdict(set)
    paths: typing.List[typing.List[str]] = []
    for line in fileinput.input():
        s, e = line.strip().split('-')
        graph[s].add(e)
        graph[e].add(s)
    # pprint.pprint(graph)
    dfs([], graph, 'start', 'end')
    print(f"paths found is {counter}")


if __name__ == "__main__":
    main()
