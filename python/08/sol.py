from collections import *
from typing import *
from heapq import *
from dataclasses import dataclass
from puzzle import PuzzleContext
from utils import *
import itertools as itt
import functools as ft

def calc_cycle_len(adj: dict[str, Tuple[str, str]], cmds: str, start: str, ends: set[str]) -> int:
    curr = start
    ans = 0
    for cmd in itt.cycle(cmds):
        ans += 1
        i = "LR".index(cmd)
        curr = adj[curr][i]
        if curr in ends:
            break
    return ans

with PuzzleContext(year=2023, day=8) as ctx:
    cmds = ctx.lines[0]
    adj = dict()
    for l in ctx.lines[2:]:
        a, b = l.split(" = ", 1)
        u, v = b[1:-1].split(", ", 1)
        adj[a] = (u, v)

    ans1 = calc_cycle_len(adj, cmds, "AAA", {"ZZZ"})
    ctx.submit(1, str(ans1))

    ends = set(
        s for s in adj.keys() if s[-1] == "Z"
    )
    ans2 = math.lcm(*(
        calc_cycle_len(adj, cmds, start, ends)
        for start in adj.keys()
        if start[-1] == "A"
    ))
    ctx.submit(2, str(ans2))
