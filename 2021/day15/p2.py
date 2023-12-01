#!/usr/bin/env python3

import collections
import copy
import fileinput
import pprint
import queue
import re
import statistics
import sys
import typing


def grid_plus_x(data: typing.List[typing.List[int]], adder) -> typing.List[typing.List[int]]:
    new_data: typing.List[typing.List[int]] = []
    for idx_y, row in enumerate(data):
        new_data.append([])
        for idx_x, i in enumerate(row):
            if i + adder >= 10:
                new_data[idx_y].append(((i+adder)%10)+1)
            else:
                new_data[idx_y].append(i+adder)
            # if adder == 4 and row[-1] == 5 and row[-2] == 7:
            #     print(f"HELP: i {i}, adder {adder}, sum {i+adder}")
    return new_data


def grid_add_right(data: typing.List[typing.List[int]], to_add_right: typing.List[typing.List[int]], adder: int) -> typing.List[typing.List[int]]:
    data_plus_one = grid_plus_x(to_add_right, adder)
    new_data: typing.List[typing.List[int]] = []
    for idx_y, row in enumerate(data):
        new_data.append(row + data_plus_one[idx_y])
    # print(data[0][-10:])
    # print(data_plus_one[0][-10:])
    # print(new_data[0][-10:])
    return new_data


def grid_add_down(data: typing.List[typing.List[int]], to_add_below: typing.List[typing.List[int]], adder: int) -> typing.List[typing.List[int]]:
    new_data = grid_plus_x(to_add_below, adder)
    return data + new_data


def grid_print(data: typing.List[typing.List[int]]) -> None:
    for row in data:
        print("".join(map(str, row)))


class Graph:
    def __init__(self, num_of_nodes):
        self.v = num_of_nodes
        self.edges = [[-1 for i in range(num_of_nodes)] for j in range(num_of_nodes)]
        self.visited = []

    def add_edge(self, u, v, weight):
        self.edges[u][v] = weight
        self.edges[v][u] = weight


def dijkstra(graph, start_node):
    D = {v: float('inf') for v in range(graph.v)}
    D[start_node] = 0

    pq = queue.PriorityQueue()
    pq.put((0, start_node))

    while not pq.empty():
        (dist, current_vertex) = pq.get()
        graph.visited.append(current_vertex)

        for neighbor in range(graph.v):
            if graph.edges[current_vertex][neighbor] != -1:
                distance = graph.edges[current_vertex][neighbor]
                if neighbor not in graph.visited:
                    old_cost = D[neighbor]
                    new_cost = D[current_vertex] + distance
                    if new_cost < old_cost:
                        pq.put((new_cost, neighbor))
                        D[neighbor] = new_cost
    return D


class Point(typing.NamedTuple):
    x: int
    y: int


def is_point_in(data: typing.List[typing.List[int]], point: Point) -> bool:
    len_x = len(data[0])
    len_y = len(data)
    if point.x >= len_x:
        return False
    if point.y >= len_y:
        return False
    if point.x < 0:
        return False
    if point.y < 0:
        return False
    return True


def p2n(point: Point, len_row: int) -> int:
    return point.x + (len_row * point.y)


def n2p(node: int, len_row: int) -> Point:
    y = node // len_row
    x = node - y
    return Point(x, y)


def main() -> None:
    data: typing.List[typing.List[int]] = []
    for line in fileinput.input():
        row: typing.List[int] = []
        for c in line.strip():
            row.append(int(c))
        data.append(row)

    og_data = copy.copy(data)
    # grid_print(data)
    data = grid_add_right(data, og_data, 1)
    # grid_print(data)
    data = grid_add_right(data, og_data, 2)
    # grid_print(data)
    data = grid_add_right(data, og_data, 3)
    # grid_print(data)
    data = grid_add_right(data, og_data, 4)
    # grid_print(data)

    og_all_right_data = copy.copy(data)
    data = grid_add_down(data, og_all_right_data, 1)
    data = grid_add_down(data, og_all_right_data, 2)
    data = grid_add_down(data, og_all_right_data, 3)
    data = grid_add_down(data, og_all_right_data, 4)

    dx = len(data[0])
    dy = len(data)

    graph = Graph(len(data[0]) * len(data))

    for y_idx, row in enumerate(data):
        for x_idx, value in enumerate(row):
            p = Point(x_idx, y_idx)
            p1 = Point(x_idx+1, y_idx)
            p2 = Point(x_idx, y_idx+1)
            if is_point_in(data, p1):
                graph.add_edge(p2n(p, dx), p2n(p1, dx), data[p1.y][p1.x])
            if is_point_in(data, p2):
                graph.add_edge(p2n(p, dx), p2n(p2, dx), data[p2.y][p2.x])

    d = dijkstra(graph, 0)
    print(f"answer vertex {dx*dy-1} is {d[dx*dy-1]}")
    # print(f"answer vertex {dx*dy} is {d[dx*dy]}")
    print(data[-1][-10:])


if __name__ == "__main__":
    main()
