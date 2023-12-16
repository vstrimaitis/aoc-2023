from collections import *
from typing import *
from heapq import *
from dataclasses import dataclass
from puzzle import PuzzleContext
from utils import *
import itertools as itt
import functools as ft

Tile = Literal[".", "/", "\\", "|"]
Dir = Literal[">", "<", "^", "v"]
Grid = list[list[Tile]]
State = tuple[int, int, Dir]

def dfs(g: Grid, n: int, m: int, u: State, visited: set[State]) -> None:
    i, j, d = u
    if u in visited:
        return
    if i < 0 or i >= n or j < 0 or j >= m:
        return
    visited.add(u)
    match g[i][j]:
        case ".":
            match d:
                case ">": dfs(g, n, m, (i, j+1, ">"), visited)
                case "<": dfs(g, n, m, (i, j-1, "<"), visited)
                case "^": dfs(g, n, m, (i-1, j, "^"), visited)
                case "v": dfs(g, n, m, (i+1, j, "v"), visited)
                case _: assert False
        case "|":
            match d:
                case ">":
                    dfs(g, n, m, (i-1, j, "^"), visited)
                    dfs(g, n, m, (i+1, j, "v"), visited)
                case "<":
                    dfs(g, n, m, (i-1, j, "^"), visited)
                    dfs(g, n, m, (i+1, j, "v"), visited)
                case "^": dfs(g, n, m, (i-1, j, "^"), visited)
                case "v": dfs(g, n, m, (i+1, j, "v"), visited)
                case _: assert False
        case "-":
            match d:
                case ">": dfs(g, n, m, (i, j+1, ">"), visited)
                case "<": dfs(g, n, m, (i, j-1, "<"), visited)
                case "^":
                    dfs(g, n, m, (i, j-1, "<"), visited)
                    dfs(g, n, m, (i, j+1, ">"), visited)
                case "v":
                    dfs(g, n, m, (i, j-1, "<"), visited)
                    dfs(g, n, m, (i, j+1, ">"), visited)
                case _: assert False
        case "/":
            match d:
                case ">": dfs(g, n, m, (i-1, j, "^"), visited)
                case "<": dfs(g, n, m, (i+1, j, "v"), visited)
                case "^": dfs(g, n, m, (i, j+1, ">"), visited)
                case "v": dfs(g, n, m, (i, j-1, "<"), visited)
                case _: assert False
        case "\\":
            match d:
                case ">": dfs(g, n, m, (i+1, j, "v"), visited)
                case "<": dfs(g, n, m, (i-1, j, "^"), visited)
                case "^": dfs(g, n, m, (i, j-1, "<"), visited)
                case "v": dfs(g, n, m, (i, j+1, ">"), visited)
                case _: assert False
        case _: assert False

def count_energized_tiles(grid: Grid, n: int, m: int, start: State) -> int:
    visited = set()
    dfs(grid, n, m, start, visited)
    return len(set((i, j) for i, j, _ in visited))

with PuzzleContext(year=2023, day=16) as ctx:
    ans1, ans2 = None, None

    g, n, m = to_grid(ctx.data)
    g = cast(Grid, g)

    ans1 = count_energized_tiles(g, n, m, (0, 0, ">"))
    ctx.submit(1, str(ans1) if ans1 else None)

    starts = [
        (0, 0, ">"),
        (0, 0, "v"),
        (0, m-1, "v"),
        (0, m-1, "<"),
        (n-1, 0, ">"),
        (n-1, 0, "^"),
        (n-1, m-1, "^"),
        (n-1, m-1, "<"),
    ]
    for i in range(1, n-1):
        starts.append((i, 0, ">"))
        starts.append((i, m-1, "<"))
        
    for j in range(1, m-1):
        starts.append((0, j, "v"))
        starts.append((n-1, j, "^"))

    ans2 = max(map(lambda s: count_energized_tiles(g, n, m, s), starts))
    ctx.submit(2, str(ans2) if ans2 else None)
