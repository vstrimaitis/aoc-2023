from __future__ import annotations
from collections import *
from typing import *
from heapq import *
from dataclasses import dataclass
from puzzle import PuzzleContext
from utils import *
import itertools as itt
import functools as ft
import re

@dataclass
class Card:
    winning_nums: set[int]
    nums: list[int]

    @classmethod
    def from_str(cls, s: str) -> Card:
        parts = s.split(" | ")
        parts[0] = parts[0].split(": ", 1)[1]
        return Card(
            winning_nums=set(extract_numbers(parts[0])),
            nums=extract_numbers(parts[1])
        )
    
    @property
    def match_count(self) -> int:
        return sum(1 for x in self.nums if x in self.winning_nums)
    
    @property
    def points(self) -> int:
        if (m := self.match_count) > 0:
            return 2 ** (m - 1)
        return 0
    
def extract_numbers(s: str) -> list[int]:
    return [
        int(x)
        for x in re.findall(r"\d+", s)
    ]

with PuzzleContext(year=2023, day=4) as ctx:
    cards = list(map(Card.from_str, ctx.nonempty_lines))
    ans1 = sum([c.points for c in cards])

    
    counts = [1 for _ in range(len(cards))]
    ans2 = 0
    for i, c in enumerate(cards):
        for d in range(c.match_count):
            j = i+d+1
            if j < len(counts):
                counts[j] += counts[i]
    ans2 = sum(counts)

    ctx.submit(1, str(ans1) if ans1 else None)
    ctx.submit(2, str(ans2) if ans2 else None)
