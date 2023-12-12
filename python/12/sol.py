from collections import *
from typing import *
from heapq import *
from dataclasses import dataclass
from puzzle import PuzzleContext
from utils import *
import itertools as itt
import functools as ft

def gen(s: str, i: int = 0, curr: list[str] = []):
    if i >= len(s):
        yield "".join(curr)
        return
    if s[i] == "?":
        for c in ".#":
            curr.append(c)
            yield from gen(s, i+1, curr)
            curr.pop()
    else:
        curr.append(s[i])
        yield from gen(s, i+1, curr)
        curr.pop()

def solve(s: str, cnts: list[int]) -> int:
    @ft.lru_cache(maxsize=None)
    def dp(i: int, j: int, p: int) -> int:
        if i >= len(s):
            if j == len(cnts) and p == 0:
                return 1
            if j == len(cnts)-1 and p == cnts[-1]:
                return 1
            return 0
        if s[i] == "#":
            return dp(i+1, j, p+1)
        if s[i] == ".":
            if p == 0:
                return dp(i+1, j, 0)
            elif j < len(cnts) and p == cnts[j]:
                return dp(i+1, j+1, 0)
            return 0
        options = []
        # put #
        options.append(dp(i+1, j, p+1))
        # put .
        if j < len(cnts) and p == cnts[j]:
            options.append(dp(i+1, j+1, 0))
        elif p == 0:
            options.append(dp(i+1, j, 0))
        return sum(options)
    return dp(0, 0, 0)
        

def matches(s: str, cnts: list[int]):

    return [len(x) for x in s.split(".") if x] == cnts

with PuzzleContext(year=2023, day=12) as ctx:
    ans1, ans2 = None, None

    # ans1 = 0
    # for i, l in enumerate(ctx.nonempty_lines):
    #     print(i, l)
    #     pattern, cnts = l.split(" ")
    #     cnts = ints(cnts)
    #     ans = 0
    #     for s in gen(pattern):
    #         if matches(s, cnts):
    #             ans += 1
    #     ans1 += ans

    # ctx.submit(1, str(ans1) if ans1 else None)

    ans2 = 0
    for i, l in enumerate(ctx.nonempty_lines):
        print(i, l)
        pattern, cnts = l.split(" ")
        cnts = ints(cnts)

        pattern = "?".join([pattern]*5)
        cnts = cnts*5

        # ans = 0
        # for s in gen2(pattern, cnts=cnts):
        #     ans += 1
        ans = solve(pattern, cnts)
        print(ans)
        ans2 += ans
    ctx.submit(2, str(ans2) if ans2 else None)
