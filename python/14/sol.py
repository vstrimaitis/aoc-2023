from collections import *
from typing import *
from heapq import *
from dataclasses import dataclass
from puzzle import PuzzleContext
from utils import *
import itertools as itt
import functools as ft

def slide_n(g, n, m):
    for i in range(n):
        for j in range(m):
            if g[i][j] == "O":
                for ii in reversed(range(0, i)):
                    if g[ii][j] == ".":
                        g[ii][j] = "O"
                        g[ii+1][j] = "."
                    else:
                        break

def slide_s(g, n, m):
    for i in reversed(range(n)):
        for j in range(m):
            if g[i][j] == "O":
                for ii in range(i+1, n):
                    if g[ii][j] == ".":
                        g[ii][j] = "O"
                        g[ii-1][j] = "."
                    else:
                        break

def slide_w(g, n, m):
    for j in range(m):
        for i in range(n):
            if g[i][j] == "O":
                for jj in reversed(range(0, j)):
                    if g[i][jj] == ".":
                        g[i][jj] = "O"
                        g[i][jj+1] = "."
                    else:
                        break

def slide_e(g, n, m):
    for j in reversed(range(m)):
        for i in range(n):
            if g[i][j] == "O":
                for jj in range(j+1, m):
                    if g[i][jj] == ".":
                        g[i][jj] = "O"
                        g[i][jj-1] = "."
                    else:
                        break

def slide(g, n, m, d):
    match d:
        case "N": f = slide_n
        case "S": f = slide_s
        case "W": f = slide_w
        case "E": f = slide_e
        case _: assert False
    f(g,n,m)

def calc(g, n, m):
    ans = 0
    for i in range(n):
        for j in range(m):
            if g[i][j] == "O":
                ans += n-i
    return ans

with PuzzleContext(year=2023, day=14) as ctx:
    ans1, ans2 = None, None

    orig_g, n, m = to_grid(ctx.data)
    g = orig_g.copy()
    slide(g, n, m, "N")
    ans1 = 0
    for i in range(n):
        for j in range(m):
            if g[i][j] == "O":
                ans1 += n-i
    ctx.submit(1, str(ans1) if ans1 else None)

    g = orig_g.copy()
    seen = dict()
    cnt = 0
    NEED = 1000000000
    seen["\n".join("".join(row) for row in g)] = 0
    while True:
        for d in "NWSE":
            slide(g,n,m,d)
        s = "\n".join("".join(row) for row in g)
        if s in seen:
            break
        cnt += 1
        seen[s] = cnt

    x = cnt
    y = seen["\n".join("".join(row) for row in g)]
    l = abs(x-y)+1
    LEFT = (NEED - x - 1) % l
    i = y + LEFT
    for k, v in seen.items():
        if v == i:
            g, n, m = to_grid(k)
            ans2 = calc(g, n, m)
            break

    ctx.submit(2, str(ans2) if ans2 else None)
