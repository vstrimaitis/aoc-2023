from collections import *
from typing import *
from heapq import *
from dataclasses import dataclass
from puzzle import PuzzleContext
from utils import *
import itertools as itt
import functools as ft


with PuzzleContext(year=2023, day=1) as ctx:
    ans1, ans2 = None, None

    # ans1 = 0 
    # for line in ctx.nonempty_lines:
    #     digits = [c for c in line if c in "0123456789"]
    #     cv = digits[0] + digits[-1]
    #     ans1 += int(cv)

    ans2 = 0 
    for line in ctx.nonempty_lines:
        r = {
            "one": "1",
            "two": "2",
            "three": "3",
            "four": "4",
            "five": "5",
            "six": "6",
            "seven": "7",
            "eight": "8",
            "nine": "9",
            "1": "1",
            "2": "2",
            "3": "3",
            "4": "4",
            "5": "5",
            "6": "6",
            "7": "7",
            "8": "8",
            "9": "9",
        }
        first = None
        fa = None
        last = None
        la = None
        for x in r.items():
            i = line.find(x[0])
            j = line[::-1].find(x[0][::-1])
            if i == -1 or j == -1:
                continue
            if first is None or i < first:
                first = i
                fa = x[1]
            if last is None or j < last:
                last = j
                la = x[1]
        cv = fa + la
        # cv = digits[0] + digits[-1]
        print(line, cv)
        ans2 += int(cv)

    ctx.submit(1, str(ans1) if ans1 else None)
    ctx.submit(2, str(ans2) if ans2 else None)
