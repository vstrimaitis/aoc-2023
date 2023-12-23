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

best_so_far = 0
def calc_longest2(g, n, m, curr, goal, d=0, visited=set()):
    if curr == goal:
        global best_so_far
        if d > best_so_far:
            best_so_far = d
            print("reached goal in ", d)
        return d
    if curr in visited:
        return -10**100
    visited.add(curr)
    i, j = curr
    if not (0 <= i < n and 0 <= j < m):
        return -10**100
    if g[i][j] == "#":
        return -10**100
    ans = -10**100
    for ii, jj in get_neigh_coords(g, i, j, DIRS_4):
        ans = max(ans, calc_longest2(g, n, m, (ii, jj), goal,d+1, visited))
    visited.remove(curr)
    return ans
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

def condense(g, n, m, curr, goal, pc, adj, d=0, p=(-1,-1), visited=set()):
    if curr == goal:
        adj[curr].append((pc, d))
        adj[pc].append((curr, d))
        return
    neighs = []
    visited.add(curr)
    i, j = curr
    for ii, jj in get_neigh_coords(g, i, j, DIRS_4):
        if (ii, jj) == p:
            continue
        if not (0 <= ii < n and 0 <= jj < m):
            continue
        if g[ii][jj] == "#":
            continue
        if (ii, jj) in visited:
            continue
        neighs.append((ii, jj))
    if len(neighs) == 0:
        return -10**100
    elif len(neighs) == 1:
        condense(g, n, m, neighs[0], goal, pc, adj, d+1, curr)
    else:
        # found choke point
        adj[pc].append((curr, d))
        adj[curr].append((pc, d))
        for neigh in neighs:
            condense(g, n, m, neigh, goal, curr, adj, 1, curr)
    visited.remove(curr)


with PuzzleContext(year=2023, day=23) as ctx:
    ans1, ans2 = None, None

    g, n, m = to_grid(ctx.data)

    start, goal = None, None
    for j in range(m):
        if g[0][j] == ".":
            start = (0, j)
        if g[n-1][j] == ".":
            goal = (n-1, j)
    assert start is not None 
    assert goal is not None

    # ans1 = calc_longest(g, n, m, start, goal)
    # print(ans1)

    # ctx.submit(1, str(ans1) if ans1 else None)

    # ans2 = calc_longest2(g, n, m, start, goal)
    # ctx.submit(2, str(ans2) if ans2 else None)  # <- this finished after a long time

    # for i in range(n):
    #     for j in range(m):
    #         if g[i][j] == ".":
    #             cnt = 0
    #             for ii, jj in get_neigh_coords(g, i, j,DIRS_4):
    #                 if g[ii][jj] != "#":
    #                     cnt += 1
    #             if cnt > 2:
    #                 print(i, j)
    #                 for ii in range(i-1, i+2):
    #                     for jj in range(j-1, j+2):
    #                         print(g[ii][jj],end="")
    #                     print()
    #                 print()

    adj = defaultdict(lambda: [])
    condense(g, n, m, start, goal, start, adj)
    for k, v in adj.items():
        print(k, v)
    ans2 = calc_longest3(adj, start, goal)
    print(ans2)


    # new_adj = defaultdict(lambda: [])
    # seen = set()
    # for u, vs in adj.items():
    #     seen.add(u)
    #     for v in vs:
    #         if v in seen:
    #             continue
    #         new_adj[u].add(v)
    