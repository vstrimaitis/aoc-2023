from collections import *
from typing import *
from heapq import *
from dataclasses import dataclass
from puzzle import PuzzleContext
from utils import *
import itertools as itt
import functools as ft
import re


with PuzzleContext(year=2023, day=5) as ctx:
    ans1, ans2 = None, None

    gs = ctx.groups
    seeds_group = gs[0]
    seeds = [int(x) for x in re.findall(r"\d+", seeds_group)]
    seeds_orig = seeds.copy()
    
    # assume correct order
    seeds = seeds_orig.copy()
    for g in gs[1:]:
        lines = g.split("\n")
        maps = []
        for l in lines[1:]:
            maps.append([int(x) for x in l.split(" ")])
        for i in range(len(seeds)):
            for (lo_dst, lo_src, l) in maps:
                if lo_src <= seeds[i] <= lo_src+l-1:
                    d = seeds[i] - lo_src
                    seeds[i] = lo_dst + d
                    break

    ans1 = min(seeds)

    seeds = seeds_orig.copy()
    seeds = [(seeds[i], seeds[i+1]) for i in range(0, len(seeds), 2)]
    for g in gs[1:]:
        lines = g.split("\n")
        maps = []
        for l in lines[1:]:
            maps.append([int(x) for x in l.split(" ")])
        new_seeds = []
        for (seed_lo, seed_l) in seeds:
            added = False
            for (lo_dst, lo_src, l) in maps:
                seed_left = seed_lo
                seed_right = seed_lo + seed_l - 1
                src_left = lo_src
                src_right = lo_src + l - 1
                if src_right < seed_left or seed_right < src_left:
                    continue
                a = (
                    min(seed_left, src_left),
                    max(seed_left, src_left)-1,
                )
                b = (
                    max(seed_left, src_left),
                    min(seed_right, src_right),
                )
                c = (
                    min(seed_right, src_right)+1,
                    max(seed_right, src_right),
                )
                delta = lo_dst - lo_src
                for r in [a, b, c]:
                    if seed_left <= r[0] and r[1] <= seed_right:
                        if src_left <= r[0] and r[1] <= src_right:
                            new_seeds.append((r[0]+delta, r[1]-r[0]+1))
                        else:
                            new_seeds.append((r[0], r[1]-r[0]+1))
                added = True
                break
            if not added:
                new_seeds.append((seed_lo, seed_l))
        seeds = new_seeds
        print("len: ", len(seeds))
        # print(seeds)

    ans2 = min([s[0] for s in seeds])
    ctx.submit(1, str(ans1) if ans1 else None)
    ctx.submit(2, str(ans2) if ans2 else None)
