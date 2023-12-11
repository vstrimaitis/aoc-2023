from collections import *
from typing import *
from heapq import *
from dataclasses import dataclass
from puzzle import PuzzleContext
from utils import *
import itertools as itt
import functools as ft

def count(values: set[int], a: int, b: int) -> int:
    if a > b:
        a, b = b, a
    ans = 0
    for x in values:
        if a <= x <= b:
            ans += 1
    return ans

def calc(galaxy_positions: list[Tuple[int, int]], empty_rows: set[int], empty_cols: set[int], expansion_multiplier: int) -> int:
    ans = 0
    for i, a in enumerate(galaxy_positions):
        for j, b in enumerate(galaxy_positions):
            if j <= i:
                continue
            empty_r = count(empty_rows, a[0], b[0])
            diff_r = abs(a[0] - b[0])
            dist_r = diff_r + empty_r*(expansion_multiplier-1)

            empty_c = count(empty_cols, a[1], b[1])
            diff_c = abs(a[1] - b[1])
            dist_c = diff_c + empty_c*(expansion_multiplier-1)

            ans += dist_r + dist_c

    return ans


    pass

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

    galaxies = []
    for i in range(n):
        for j in range(m):
            if g[i][j] == "#":
                galaxies.append((i, j))

    ans1 = calc(galaxies, empty_rows, empty_cols, 2)
    ctx.submit(1, str(ans1))

    ans2 = calc(galaxies, empty_rows, empty_cols, 1000000)
    ctx.submit(2, str(ans2))
