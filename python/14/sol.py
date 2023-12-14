from __future__ import annotations
from collections import *
from typing import *
from heapq import *
from dataclasses import dataclass
from puzzle import PuzzleContext
from utils import *
import itertools as itt
import functools as ft

Direction = Literal["N", "W", "S", "E"]
DIRS = get_args(Direction)

class Grid:
    def __init__(self, cells: list[list[str]]):
        self._cells = cells
        self._n = len(cells)
        self._m = len(cells[0])

    @classmethod
    def from_str(cls, s: str) -> Grid:
        return Grid([list(r) for r in s.split("\n")])
    
    def rotate_cw(self) -> Grid:
        return Grid([
            list(reversed(col))
            for col in zip(*self._cells)
        ])
    
    def rotate_ccw(self) -> Grid:
        g = self
        for _ in range(3):
            g = g.rotate_cw()
        return g
    
    def slide(self, direction: Direction) -> Grid:
        if direction == "N":
            return self._slide_north()
        i = DIRS.index(direction)
        g = self.rotate_cw()
        g = g.slide(DIRS[i-1])
        return g.rotate_ccw()
    
    def spin(self) -> Grid:
        g = self
        for d in DIRS:
            g = g.slide(d)
        return g
    
    def _slide_north(self) -> Grid:
        # make a copy to not modify the current instance
        g = [list(r) for r in self._cells]
        n = self._n
        m = self._m
        for j in range(m):
            avail_spot = 0
            for i in range(n):
                if g[i][j] == "#":
                    avail_spot = i + 1
                elif g[i][j] == "O":
                    g[avail_spot][j], g[i][j] = g[i][j], g[avail_spot][j]
                    avail_spot += 1
        return Grid(g)
    
    @property
    def total_load(self) -> int:
        ans = 0
        for i in range(self._n):
            for j in range(self._m):
                if self._cells[i][j] == "O":
                    ans += self._n - i
        return ans

    def __str__(self) -> str:
        return "\n".join("".join(r) for r in self._cells)
    
    # Enables using Grids as keys in a dict
    def __hash__(self) -> int:
        return hash(str(self))
    
    def __eq__(self, other) -> bool:
        return str(self) == str(other)

def solve1(g: Grid) -> int:
    return g.slide("N").total_load

def solve2(g: Grid, total_cycles: int) -> int:
    seen: dict[Grid, int] = OrderedDict()
    n_cycles = 0
    seen[g] = 0

    while True:
        g = g.spin()
        if g in seen:
            break
        n_cycles += 1
        seen[g] = n_cycles
    loop_start = seen[g]
    loop_end = n_cycles
    loop_len = loop_end - loop_start + 1
    
    n_cycles_left = (total_cycles - loop_start) % loop_len
    target_dist = loop_start + n_cycles_left
    return list(seen.keys())[target_dist].total_load

with PuzzleContext(year=2023, day=14) as ctx:
    g = Grid.from_str(ctx.data)

    ans1 = solve1(g)
    ctx.submit(1, str(ans1))
    
    ans2 = solve2(g, 1_000_000_000)
    ctx.submit(2, str(ans2))
