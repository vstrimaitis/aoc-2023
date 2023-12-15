from collections import *
from typing import *
from heapq import *
from dataclasses import dataclass
from puzzle import PuzzleContext
from utils import *
import itertools as itt
import functools as ft


def calc(s: str) -> int:
    curr = 0
    for c in s:
        curr += ord(c)
        curr = 17*curr
        curr = curr % 256
    return curr

with PuzzleContext(year=2023, day=15) as ctx:
    ans1, ans2 = None, None

    ans1 = 0
    for p in ctx.lines[0].split(","):
        ans1 += calc(p)
    ctx.submit(1, str(ans1) if ans1 else None)

    N = 256
    lenses: list[list[tuple[str, int]]] = [[] for _ in range(N)]
    for p in ctx.lines[0].split(","):
        if "-" in p:
            label = p.split("-")[0]
            box_id = calc(label)
            print(label, box_id)
            lenses[box_id] = [l for l in lenses[box_id] if l[0] != label]
        elif "=" in p:
            label, val = p.split("=", 1)
            box_id = calc(label)
            print(label, box_id)
            val = int(val)
            i = [i for i, l in enumerate(lenses[box_id]) if l[0] == label]
            if len(i) > 0:
                assert len(i) == 1
                lenses[box_id][i[0]] = (label, val)
            else:
                lenses[box_id].append((label, val))
    ans2 = 0
    for i in range(N):
        for i, (box_id, v) in enumerate(lenses[i]):
            ans2 += (calc(box_id)+1)*(i+1)*v
    ctx.submit(2, str(ans2) if ans2 else None)
