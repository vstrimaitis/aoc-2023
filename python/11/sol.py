from collections import *
from typing import *
from heapq import *
from dataclasses import dataclass
from puzzle import PuzzleContext
from utils import *
import itertools as itt
import functools as ft

def find_sp(g: list[list[str]], src, dst):
    return abs(dst[0]-src[0]) + abs(dst[1]-src[1])

with PuzzleContext(year=2023, day=11) as ctx:
    ans1, ans2 = None, None
    g, n, m = to_grid(ctx.data)

    empty_rows = set()
    empty_cols = set()

    for i in range(n):
        if all(g[i][j] == "." for j in range(m)):
            empty_rows.add(i)
    for j in range(m):
        if all(g[i][j] == "." for i in range(n)):
            empty_cols.add(j)

    # gg = []
    # for i in range(n):
    #     r = []
    #     for j in range(m):
    #         r.append(g[i][j])
    #         if j in empty_cols:
    #             r.append(g[i][j])
    #     gg.append(r)
    #     if i in empty_rows:
    #         gg.append(r.copy())
            
    # g = gg.copy()
    # n = len(g)
    # m = len(g[0])

    galaxies = []
    for i in range(n):
        for j in range(m):
            if g[i][j] == "#":
                galaxies.append((i, j))

    MULT = 1000000
    ans1 = 0
    galaxies = sorted(galaxies) 
    for a in galaxies:
        for b in galaxies:
            if a < b:
                row_range = (min(a[0], b[0]), max(a[0], b[0]))
                col_range = (min(a[1], b[1]), max(a[1], b[1]))
                cnt_r = 0
                for i in empty_rows:
                    if row_range[0] <= i <= row_range[1]:
                        cnt_r += 1
                        
                cnt_c = 0
                for j in empty_cols:
                    if col_range[0] <= j <= col_range[1]:
                        cnt_c += 1
                
                dr = abs(a[0]-b[0])
                dc = abs(a[1]-b[1])
                ans1 += cnt_r*MULT+(dr-cnt_r) + cnt_c*MULT+(dc-cnt_c)
    ctx.submit(2, str(ans1))
