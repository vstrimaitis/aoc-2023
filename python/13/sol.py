from collections import *
from typing import *
from heapq import *
from dataclasses import dataclass
from puzzle import PuzzleContext
from utils import *
import itertools as itt
import functools as ft

SymmetryLine = tuple[Literal["H", "V"], int, int]

def get_horizontal_symmetry_lines(grid: list[list[str]]) -> list[int]:
    n = len(grid)
    ans = []
    for i in range(n-1):
        r1 = reversed(range(0, i+1))
        r2 = range(i+1, n)
        if all(grid[x] == grid[y] for x, y in zip(r1, r2)):
            ans.append(i)
    return ans

def get_symmetry_lines(grid: list[list[str]]) -> list[SymmetryLine]:
    h_lines = get_horizontal_symmetry_lines(grid)
    v_lines = get_horizontal_symmetry_lines(list(zip(*grid[::-1])))
    return [
        *map(lambda x: ("H", x, 100*(x+1)), h_lines),
        *map(lambda x: ("V", x, x+1), v_lines),
    ]

def solve1(s: str) -> int:
    g, _, _ = to_grid(s)
    lines = get_symmetry_lines(g)
    return sum(map(lambda x: x[2], lines))

def solve2(s: str) -> int:
    g, n, m = to_grid(s)
    lines = set(get_symmetry_lines(g))
    for i in range(n):
        for j in range(m):
            c = g[i][j]
            g[i][j] = "." if c == "#" else "#"
            new_lines = set(get_symmetry_lines(g))
            if diff := new_lines - lines:
                assert len(diff) == 1
                return list(diff)[0][2]
            g[i][j] = c
    assert False


with PuzzleContext(year=2023, day=13) as ctx:
    ans1 = sum(map(solve1, ctx.groups))
    ctx.submit(1, str(ans1))

    ans2 = sum(map(solve2, ctx.groups))
    ctx.submit(2, str(ans2))
