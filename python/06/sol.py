from collections import *
from typing import *
from heapq import *
from dataclasses import dataclass
from puzzle import PuzzleContext
from utils import *
import itertools as itt
import functools as ft

def calc(t: int, d: int) -> int:
    ans = 0
    for speed in range(0, t+1):
        t_left = t - speed
        dist = t_left * speed
        if dist > d:
            ans += 1
    return ans

with PuzzleContext(year=2023, day=6) as ctx:
    ans1, ans2 = None, None

    times = [int(x) for x in re.findall(r"\d+", ctx.lines[0])]
    dists = [int(x) for x in re.findall(r"\d+", ctx.lines[1])]

    ans1 = 1
    for t, d in zip(times, dists):
        ans1 *= calc(t, d)
    ctx.submit(1, str(ans1) if ans1 else None)

    t = [int(x) for x in re.findall(r"\d+", ctx.lines[0].replace(" ", ""))][0]
    d = [int(x) for x in re.findall(r"\d+", ctx.lines[1].replace(" ", ""))][0]
    ans2 = calc(t, d)

    ctx.submit(2, str(ans2) if ans2 else None)
