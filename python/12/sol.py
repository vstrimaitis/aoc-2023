from collections import *
from typing import *
from heapq import *
from dataclasses import dataclass
from puzzle import PuzzleContext
from utils import *
import itertools as itt
import functools as ft

def solve2(s: str, cnts: list[int]) -> int:
    # add one '.' to make conditions simpler
    s += "."
    @ft.lru_cache(maxsize=None)
    def dp(i: int, j: int, p: int) -> int:
        if j >= len(cnts):
            # all groups of #s have been found - every remaining
            # char must be either '.' or '?' (will replace with '.')
            return 1 if all(c != "#" for c in s[i:]) else 0
        if i >= len(s):
            # we reached the end but not all cnts have been exchausted
            return 0
        
        def dot_case():
            if p == 0:
                return dp(i+1, j, 0)
            if p == cnts[j]:
                return dp(i+1, j+1, 0)
            return 0
        
        def hash_case():
            return dp(i+1, j, p+1)

        match s[i]:
            case ".": return dot_case()
            case "#": return hash_case()
            case "?": return dot_case() + hash_case()
            case _: raise ValueError(f"Invalid char: {s[i]}")
    return dp(0, 0, 0)

def parse(lines: list[str]) -> list[Tuple[str, list[int]]]:
    def parse_line(line: str):
        parts = line.split(" ")
        return (parts[0], ints(parts[1]))
    return lmap(parse_line, lines)

with PuzzleContext(year=2023, day=12) as ctx:
    inputs = parse(ctx.nonempty_lines)
    
    ans1 = sum(
        solve2(pattern, cnts)
        for pattern, cnts in inputs
    )
    ctx.submit(1, str(ans1))

    ans2 = sum(
        solve2("?".join([pattern]*5), cnts*5)
        for pattern, cnts in inputs
    )
    ctx.submit(2, str(ans2))
