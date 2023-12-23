from collections import *
from typing import *
from heapq import *
from dataclasses import dataclass
from puzzle import PuzzleContext
from utils import *
import itertools as itt
import functools as ft

def calc_longest(g, n, m, curr, goal, d=0, visited=set()):
    if curr == goal:
        return 0
    if curr in visited:
        return -10**100
    visited.add(curr)
    i, j = curr
    if not (0 <= i < n and 0 <= j < m):
        return -10**100
    if g[i][j] == "#":
        return -10**100
    ans = -10**100
    if g[i][j] == ".":
        for ii, jj in get_neigh_coords(g, i, j, DIRS_4):
            ans = max(ans, calc_longest(g, n, m, (ii, jj), goal,d+1, visited))
    elif g[i][j] == "v":
        ans = max(ans, calc_longest(g, n, m, (i+1, j), goal,d+1, visited))
    elif g[i][j] == "^":
        ans = max(ans, calc_longest(g, n, m, (i-1, j), goal,d+1, visited))
    elif g[i][j] == "<":
        ans = max(ans, calc_longest(g, n, m, (i, j-1), goal,d+1, visited))
    elif g[i][j] == ">":
        ans = max(ans, calc_longest(g, n, m, (i, j+1), goal,d+1, visited))
    visited.remove(curr)
    return ans+1

best_so_far3 = 0
def calc_longest3(adj, curr, goal, d=0, visited=set()):
    if curr == goal:
        global best_so_far3
        if d > best_so_far3:
            best_so_far3 = d
            print("reached goal in ", d)
        return d
    visited.add(curr)
    ans = -10**100
    for v, dd in adj[curr]:
        if v in visited:
            continue
        ans = max(ans, calc_longest3(adj, v, goal, d+dd, visited))
    visited.remove(curr)
    return ans

def find_split_points(g, n, m):
    ans = []
    for j in range(m):
        if g[0][j] == ".":
            ans.append((0, j))
        if g[n-1][j] == ".":
            ans.append((n-1, j))
    for i in range(n):
        for j in range(m):
            if g[i][j] == ".":
                cnt = 0
                for ii, jj in get_neigh_coords(g, i, j,DIRS_4):
                    if g[ii][jj] != "#":
                        cnt += 1
                if cnt > 2:
                    ans.append((i, j))
    return set(ans)

def calc_dist(g, n, m, p1, p2, split_points):
    q = deque()
    dists = dict()
    q.append(p1)
    dists[p1] = 0
    while q:
        u = q.popleft()
        if u == p2:
            return dists[u]
        if u != p1 and  u in split_points:
            continue
        neighs = []
        i, j = u
        for ii, jj in get_neigh_coords(g, i, j, DIRS_4):
            if (ii, jj) in dists:
                continue
            if not (0 <= ii < n and 0 <= jj < m):
                continue
            if g[ii][jj] == "#":
                continue
            neighs.append((ii, jj))
        if len(neighs) == 0:
            assert False
        elif len(neighs) == 1:
            dists[neighs[0]] = dists[u] + 1
            q.append(neighs[0])
        else:
            if u == p1:
                for v in neighs:
                    dists[v] = dists[u] + 1
                    q.append(v)
            else:
                return None
    return None

def solve1(data: str) -> int:
    g, n, m = to_grid(data)

    start, goal = None, None
    for j in range(m):
        if g[0][j] == ".":
            start = (0, j)
        if g[n-1][j] == ".":
            goal = (n-1, j)
    assert start is not None 
    assert goal is not None

    return calc_longest(g, n, m, start, goal)

def solve2(data: str) -> int:
    g, n, m = to_grid(data)
    splits = find_split_points(g, n, m)
    adj = defaultdict(lambda: [])
    for a in splits:
        for b in splits:
            if a != b:
                d = calc_dist(g, n, m, a, b, splits)
                if d is not None:
                    adj[a].append((b, d))


    start, goal = None, None
    for j in range(m):
        if g[0][j] == ".":
            start = (0, j)
        if g[n-1][j] == ".":
            goal = (n-1, j)
    assert start is not None 
    assert goal is not None
    return calc_longest3(adj, start, goal)

with PuzzleContext(year=2023, day=23) as ctx:
    ans1 = solve1(ctx.data)
    ctx.submit(1, str(ans1))

    ans2 = solve2(ctx.data)
    ctx.submit(2, str(ans2))
