from __future__ import annotations
from collections import *
from typing import *
from heapq import *
from dataclasses import dataclass
from puzzle import PuzzleContext
from utils import *
import itertools as itt
import functools as ft

@dataclass
class Draw:
    blue: int
    red: int
    green: int

    @classmethod
    def from_str(cls, s: str) -> Draw:
        counts = {
            parts[1]: int(parts[0])
            for cnt_descr in s.split(", ")
            if (parts := cnt_descr.split(" "))
        }
        return Draw(
            blue=counts.get("blue", 0),
            red=counts.get("red", 0),
            green=counts.get("green", 0)
        )
    
    @property
    def power(self) -> int:
        return self.red * self.green * self.blue

@dataclass
class Game:
    id_: int
    draws: list[Draw]

    @classmethod
    def from_str(cls, s: str) -> Game:
        id_descr, draws_descr = s.split(": ")
        return Game(
            id_=int(id_descr.split(" ")[1]),
            draws=[Draw.from_str(s) for s in draws_descr.split("; ")]
        )
    
    @property
    def minimizing_draw(self) -> Draw:
        return ft.reduce(
            lambda a, b: Draw(
                red=max(a.red, b.red),
                green=max(a.green, b.green),
                blue=max(a.blue, b.blue),
            ),
            self.draws,
            Draw(0, 0, 0)
        )


with PuzzleContext(year=2023, day=2) as ctx:
    ans1, ans2 = 0, 0

    games = list(map(Game.from_str, ctx.nonempty_lines))

    for game in games:
        if all(d.red <= 12 and d.green <= 13 and d.blue <= 14 for d in game.draws):
            ans1 += game.id_
        ans2 += game.minimizing_draw.power

    ctx.submit(1, str(ans1) if ans1 else None)
    ctx.submit(2, str(ans2) if ans2 else None)
