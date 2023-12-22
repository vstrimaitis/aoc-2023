from __future__ import annotations
from collections import *
from typing import *
from heapq import *
from dataclasses import dataclass
from puzzle import PuzzleContext
from utils import *
import itertools as itt
import functools as ft

Coord = list[int]

@dataclass
class Brick:
    id_: int
    corners: tuple[Coord, Coord]

    @classmethod
    def parse(cls, s: str, i: int) -> Brick:
        a, b = s.split("~", 1)
        x1, y1, z1 = [int(x) for x in a.split(",")]
        x2, y2, z2 = [int(x) for x in b.split(",")]
        return Brick(i, (
            [min(x1, x2), min(y1, y2), min(z1, z2)],
            [max(x1, x2), max(y1, y2), max(z1, z2)],
        ))

    @property
    def bottom_z(self) -> int:
        return self.corners[0][2]

    @property
    def top_z(self) -> int:
        return self.corners[1][2]
    
    def drop(self, amount: int = 1) -> None:
        for c in self.corners:
            c[2] -= amount
    
    def intersects(self, other: Brick) -> bool:
        [xa1, ya1, za1], [xa2, ya2, za2] = self.corners
        [xb1, yb1, zb1], [xb2, yb2, zb2] = other.corners
        if max(xa1, xa2) < min(xb1, xb2): return False
        if min(xa1, xa2) > max(xb1, xb2): return False
        if max(ya1, ya2) < min(yb1, yb2): return False
        if min(ya1, ya2) > max(yb1, yb2): return False
        if max(za1, za2) < min(zb1, zb2): return False
        if min(za1, za2) > max(zb1, zb2): return False
        return True
    
class Snapshot:
    def __init__(self, bricks: list[Brick]):
        self._bricks = bricks
        self._sort_bricks()
        self._build_maps()

    def _sort_bricks(self) -> None:
        self._bricks = sorted(bricks, key=lambda b: b.bottom_z)
    
    def _build_maps(self) -> None:
        self._bottom_z_to_idx = defaultdict(lambda: set())
        self._top_z_to_idx = defaultdict(lambda: set())
        for i, b in enumerate(self._bricks):
            self._bottom_z_to_idx[b.bottom_z].add(i)
            self._top_z_to_idx[b.top_z].add(i)

    def count_chain_reactions(self) -> int:
        return sum(
            self._do_chain_reaction(i) - 1
            for i in range(len(self._bricks))
        )
    
    def _do_chain_reaction(self, start_idx: int) -> int:
        q = deque()
        removed = set()
        q.append(start_idx)
        removed.add(start_idx)
        while q:
            i = q.popleft()
            b = self._bricks[i]
            for j in self._bottom_z_to_idx[b.top_z+1]:
                if j in removed:
                    continue
                if self._can_fall(j, removed):
                    q.append(j)
                    removed.add(j)
        return len(removed)
    
    def _can_fall(self, idx: int, ignore: set[int] = set()) -> bool:
        ans = True
        self._drop_one(idx, 1)
        for k in self._top_z_to_idx[self._bricks[idx].bottom_z]:
            if k in ignore or k == idx:
                continue
            if self._bricks[idx].intersects(self._bricks[k]):
                ans = False
                break
        self._drop_one(idx, -1)
        return ans

    def count_safe_to_remove(self) -> int:
        ans = 0
        for i, b in enumerate(self._bricks):
            is_safe = all(
                not self._can_fall(j, {i})
                for j in self._bottom_z_to_idx[b.top_z+1]
            )
            if is_safe:
                ans += 1
        return ans

    def drop_all(self) -> None:
        last_known_top_z = 0
        for i, b in enumerate(self._bricks):
            initial_drop = max(0, b.bottom_z - (last_known_top_z+1))
            self._drop_one(i, initial_drop)
            while b.bottom_z > 1 and self._can_fall(i):
                self._drop_one(i, 1)
            last_known_top_z = max(last_known_top_z, b.top_z)
        self._sort_bricks()
        self._build_maps()

    def _drop_one(self, idx: int, amount: int) -> None:
        b = self._bricks[idx]
        self._bottom_z_to_idx[b.bottom_z].remove(idx)
        self._top_z_to_idx[b.top_z].remove(idx)
        b.drop(amount)
        self._bottom_z_to_idx[b.bottom_z].add(idx)
        self._top_z_to_idx[b.top_z].add(idx)

    # for debugging only
    def draw(self, perspective: str) -> None:
        max_x = max([max(x1, x2) for ([x1, _, _], [x2, _, _]) in map(lambda x: x.corners, self._bricks)])
        max_y = max([max(y1, y2) for ([_, y1, _], [_, y2, _]) in map(lambda x: x.corners, self._bricks)])
        max_z = max([max(z1, z2) for ([_, _, z1], [_, _, z2]) in map(lambda x: x.corners, self._bricks)])
        lines = []
        if perspective == "front":
            for z in range(0, max_z+1):
                if z == 0:
                    line = ["-"]*(max_x+1)
                else:
                    line = []
                    for x in range(0, max_x+1):
                        b = Brick(-1, ([x, 0, z], [x, 10**100, z]))
                        visible = []
                        for bb in self._bricks:
                            if bb.intersects(b):
                                visible.append(bb)
                        if len(visible) == 0:
                            line.append(".")
                        elif len(visible) == 1:
                            line.append(chr(ord("A") + visible[0].id_))
                        else:
                            line.append("?")
                lines.append("".join(line))
        elif perspective == "side":
            for z in range(0, max_z+1):
                if z == 0:
                    line = ["-"]*(max_y+1)
                else:
                    line = []
                    for y in range(0, max_y+1):
                        b = Brick(-1, ([0, y, z], [10**100, y, z]))
                        visible = []
                        for bb in self._bricks:
                            if bb.intersects(b):
                                visible.append(bb)
                        if len(visible) == 0:
                            line.append(".")
                        elif len(visible) == 1:
                            line.append(chr(ord("A") + visible[0].id_))
                        else:
                            line.append("?")
                lines.append("".join(line))
        else: assert False, f"unknown perspective {perspective}"

        print("\n".join(reversed(lines)))
        print()


with PuzzleContext(year=2023, day=22) as ctx:

    bricks = lmap(
        lambda x: Brick.parse(x[1], x[0]),
        enumerate(ctx.nonempty_lines)
    )
    snap = Snapshot(bricks)
    snap.drop_all()

    ans1 = snap.count_safe_to_remove()
    ctx.submit(1, str(ans1))

    ans2 = snap.count_chain_reactions()
    ctx.submit(2, str(ans2))
