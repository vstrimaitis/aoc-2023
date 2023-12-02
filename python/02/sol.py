from collections import *
from typing import *
from heapq import *
from dataclasses import dataclass
from puzzle import PuzzleContext
from utils import *
import itertools as itt
import functools as ft


with PuzzleContext(year=2023, day=2) as ctx:
    ans1, ans2 = None, None

    ans1 = 0
    for line in ctx.nonempty_lines:
        id, descr = line.split(": ")
        id = int(id.split(" ")[1])
        subsets = descr.split("; ")
        is_possible = True
        for s in subsets:
            counts = {}
            for ss in s.split(", "):
                x, col = ss.split(" ")
                x = int(x)
                counts[col] = x
            if counts.get("red", 0) > 12 or counts.get("green", 0) > 13 or counts.get("blue", 0) > 14:
                is_possible = False
        if is_possible:
            ans1 += id

    ans2 = 0
    for line in ctx.nonempty_lines:
        id, descr = line.split(": ")
        id = int(id.split(" ")[1])
        subsets = descr.split("; ")
        mins = {"red": 0, "green": 0, "blue": 0}
        for s in subsets:
            counts = {}
            for ss in s.split(", "):
                x, col = ss.split(" ")
                x = int(x)
                counts[col] = x
            mins["red"] = max(mins["red"], counts.get("red", 0))
            mins["green"] = max(mins["green"], counts.get("green", 0))
            mins["blue"] = max(mins["blue"], counts.get("blue", 0))
        x = mins["red"] * mins["green"] * mins["blue"]
        ans2 += x

    ctx.submit(1, str(ans1) if ans1 else None)
    ctx.submit(2, str(ans2) if ans2 else None)
