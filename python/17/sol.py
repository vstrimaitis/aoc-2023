from collections import *
from typing import *
from heapq import *
from dataclasses import dataclass
from puzzle import PuzzleContext
from utils import *
import itertools as itt
import functools as ft

def solve1(g, n, m):
    dists = dict()
    pq = []
    heapify(pq)
    heappush(pq, (0, 0, 0, "?", 0))
    dists[(0, 0, "?", 0)] = 0
    while len(pq) > 0:
        i, j, d, prev_dir, prev_cnt = heappop(pq)
        if d > dists[(i, j, prev_dir, prev_cnt)]:
            continue
        dirs = ["^", "v", "<", ">"]
        match prev_dir:
            case "<": dirs.remove(">")
            case ">": dirs.remove("<")
            case "^": dirs.remove("v")
            case "v": dirs.remove("^")
        for dd in dirs:
            match dd:
                case "^": ii, jj = i-1, j
                case "v": ii, jj = i+1, j
                case ">": ii, jj = i, j+1
                case "<": ii, jj = i, j-1
                case _: assert False
            if dd == prev_dir:
                new_cnt = prev_cnt + 1
            else:
                new_cnt = 1
            if new_cnt > 3:
                continue
            if 0 <= ii < n and 0 <= jj < m:
                new_d = d + int(g[ii][jj])
                if (ii, jj, dd, new_cnt) not in dists or new_d < dists[(ii, jj, dd, new_cnt)]:
                    dists[(ii, jj, dd, new_cnt)] = new_d
                    heappush(pq, (ii, jj, new_d, dd, new_cnt))

    ans = min(dists[k] for k in dists.keys() if (k[0], k[1]) == (n-1, m-1))
    return ans

def solve2(g, n, m):
    dists = dict()
    pq = []
    heapify(pq)
    heappush(pq, (0, 0, 0, "?", 0))
    dists[(0, 0, "?", 0)] = 0
    while len(pq) > 0:
        i, j, d, prev_dir, prev_cnt = heappop(pq)
        if d > dists[(i, j, prev_dir, prev_cnt)]:
            continue
        dirs = ["^", "v", "<", ">"]
        match prev_dir:
            case "<":
                dirs.remove(">")
                dirs.remove("<")
            case ">":
                dirs.remove("<")
                dirs.remove(">")
            case "^":
                dirs.remove("v")
                dirs.remove("^")
            case "v":
                dirs.remove("^")
                dirs.remove("v")
        for dd in dirs:
            match dd:
                case "^": di, dj = -1, 0
                case "v": di, dj = 1, 0
                case ">": di, dj = 0, 1
                case "<": di, dj = 0, -1
                case _: assert False
                
            s = 0
            ii = i
            jj = j
            for cnt in range(1, 11):
                ii += di
                jj += dj
                if 0 <= ii < n and 0 <= jj < m:
                    s += int(g[ii][jj])
                    if cnt >= 4:
                        new_d = d + s
                        if (ii, jj, dd, cnt) not in dists or new_d < dists[(ii, jj, dd, cnt)]:
                            dists[(ii, jj, dd, cnt)] = new_d
                            heappush(pq, (ii, jj, new_d, dd, cnt))

    ans = min(dists[k] for k in dists.keys() if (k[0], k[1]) == (n-1, m-1))
    return ans

with PuzzleContext(year=2023, day=17) as ctx:
    ans1, ans2 = None, None

    g, n, m = to_grid(ctx.data)
    ans1 = solve1(g, n, m)

    ctx.submit(1, str(ans1) if ans1 else None)

    ans2 = solve2(g, n, m)
    ctx.submit(2, str(ans2) if ans2 else None)
