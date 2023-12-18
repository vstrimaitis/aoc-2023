from collections import *
from typing import *
from heapq import *
from dataclasses import dataclass
from puzzle import PuzzleContext
from utils import *
import itertools as itt
import functools as ft

DELTAS = {
    "L": (0, -1),
    "R": (0, 1),
    "U": (-1, 0),
    "D": (1, 0),
}

def dfs(g, i, j):
    if g[(i, j)] == "#":
        return
    g[(i,j)] = "#"
    for di, dj in DIRS_4:
        dfs(g, i+di, j+dj)

with PuzzleContext(year=2023, day=18) as ctx:
    ans1, ans2 = None, None

    g = defaultdict(lambda: ".")
    i = 0
    j = 0
    g[(i, j)] = "#"
    for l in ctx.nonempty_lines:
        d = l[0]
        cnt = int(l.split(" ")[1])
        di, dj = DELTAS[d]
        for _ in range(cnt):
            i += di
            j += dj
            g[(i, j)] = "#"
    

    # dir_first = ctx.nonempty_lines[0][0]
    # dir_last = ctx.nonempty_lines[0]
    dfs(g, 1, 1)
    ans1 = sum([1 for v in g.values() if v =="#"])
    print(ans1)

    
    pts = []
    i = 0
    j = 0
    for l in ctx.nonempty_lines:
        # d = l[0]
        # cnt = int(l.split(" ")[1])
        code = l.split(" ")[2][2:-1]
        cnt_hex = code[:5]
        dir_hex = code[-1]
        d = "RDLU"[int(dir_hex)]
        cnt = int(cnt_hex, 16)
        di, dj = DELTAS[d]
        i += di*cnt
        j += dj*cnt
        pts.append((i, j))
        
    area = 0
    for i in range(len(pts)):
        x1, y1 = pts[i]
        x2, y2 = pts[(i+1)%len(pts)]
        area += x1*y2-x2*y1
    area = abs(area) // 2
    boundary_pts = len(pts)
    for i in range(len(pts)):
        a = pts[i]
        b = pts[(i+1)%len(pts)]
        dx = max(0,abs(a[0]-b[0])-1)
        dy = max(0,abs(a[1]-b[1])-1)
        boundary_pts += dx+dy
    print(boundary_pts)
    inner_pts = area - boundary_pts//2 + 1
    ans2 = inner_pts + boundary_pts
    print(ans2)

    # ctx.submit(1, str(ans1) if ans1 else None)
    # ctx.submit(2, str(ans2) if ans2 else None)
