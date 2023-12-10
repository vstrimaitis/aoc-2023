from collections import *
from typing import *
from heapq import *
from dataclasses import dataclass
from puzzle import PuzzleContext
from utils import *
import itertools as itt
import functools as ft

def is_vertical(adjs, i, j):
    return (i-1, j) in adjs # or (i+1, j) in adjs

with PuzzleContext(year=2023, day=10) as ctx:
    ans1, ans2 = None, None

    g, n, m = to_grid(ctx.data)
    adj = [[[] for j in range(m)] for i in range(n)]
    for i in range(n):
        for j in range(m):
            match g[i][j]:
                case "|":
                    dirs = [(-1, 0), (1, 0)]
                case "-":
                    dirs = [(0, -1), (0, 1)]
                case "L":
                    dirs = [(-1, 0), (0, 1)]
                case "J":
                    dirs = [(-1, 0), (0, -1)]
                case "7":
                    dirs = [(1, 0), (0, -1)]
                case "F":
                    dirs = [(1, 0), (0, 1)]
                case _:
                    continue
            adj[i][j] = get_neigh_coords(g, i, j, dirs)
    
    start_pos = None
    for i in range(n):
        for j in range(m):
            if g[i][j] == "S":
                for ii, jj in get_neigh_coords(g, i, j, DIRS_4):
                    if (i, j) in adj[ii][jj]:
                        adj[i][j].append((ii, jj))
                start_pos = (i, j)
                break

    real_adj = [[[] for j in range(m)] for i in range(n)]
    for i in range(n):
        for j in range(m):
            for ii, jj in adj[i][j]:
                if (i, j) in adj[ii][jj]:
                    real_adj[i][j].append((ii, jj))
    adj = real_adj
    assert start_pos is not None

    import networkx as nx

    indices = dict()
    rindices = dict()
    for i in range(n):
        for j in range(m):
            idx = len(indices)
            indices[(i, j)] = idx
            rindices[idx] = (i, j)
    edge_list = []
    for i in range(n):
        for j in range(m):
            for ii, jj in adj[i][j]:
                edge_list.append((indices[(i, j)], indices[(ii, jj)]))
    G = nx.Graph(edge_list)
    c = nx.find_cycle(G, source=indices[start_pos], orientation=None)
    ans1 = len(c)//2

    ctx.submit(1, str(ans1) if ans1 else None)

    # print(c)
    gg = [["." for j in range(m)] for i in range(n)]
    for idx, _ in c:
        i, j = rindices[idx]
        gg[i][j] = "X"

    cycle_nodes = set(rindices[idx] for idx, _ in c)
    ans2 = 0
    for i in range(n):
        intersections = 0
        for j in range(m):
            if (i, j) in cycle_nodes:
                if g[i][j] in "|JL" or (g[i][j] == "S" and is_vertical(adj[i][j], i, j)):
                    intersections += 1
                continue
            if intersections % 2 == 1:
                ans2 += 1
                gg[i][j] = "I"
    
    # for r in gg:
    #     print("".join(r))

    ctx.submit(2, str(ans2) if ans2 else None)
