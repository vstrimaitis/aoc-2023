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

def part_1(data: str) -> int:
    seeds_str, mappings_str = data.split("\n\n", 1)
    seeds = [int(x) for x in re.findall(r"\d+", seeds_str)]
    for s in mappings_str.split("\n\n"):
        lines = s.split("\n")
        for i in range(len(seeds)):
            for l in lines[1:]:
                lo_dst, lo_src, cnt = [int(x) for x in l.split(" ")]
                if lo_src <= seeds[i] <= lo_src + cnt - 1:
                    d = seeds[i] - lo_src
                    seeds[i] = lo_dst + d
                    break
    return min(seeds)

@dataclass
class Range:
    left: int
    right: int

    @classmethod
    def from_start_and_len(cls, start: int, length: int) -> Range:
        return Range(
            left=start,
            right=start+length-1,
        )
    
    def __len__(self) -> int:
        return self.right - self.left + 1
    
    def contains(self, other: Range) -> bool:
        return self.left <= other.left and other.right <= self.right

    def intersects(self, other: Range) -> bool:
        if other.right < self.left or self.right < other.left:
            return False
        return True
    
    def shift_by(self, amount: int) -> Range:
        return Range(
            left=self.left + amount,
            right=self.right + amount,
        )
    
    def split_against(self, other: Range) -> list[Range]:
        a = Range(
            left=min(self.left, other.left),
            right=max(self.left, other.left)-1,
        )
        b = Range(
            left=max(self.left, other.left),
            right=min(self.right, other.right),
        )
        c = Range(
            left=min(self.right, other.right)+1,
            right=max(self.right, other.right),
        )
        return [
            x for x in [a, b, c]
            if self.contains(x)
        ]

@dataclass
class Map:
    name: str
    ranges: list[Tuple[Range, Range]]

    @classmethod
    def parse(cls, data: str) -> Map:
        lines = data.split("\n")
        name = lines[0].split(" ")[0]
        ranges = []
        for l in lines[1:]:
            dst_left, src_left, cnt = [int(x) for x in l.split(" ")]
            src_range = Range.from_start_and_len(src_left, cnt)
            dst_range = Range.from_start_and_len(dst_left, cnt)
            ranges.append((src_range, dst_range))
        return Map(name, ranges)

@dataclass
class Input:
    seed_ranges: list[Range]
    mappings: list[Map]

    @classmethod
    def parse(cls, data: str) -> Input:
        seeds_str, maps_str = data.split("\n\n", 1)
        seed_nums = [int(x) for x in re.findall(r"\d+", seeds_str)]
        return Input(
            seed_ranges=[
                Range.from_start_and_len(seed_nums[i], seed_nums[i+1])
                for i in range(0, len(seed_nums), 2)
            ],
            mappings=list(map(Map.parse, maps_str.split("\n\n"))),
        )

def part_2(inp: Input) -> int:
    seeds = inp.seed_ranges.copy()
    for mapping in inp.mappings:
        new_seeds = []
        for seed in seeds:
            added = False
            for (src, dst) in mapping.ranges:
                if not seed.intersects(src):
                    continue
                for r in seed.split_against(src):
                    if src.contains(r):
                        new_seeds.append(r.shift_by(dst.left-src.left))
                    else:
                        new_seeds.append(r)
                added = True
                break
            if not added:
                new_seeds.append(seed)
        seeds = new_seeds
        print(f"number of seeds: {len(seeds)}")
    return min(s.left for s in seeds)


with PuzzleContext(year=2023, day=5) as ctx:
    ans1 = part_1(ctx.data)
    ctx.submit(1, str(ans1) if ans1 else None)

    ans2 = part_2(Input.parse(ctx.data))
    ctx.submit(2, str(ans2) if ans2 else None)
