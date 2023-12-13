from collections import *
from typing import *
from heapq import *
from dataclasses import dataclass
from puzzle import PuzzleContext
from utils import *
import itertools as itt
import functools as ft

def reflect_h(g, n, m):
    lines = []
    for i in range(n-1):
        ok = True
        for d in range(1, n):
            i1 = i-d+1
            i2 = i+d
            if i1 < 0 or i2 >= n:
                break
            if "".join(g[i1]) != "".join(g[i2]):
                ok = False
                break
        if ok:
            lines.append(i)
    return lines
def reflect_v(g, n, m):
    lines = []
    for j in range(m-1):
        ok = True
        cnt = 0
        for d in range(1, m):
            j1 = j-d+1
            j2 = j+d
            if j1 < 0 or j2 >= m:
                break
            cnt += 1
            ok2 = True
            for i in range(n):
                if g[i][j1] != g[i][j2]:
                    ok2 = False
                    break
            if not ok2:
                ok = False
                break
        if ok:
            lines.append(j)
    return lines


def solve_h(g, n, m):
    for i in range(n-1):
        ok = True
        for d in range(1, n):
            i1 = i-d+1
            i2 = i+d
            if i1 < 0 or i2 >= n:
                break
            if "".join(g[i1]) != "".join(g[i2]):
                ok = False
                break
        if ok:
            return i+1
    return None
def solve_v(g, n, m):
    for j in range(m-1):
        ok = True
        cnt = 0
        for d in range(1, m):
            j1 = j-d+1
            j2 = j+d
            if j1 < 0 or j2 >= m:
                break
            cnt += 1
            ok2 = True
            for i in range(n):
                if g[i][j1] != g[i][j2]:
                    ok2 = False
                    break
            if not ok2:
                ok = False
                break
        if ok:
            return j+1
    return None
            

def solve(s: str) -> int:
    g, n, m = to_grid(s)
    if x := solve_v(g, n, m):
        return x
    if y := solve_h(g, n, m):
        return 100*y
    assert False

def solve1(g,n,m) -> int:
    lines = []
    lines.append(reflect_v(g, n, m))
    lines.append(reflect_h(g, n, m))
    return lines

def solve2(s: str) -> int:
    g, n, m = to_grid(s)

    init_lines = solve1(g, n, m)
    for i in range(n):
        for j in range(m):
            c = g[i][j]
            g[i][j] = "." if c == "#" else "#"
            x = solve1(g, n, m)
            if y := set(x[0]) - set(init_lines[0]):
                return list(y)[0]+1
            if y := set(x[1]) - set(init_lines[1]):
                return 100*(list(y)[0]+1)
            g[i][j] = c
    assert False

with PuzzleContext(year=2023, day=13) as ctx:
    ans1, ans2 = None, None

    ans1 = 0
    for gr in ctx.groups:
        x = solve(gr)
        ans1 += x


    ans2 = 0
    for gr in ctx.groups:
        x = solve2(gr)
        print(x)
        ans2 += x

    ctx.submit(1, str(ans1) if ans1 else None)
    ctx.submit(2, str(ans2) if ans2 else None)
