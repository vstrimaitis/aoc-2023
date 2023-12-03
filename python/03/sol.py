from __future__ import annotations
from collections import *
from typing import *
from heapq import *
from dataclasses import dataclass, field
from puzzle import PuzzleContext
from utils import *
import itertools as itt
import functools as ft
import re

Coords = Tuple[int, int]

@dataclass
class Symbol:
    value: str
    coords: Coords

@dataclass
class Number:
    value: int
    coords: Coords
    adjacent_symbols: list[Symbol] = field(default_factory=lambda: [])

    @classmethod
    def from_position(cls, grid: list[str], row: int, col: int, value: int) -> Number:
        coords = (row, col)
        col_end = col+len(str(value))-1
        number_coords = set([(row, j) for j in range(col, col_end+1)])
        adj_coords = [
            (i, j)
            for i in range(row-1, row+2)
            for j in range(col-1, col_end+2)
            if (
                0 <= i < len(grid) and
                0 <= j < len(grid[i]) and
                (i, j) not in number_coords
            )
        ]
        adj_symbols = []
        for (i, j) in adj_coords:
            c = grid[i][j]
            if c not in ".0123456789":
                adj_symbols.append(Symbol(c, (i, j)))
        return Number(value, coords, adj_symbols)

def extract_numbers(grid: list[str]) -> list[Number]:
    nums = []
    for i, line in enumerate(grid):
        for m in re.finditer(r"\d+", line):
            nums.append(Number.from_position(grid, i, m.span()[0], int(m.group(0))))
    return nums

with PuzzleContext(year=2023, day=3) as ctx:
    ans1, ans2 = None, None

    numbers = extract_numbers(ctx.nonempty_lines)
    
    ans1 = sum(
        num.value
        for num in numbers
        if len(num.adjacent_symbols) > 0
    )

    groups = defaultdict(lambda: [])
    for num in numbers:
        for symbol in num.adjacent_symbols:
            if symbol.value == "*":
                groups[symbol.coords].append(num.value)
    ans2 = sum(
        g[0] * g[1]
        for g in groups.values()
        if len(g) == 2
    )

    ctx.submit(1, str(ans1) if ans1 else None)
    ctx.submit(2, str(ans2) if ans2 else None)
