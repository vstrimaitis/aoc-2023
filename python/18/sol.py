from collections import *
from typing import *
from heapq import *
from dataclasses import dataclass
from puzzle import PuzzleContext
from utils import *
import itertools as itt
import functools as ft
from enum import Enum

@dataclass
class DirectionMetadata:
    symbol: str
    index: int
    delta: tuple[int, int]

class Direction(Enum):
    RIGHT = DirectionMetadata("R", 0, (0, 1))
    DOWN = DirectionMetadata("D", 1, (1, 0))
    LEFT = DirectionMetadata("L", 2, (0, -1))
    UP = DirectionMetadata("U", 3, (-1, 0))

@dataclass
class Instruction:
    direction: Direction
    distance: int

def dir_from_str(s: str) -> Direction:
    for d in Direction:
        if d.value.symbol == s:
            return d
    assert False, f"invalid direction {s}"

def dir_from_int(s: int) -> Direction:
    for d in Direction:
        if d.value.index == s:
            return d
    assert False, f"invalid direction number {s}"

def parse_line(line: str, part: Literal[1, 2]) -> Instruction:
    parts = line.split(" ")
    if part == 1:
        return Instruction(
            direction=dir_from_str(parts[0]),
            distance=int(parts[1])
        )
    hex_code = parts[2][2:-1]
    hex_dist = hex_code[:5]
    hex_dir = int(hex_code[5])
    return Instruction(
        direction=dir_from_int(hex_dir),
        distance=int(hex_dist, 16),
    )

def parse(s: str, part: Literal[1, 2]) -> list[Instruction]:
    return list(map(lambda line: parse_line(line, part), s.split("\n")))

class Polygon:
    def __init__(self, points: list[tuple[int, int]]):
        self._pts = points

    @property
    def area(self) -> int:
        ans = 0
        n = len(self._pts)
        for i in range(n):
            x1, y1 = self._pts[i]
            x2, y2 = self._pts[(i+1)%n]
            ans += x1*y2-x2*y1
        return abs(ans) // 2
    
    @property
    def n_boundary_points(self) -> int:
        n = len(self._pts)
        ans = n
        for i in range(n):
            x1, y1 = self._pts[i]
            x2, y2 = self._pts[(i+1)%n]
            dx = max(0, abs(x1 - x2) - 1)
            dy = max(0, abs(y1 - y2) - 1)
            ans += dx + dy
        return ans

    @property
    def n_inner_points(self) -> int:
        return self.area - self.n_boundary_points // 2 + 1
    
    @property
    def grid_area(self) -> int:
        return self.n_boundary_points + self.n_inner_points

def solve(instructions: list[Instruction]) -> int:
    pts = []
    i, j = 0, 0
    for instr in instructions:
        di, dj = instr.direction.value.delta
        i += di * instr.distance
        j += dj * instr.distance
        pts.append((i, j))

    return Polygon(pts).grid_area

with PuzzleContext(year=2023, day=18) as ctx:
    ans1 = solve(parse(ctx.data, part=1))
    ctx.submit(1, str(ans1))

    ans2 = solve(parse(ctx.data, part=2))
    ctx.submit(2, str(ans2))
