from collections import *
from typing import *
from heapq import *
from dataclasses import dataclass
from puzzle import PuzzleContext
from utils import *
import itertools as itt
import functools as ft

Grid = list[list[str]]
Coord = tuple[int, int]
AdjacencyList = dict[Coord, list[tuple[Coord, int]]]

def get_size(g: Grid) -> tuple[int, int]:
    return len(g), len(g[0])

def calc_longest(
    adj: AdjacencyList,
    curr: Coord,
    goal: Coord,
    d: int = 0,
    visited: set[Coord] = set()
) -> int:
    if curr == goal:
        return d
    visited.add(curr)
    ans = -10**100
    for v, dd in adj[curr]:
        if v in visited:
            continue
        ans = max(ans, calc_longest(adj, v, goal, d+dd, visited))
    visited.remove(curr)
    return ans

def get_next_coords(g: Grid, i: int, j: int) -> list[Coord]:
    n, m = get_size(g)
    ans = []
    match g[i][j]:
        case "#": ans = []
        case ".": ans = [(i+di, j+dj) for (di, dj) in DIRS_4]
        case "v": ans = [(i+1, j)]
        case "^": ans = [(i-1, j)]
        case "<": ans = [(i, j-1)]
        case ">": ans = [(i, j+1)]
        case _: assert False
    return [
        (ii, jj)
        for ii, jj in ans
        if 0 <= ii < n and 0 <= jj < m and g[ii][jj] != "#"
    ]

def find_split_points(g: Grid) -> set[Coord]:
    n, m = get_size(g)
    ans = []
    for i in range(n):
        for j in range(m):
            if g[i][j] == "#":
                continue
            if i in (0, n-1) or len(get_next_coords(g, i, j)) >= 3:
                ans.append((i, j))
    return set(ans)

def calc_dist(g: Grid, p1: Coord, p2: Coord, split_points: set[Coord]) -> int | None:
    q = deque()
    dists = dict()

    q.append(p1)
    dists[p1] = 0
    while q:
        u = q.popleft()
        if u == p2:
            return dists[u]
        if u != p1 and u in split_points:
            continue
        for v in get_next_coords(g, *u):
            if v not in dists:
                dists[v] = dists[u] + 1
                q.append(v)
    return None

def solve(data: str) -> int:
    g, n, m = to_grid(data)
    splits = find_split_points(g)
    start = [p for p in splits if p[0] == 0][0]
    goal = [p for p in splits if p[0] == n-1][0]

    adj = defaultdict(lambda: [])
    for a in splits:
        for b in splits:
            if a == b:
                continue
            if (d := calc_dist(g, a, b, splits)) is not None:
                adj[a].append((b, d))

    return calc_longest(adj, start, goal)

with PuzzleContext(year=2023, day=23) as ctx:
    ans1 = solve(ctx.data)
    ctx.submit(1, str(ans1))

    t = str.maketrans({c: "." for c in "><v^"})
    ans2 = solve(ctx.data.translate(t))
    ctx.submit(2, str(ans2))
