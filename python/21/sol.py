from collections import *
from typing import *
from heapq import *
from dataclasses import dataclass
from puzzle import PuzzleContext
from utils import *
import itertools as itt
import functools as ft

def solve(g: list[str], target_count: int) -> int:
    n = len(g)
    m = len(g[0])
    start = None
    for i in range(n):
        for j in range(m):
            if g[i][j] == "S":
                start = (i, j)
    assert start is not None

    modulo_counts = []
    d = 0
    boundary = set([start])
    while True:
        if d == target_count:
            return len(boundary)
        if len(modulo_counts) == 3:
            a0, a1, a2 = modulo_counts
            b0 = a0
            b1 = a1-a0
            b2 = a2-a1
            n_cycles = target_count // n
            return b0 + b1*n_cycles + (n_cycles*(n_cycles-1)//2)*(b2-b1)
        d += 1
        new_boundary = set()
        for i, j in boundary:
            for di, dj in DIRS_4:
                ii = i + di
                jj = j + dj
                if g[ii%n][jj%m] != "#":
                    new_boundary.add((ii, jj))
        boundary = new_boundary
        if d % n == target_count % n:
            modulo_counts.append(len(boundary))

with PuzzleContext(year=2023, day=21) as ctx:

    g = ctx.lines
    ans1 = solve(g, 64)
    ctx.submit(1, str(ans1))

    ans2 = solve(g, 26501365)
    ctx.submit(2, str(ans2))
