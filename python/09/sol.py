from collections import *
from typing import *
from heapq import *
from dataclasses import dataclass
from puzzle import PuzzleContext
from utils import *
import itertools as itt
import functools as ft

def calc_diff_lists(arr: list[int]) -> list[list[int]]:
    lists = [arr]
    while not all(x == 0 for x in lists[-1]):
        lists.append(
            [
                y-x
                for x, y in zip(lists[-1], lists[-1][1:])
            ]
        )
    return lists

with PuzzleContext(year=2023, day=9) as ctx:

    histories = lmap(ints, ctx.nonempty_lines)
    ans1 = sum(
        sum(dlist[-1] for dlist in calc_diff_lists(hist))
        for hist in histories
    )
    ctx.submit(1, str(ans1))

    ans2 = sum(
        ft.reduce(
            lambda acc, x: x - acc,
            reversed([dlist[0] for dlist in calc_diff_lists(hist)])
        )
        for hist in histories
    )
    ctx.submit(2, str(ans2))
