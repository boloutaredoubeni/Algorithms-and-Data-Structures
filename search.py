#!/usr/bin/env python3
import math
from collections import deque


def linear_search(xs, val):
    for i, x in enumerate(xs):
        if x == val:
            return i
    return -1


def binary_search(xs, val):
    lo = 0
    hi = len(xs) - 1
    while lo <= hi:
        i = (lo + hi) // 2
        if xs[i] == val:
            return i
        elif xs[i] > val:
            hi = i - 1
        else:
            lo = i + 1
    return -1


def dfs_recur(graph, start_vertex):
    visited = []

    def dfs(g, v):
        visited.append(v)
        for u in graph.get(v, []):
            if u not in visited:
                dfs(g, u)

    dfs(graph, start_vertex)

    return visited


def dfs_iter(graph, vertex):
    visited = []
    stack = [vertex]
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.append(vertex)
            for u in graph.get(vertex, []):
                stack.append(u)

    return visited


def pre_order_recur(tree):
    visited = []

    def pre_order(node):
        if not node:
            return
        visited.append(node.data)
        pre_order(node.left)
        pre_order(node.right)

    pre_order(tree)
    return visited


def pre_order_iter(tree):
    if not tree:
        return

    visited = []
    stack = [tree]
    while stack:
        node = stack.pop()
        visited.append(node.data)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)

    return visited


def in_order_recur(tree):
    visited = []

    def in_order(node):
        if not node:
            return

        in_order(node.left)
        visited.append(node.data)
        in_order(node.right)

    in_order(tree)
    return visited


def in_order_iter(tree):
    visited = []
    stack = []
    while stack or tree:
        if tree:
            stack.append(tree)
            tree = tree.left
        else:
            tree = stack.pop()
            visited.append(tree.data)
            tree = tree.right

    return visited


def post_order_recur(tree):
    visited = []

    def post_order(node):
        if not tree:
            return

        post_order(node.left)
        post_order(node.right)
        visited.append(node.data)

    post_order(tree)
    return visited


def post_order_iter(tree):
    visited = []
    stack = []
    prev_node = None
    while stack or tree:
        if tree:
            stack.append(tree)
            tree = tree.left
        else:
            peek = stack[-1]
            if peek.right and prev_node != peek.right:
                tree = peek.right
            else:
                visited.append(peek.data)
                prev_node = stack.pop()

    return visited


def bfs_iter(graph, vertex):
    visited = []
    distances = {}
    parents = {}
    for v in graph.keys():
        distances[v] = math.inf
        parents[v] = None

    q = deque()
    q.appendleft(vertex)
    distances[vertex] = 0
    while q:
        current = q.pop()
        visited.append(current)
        for node in graph.get(current, []):
            if distances[node] == math.inf:
                distances[node] = distances[current] + 1
                parents[node] = current
                q.appendleft(node)

    return visited


def bfs_recur(graph, vertex):
    pass


def level_order_iter(tree):
    visited = []
    q = deque()
    q.appendleft(tree)
    while q:
        node = q.pop()
        visited.append(node.data)
        if node.left:
            q.appendleft(node.left)
        if node.right:
            q.appendleft(node.right)


def level_order_recur(tree):
    visited = []

    def level_order(level):
        next_level = []
        for node in level:
            visited.append(node.data)
            if node.left:
                next_level.append(node.left)
            if node.right:
                next_level.append(node.right)

        if next_level:
            level_order(next_level)

    level_order([tree])
    return visited