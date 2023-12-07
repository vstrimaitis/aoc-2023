from collections import *
from typing import *
from heapq import *
from dataclasses import dataclass
from puzzle import PuzzleContext
from utils import *
import itertools as itt
import functools as ft

def get_type(hand: str) -> int:
    chars = list(hand)
    counts = defaultdict(lambda: 0)
    for c in chars:
        counts[c] += 1
    if len(counts) == 1:
        return 6
    if len(counts) == 2:
        a, b = list(counts.keys())
        if max(counts[a], counts[b]) == 4:
            return 5
        if max(counts[a], counts[b]) == 3:
            return 4
        assert False
    if len(counts) == 3:
        l = sorted(list(counts.values()))
        if l == [1, 1, 3]:
            return 3
        if l == [1, 2, 2]:
            return 2
        print(hand, l)
        assert False
    if len(counts) == 4:
        return 1
    return 0

def cmp(a: str, b: str) -> int:
    if get_type(a) < get_type(b):
        return -1
    if get_type(a) > get_type(b):
        return 1
    vals = {
        '0': 0,
        '1': 1,
        '2': 2,
        '3': 3,
        '4': 4,
        '5': 5,
        '6': 6,
        '7': 7,
        '8': 8,
        '9': 9,
        'T': 10,
        'J': 11,
        'Q': 12,
        'K': 13,
        'A': 14,
    }
    for ca, cb in zip(list(a), list(b)):
        if vals[ca] < vals[cb]:
            return -1
        if vals[ca] > vals[cb]:
            return 1
    return 0

CACHE = {}

def gen(hand: str, i: int = 0, curr: list[str] = []):
    if i >= len(hand):
        yield curr
        return
    if hand[i] != "J":
        curr.append(hand[i])
        yield from gen(hand, i+1, curr)
        curr.pop()
    else:
        for c in "23456789TKQA":
            curr.append(c)
            yield from gen(hand, i+1, curr)
            curr.pop()

def get_type_2(hand: str) -> int:
    if hand in CACHE:
        types = CACHE[hand]
    else:
        types = list(get_type(x) for x in gen(hand))
        CACHE[hand] = types
    return max(types)

def cmp_2(a: str, b: str) -> int:
    if get_type_2(a) < get_type_2(b):
        return -1
    if get_type_2(a) > get_type_2(b):
        return 1
    vals = {
        '0': 0,
        '1': 1,
        '2': 2,
        '3': 3,
        '4': 4,
        '5': 5,
        '6': 6,
        '7': 7,
        '8': 8,
        '9': 9,
        'T': 10,
        'J': -1,
        'Q': 12,
        'K': 13,
        'A': 14,
    }
    for ca, cb in zip(list(a), list(b)):
        if vals[ca] < vals[cb]:
            return -1
        if vals[ca] > vals[cb]:
            return 1
    return 0
    

with PuzzleContext(year=2023, day=7) as ctx:
    ans1, ans2 = None, None

    hands = lmap(lambda l: l.split(" "), ctx.nonempty_lines)

    # for i in range(len(hands)):
    #     for j in range(len(hands)):
    #         if cmp(hands[i][0], hands[j][0]) == -1:
    #             hands[i], hands[j] = hands[j], hands[i]
    hands = sorted(hands, key=ft.cmp_to_key(lambda a, b: cmp(a[0], b[0])))
    
    ans1 = 0
    for i, (_, x) in enumerate(hands):
        ans1 += (i+1) * int(x)
    ctx.submit(1, str(ans1) if ans1 else None)


    hands = sorted(hands, key=ft.cmp_to_key(lambda a, b: cmp_2(a[0], b[0])))
    ans2 = 0
    for i, (_, x) in enumerate(hands):
        ans2 += (i+1) * int(x)

    ctx.submit(2, str(ans2) if ans2 else None)
