from collections import *
from typing import *
from heapq import *
from dataclasses import dataclass
from puzzle import PuzzleContext
from utils import *
import itertools as itt
import functools as ft

Grid = list[list[str]]
Height = int
Width = int
GridDef = tuple[Grid, Height, Width]
Direction = Literal["N", "W", "S", "E"]

def rotate_cw(g: Grid, n: Height, m: Width) -> GridDef:
    n, m = m, n
    g = [list(reversed(col)) for col in zip(*g)]
    return g, n, m

def rotate_ccw(g: Grid, n: Height, m: Width) -> GridDef:
    for _ in range(3):
        g, n, m = rotate_cw(g, n, m)
    return g, n, m

def slide_n(g: Grid, n: Height, m: Width) -> Grid:
    for j in range(m):
        avail_spot = 0
        for i in range(n):
            if g[i][j] == "#":
                avail_spot = i + 1
            elif g[i][j] == "O":
                g[avail_spot][j], g[i][j] = g[i][j], g[avail_spot][j]
                avail_spot += 1
    return g

def slide(g: Grid, n: Height, m: Width, d: Direction) -> Grid:
    def delegate(to: Direction) -> Grid:
        g2, n2, m2 = rotate_cw(g, n, m)
        g2 = slide(g2, n2, m2, to)
        g2, _, _ = rotate_ccw(g2, n2, m2)
        return g2
    match d:
        case "N": return slide_n([r.copy() for r in g], n, m)
        case "W": return delegate("N")
        case "S": return delegate("W")
        case "E": return delegate("S")
        case _: assert False

def calc_total_load(g: Grid, n: Height, m: Width) -> int:
    ans = 0
    for i in range(n):
        for j in range(m):
            if g[i][j] == "O":
                ans += n-i
    return ans

def solve1(g: Grid, n: Height, m: Width) -> int:
    g = slide(g, n, m, "N")
    return calc_total_load(g, n, m)

def solve2(g: Grid, n: Height, m: Width, total_cycles: int) -> int:
    def do_cycle(gr: Grid) -> Grid:
        for d in ("N", "W", "S", "E"):
            gr = slide(gr, n, m, d)
        return gr
    
    def to_str(g: Grid) -> str:
        return "\n".join("".join(r) for r in g)
    
    seen = dict()
    loads = []
    n_cycles = 0

    seen[to_str(g)] = 0
    loads.append(calc_total_load(g, n, m))

    while True:
        g = do_cycle(g)
        s = to_str(g)
        if s in seen:
            break
        n_cycles += 1
        seen[s] = n_cycles
        loads.append(calc_total_load(g, n, m))
    loop_start = seen[to_str(g)]
    loop_end = n_cycles
    loop_len = loop_end - loop_start + 1
    
    n_cycles_left = (total_cycles - loop_start) % loop_len
    target_dist = loop_start + n_cycles_left
    return loads[target_dist]

with PuzzleContext(year=2023, day=14) as ctx:
    g, n, m = to_grid(ctx.data)

    ans1 = solve1(g, n, m)
    ctx.submit(1, str(ans1))
    
    ans2 = solve2(g, n, m, 1_000_000_000)
    ctx.submit(2, str(ans2))
