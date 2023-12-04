from collections import *
from typing import *
from heapq import *
from dataclasses import dataclass
from puzzle import PuzzleContext
from utils import *
import itertools as itt
import functools as ft
import re


with PuzzleContext(year=2023, day=4) as ctx:
    ans1, ans2 = None, None

    ans1 = 0
    for l in ctx.nonempty_lines:
        parts = l.split(" | ")
        winning = set([int(x) for x in re.findall(r"\d+", parts[0].split(": ")[1])])
        have = [int(x) for x in re.findall(r"\d+", parts[1])]
        pts = 0
        for x in have:
            if x in winning:
                if pts == 0:
                    pts = 1
                else:
                    pts *= 2
        ans1 += pts

    
    ans2 = 0
    counts = defaultdict(lambda: 1)
    for i, l in enumerate(ctx.nonempty_lines):
        _ = counts[i]
        parts = l.split(" | ")
        winning = set([int(x) for x in re.findall(r"\d+", parts[0].split(": ")[1])])
        have = [int(x) for x in re.findall(r"\d+", parts[1])]
        matches = sum(1 for x in have if x in winning)
        for j in range(matches):
            counts[i+j+1] += counts[i]
    ans2 = sum(counts.values())
        

    ctx.submit(1, str(ans1) if ans1 else None)
    ctx.submit(2, str(ans2) if ans2 else None)
