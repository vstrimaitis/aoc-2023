from collections import *
from typing import *
from heapq import *
from dataclasses import dataclass
from puzzle import PuzzleContext
from utils import *
import itertools as itt
import functools as ft

def predict(arr: list[int]) -> int:
    lists = [arr]
    while True:
        new_list = []
        prev_list = lists[-1]
        for i in range(len(prev_list)-1):
            new_list.append(prev_list[i+1]-prev_list[i])
        lists.append(new_list)
        if all(x == 0 for x in new_list):
            break
    return sum(l[-1] for l in lists)

def predict2(arr: list[int]) -> int:
    lists = [arr]
    while True:
        new_list = []
        prev_list = lists[-1]
        for i in range(len(prev_list)-1):
            new_list.append(prev_list[i+1]-prev_list[i])
        lists.append(new_list)
        if all(x == 0 for x in new_list):
            break

    x = 0
    for i in reversed(range(len(lists))):
        x = lists[i][0] - x
    return x

with PuzzleContext(year=2023, day=9) as ctx:
    ans1, ans2 = None, None

    ans1 = 0
    for l in ctx.nonempty_lines:
        pred = predict(ints(l))
        ans1 += pred

    ctx.submit(1, str(ans1) if ans1 else None)

    ans2 = 0
    for l in ctx.nonempty_lines:
        pred = predict2(ints(l))
        ans2 += pred
    ctx.submit(2, str(ans2) if ans2 else None)
