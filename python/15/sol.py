from collections import *
from typing import *
from heapq import *
from dataclasses import dataclass
from puzzle import PuzzleContext
from utils import *
import itertools as itt
import functools as ft

def calc_hash(s: str) -> int:
    curr = 0
    for c in s:
        curr += ord(c)
        curr = 17*curr
        curr = curr % 256
    return curr

@dataclass
class Lens:
    label: str
    focal_length: int

@dataclass
class InstalledLens(Lens):
    box_id: int
    slot_id: int

    @property
    def focusing_power(self) -> int:
        return (self.box_id+1)*(self.slot_id+1)*self.focal_length

class HashMap:
    def __init__(self, size: int):
        self._boxes: list[list[Lens]] = [[] for _ in range(size)]
    
    def add(self, label: str, value: int) -> None:
        box_id = calc_hash(label)
        i = [i for i, l in enumerate(self._boxes[box_id]) if l.label == label]
        if len(i) == 0:
            self._boxes[box_id].append(Lens(label, value))
        else:
            assert len(i) == 1
            i = i[0]
            self._boxes[box_id][i].focal_length = value 

    def remove(self, label: str) -> None:
        box_id = calc_hash(label)
        self._boxes[box_id] = [l for l in self._boxes[box_id] if l.label != label]

    @property
    def installed_lenses(self) -> Iterable[InstalledLens]:
        for box_id, box in enumerate(self._boxes):
            for slot_id, lens in enumerate(box):
                yield InstalledLens(lens.label, lens.focal_length, box_id, slot_id)

with PuzzleContext(year=2023, day=15) as ctx:
    ans1 = sum(map(calc_hash, ctx.lines[0].split(",")))
    ctx.submit(1, str(ans1) if ans1 else None)

    boxes = HashMap(256)
    for p in ctx.lines[0].split(","):
        if "-" in p:
            label = p.split("-")[0]
            boxes.remove(label)
        elif "=" in p:
            label, val = p.split("=", 1)
            boxes.add(label, int(val))
    ans2 = sum(l.focusing_power for l in boxes.installed_lenses)
    ctx.submit(2, str(ans2) if ans2 else None)
