from collections import *
from typing import *
from heapq import *
from dataclasses import dataclass
from puzzle import PuzzleContext
from utils import *
import itertools as itt
import functools as ft
import re

with PuzzleContext(year=2023, day=3) as ctx:
    ans1, ans2 = None, None

    grid = ctx.nonempty_lines
    ans1 = 0
    mp = defaultdict(lambda: defaultdict(lambda: []))
    for i, line in enumerate(grid):
        for m in re.finditer(r"\d+", line):
            if m:
                j1 = m.span()[0]
                j2 = m.span()[1]
                x = int(m.group(0))
                ok = False
                for j in range(j1, j2):
                    for di in [-1, 0, 1]:
                        for dj in [-1, 0, 1]:
                            if di == 0 and dj == 0:
                                continue
                            ii = i + di
                            jj = j + dj
                            if 0 <= ii < len(grid) and 0 <= jj < len(line):
                                if grid[ii][jj] not in ".0123456789":
                                    if not ok:
                                        mp[grid[ii][jj]][(ii, jj)].append(x)
                                    ok = True
                if ok:
                    # print(x)
                    # input()
                    ans1 += x

    ans2 = 0
    for p in mp["*"].values():
        if len(p) == 2:
            ans2 += p[0] * p[1]

    ctx.submit(1, str(ans1) if ans1 else None)
    ctx.submit(2, str(ans2) if ans2 else None)
