from collections import *
from typing import *
from heapq import *
from dataclasses import dataclass
from puzzle import PuzzleContext
from utils import *
import itertools as itt
import functools as ft

def get_next(conds, ratings) -> str:
    for cond, nxt in conds:
        if cond is None:
            return nxt
        res = eval(cond, ratings)
        if res:
            return nxt
    assert False

def is_accepted(ratings, workflows) -> bool:
    curr = "in"
    while True:
        curr = get_next(workflows[curr], ratings)
        if curr == "R":
            return False
        if curr == "A":
            return True
        
def simulate(ratings, workflows, curr) -> int:
    if any(x > y for x, y in ratings.values()):
        return 0
    if curr == "A":
        ans = 1
        for x, y in ratings.values():
            ans *= max(0, y-x+1)
        return ans
    if curr == "R":
        return 0
    conds = workflows[curr]
    ans = 0
    for cond, nxt in conds:
        if cond is None:
            ans += simulate(ratings, workflows, nxt)
            break
        if "<" in cond:
            name, val = cond.split("<", 1)
            val = int(val)
            new_ratings = ratings.copy()
            new_ratings[name] = (new_ratings[name][0], val-1)
            ans += simulate(new_ratings, workflows, nxt)
            ratings[name] = (val, ratings[name][1])
        else:
            name, val = cond.split(">", 1)
            val = int(val)
            new_ratings = ratings.copy()
            new_ratings[name] = (val+1, new_ratings[name][1])
            ans += simulate(new_ratings, workflows, nxt)
            ratings[name] = (ratings[name][0], val)
    return ans
        




with PuzzleContext(year=2023, day=19) as ctx:
    ans1, ans2 = None, None

    def parse_one(s: str) -> tuple[Optional[str], str]:
        if ":" in s:
            parts = s.split(":")
            return parts[0], parts[1]
        return (None, s)

    workflows_str, parts = ctx.groups
    workflows = dict()
    for l in workflows_str.split("\n"):
        name, rest = l.split("{", 1)
        rest = rest[:-1]
        conds = [parse_one(s) for s in rest.split(",")]
        workflows[name] = conds
        
    ans1 = 0
    for l in parts.split('\n'):
        l = l[1:-1]
        ratings = dict()
        for s in l.split(","):
            parts = s.split("=")
            ratings[parts[0]] = int(parts[1])
        s = sum(list(ratings.values()))
        if is_accepted(ratings, workflows):
            ans1 += s
    ctx.submit(1, str(ans1) if ans1 else None)

    ratings = {"x": (1, 4000),"m": (1, 4000),"a": (1, 4000),"s": (1, 4000)}

    ans2 = simulate(ratings, workflows, "in")
    ctx.submit(2, str(ans2) if ans2 else None)
