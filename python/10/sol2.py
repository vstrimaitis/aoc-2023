from __future__ import annotations
from collections import *
from typing import *
from heapq import *
from dataclasses import dataclass
from puzzle import PuzzleContext
from utils import *
import itertools as itt
import functools as ft

EXPANSIONS = {
    "L": [
        ".#.",
        ".##",
        "...",
    ],
    "J": [
        ".#.",
        "##.",
        "...",
    ],
    "7": [
        "...",
        "##.",
        ".#.",
    ],
    "F": [
        "...",
        ".##",
        ".#.",
    ],
    "|": [
        ".#.",
        ".#.",
        ".#.",
    ],
    "-": [
        "...",
        "###",
        "...",
    ],
    ".": [
        "...",
        "...",
        "..."
    ],
    "S": [
        "...",
        ".S.",
        "..."
    ],
}

def fill(g: list[list[str]], i: int, j: int, fill_char: str, walls: set[str]):
    n = len(g)
    m = len(g[0])
    if i < 0 or i >= n or j < 0 or j >= m:
        return
    if g[i][j] in {*walls, fill_char}:
        return
    g[i][j] = fill_char
    for di, dj in DIRS_4:
        fill(g, i+di, j+dj, fill_char, walls)

def find_cycle(
    g: list[list[str]],
    curr: Tuple[int, int],
    goal: Tuple[int, int],
    prev: Tuple[int, int],
    ans: list[Tuple[int, int]]
) -> None:
    ans.append(curr)
    if curr == goal:
        return
    i, j = curr
    for di, dj in DIRS_4:
        ii = i + di
        jj = j + dj
        if (ii, jj) == prev:
            continue
        if ii < 0 or ii >= len(g):
            continue
        if jj < 0 or jj >= len(g[0]):
            continue
        if g[ii][jj] != "#":
            continue
        find_cycle(g, (ii, jj), goal, curr, ans)

def print_grid(g: list[list[str]], msg: str = "") -> None:
    if msg:
        print(msg + ":")
    print("\n".join(["".join(row) for row in g]))
    print()


with PuzzleContext(year=2023, day=10) as ctx:
    grid = lmap(list, ctx.nonempty_lines)
    n = len(grid)
    m = len(grid[0])
    
    new_grid = [["?" for _ in range(3*m)] for _ in range(3*n)]
    start_pos = None
    for i in range(n):
        for j in range(m):
            exp = EXPANSIONS[grid[i][j]]
            if grid[i][j] == "S":
                start_pos = 3*i+1, 3*j+1
            for di in range(3):
                for dj in range(3):
                    new_grid[3*i+di][3*j+dj] = exp[di][dj]
    print_grid(new_grid, "after expansion")

    assert start_pos is not None
    i, j = start_pos
    ends = []
    for di, dj in DIRS_4:
        if new_grid[i+di*2][j+dj*2] == "#":
            ends.append((i+di, j+dj))
    for i, j in ends:
        new_grid[i][j] = "#"
    new_grid[start_pos[0]][start_pos[1]] = "#"

    print_grid(new_grid, "after inferring starting pipe type")
    
    cycle = [start_pos]
    find_cycle(new_grid, ends[0], ends[1], start_pos, cycle)

    ans1 = len(cycle) // 3 // 2
    # ctx.submit(1, str(ans1))

    # mark the cells that form a cycle with "C"
    for i, j in cycle:
        new_grid[i][j] = "C"

    print_grid(new_grid, "after finding and marking the cycle")

    # flood fill from the outside - marks all outside cells with "O"
    fill(new_grid, 0, 0, "O", walls={"C", "#"})
    print_grid(new_grid, "after flood-filling outer cells")

    # flood fill on the cycle - marks all cells within (or on) the cycle with "I"
    fill(new_grid, start_pos[0], start_pos[1], "I", walls={"O"})
    print_grid(new_grid, "after flood-filling inner cells")

    cycle_coords = set(cycle)
    ans2 = 0
    for i in range(n):
        for j in range(m):
            ii = 3*i + 1
            jj = 3*j + 1
            if (ii, jj) in cycle_coords:
                continue
            if new_grid[ii][jj] == "I":
                ans2 += 1
    ctx.submit(2, str(ans2))

