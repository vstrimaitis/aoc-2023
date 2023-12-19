from __future__ import annotations
from collections import *
from typing import *
from heapq import *
from dataclasses import dataclass
import dataclasses
from puzzle import PuzzleContext
from utils import *
import itertools as itt
import functools as ft
from abc import ABC, abstractmethod

@dataclass
class Range:
    l: int
    r: int

    @property
    def length(self) -> int:
        return max(0, self.r - self.l + 1)

@dataclass
class PartRatings:
    x: Range
    m: Range
    a: Range
    s: Range

    @property
    def count(self) -> int:
        return self.x.length * self.m.length * self.a.length * self.s.length
    
    @property
    def total(self) -> int:
        return self.x.l + self.m.l + self.a.l + self.s.l

    
    @classmethod
    def parse(cls, s: str) -> PartRatings:
        d = dict()
        for p in s[1:-1].split(","):
            field, val = p.split("=", 1)
            val = int(val)
            d[field] = Range(val, val)
        return PartRatings(**d)
    
class Node(ABC):
    @abstractmethod
    def evaluate(self, ratings: PartRatings) -> int:
        ...

class AcceptedNode(Node):
    def evaluate(self, ratings: PartRatings) -> int:
        return ratings.count
    
class RejectedNode(Node):
    def evaluate(self, ratings: PartRatings) -> int:
        return 0
    
class PassthroughNode(Node):
    def __init__(self, workflow_name: str, index: int, next: Node):
        self.id_ = f"{workflow_name}-{index}"
        self._next = next

    def evaluate(self, ratings: PartRatings) -> int:
        return self._next.evaluate(ratings)
    
class RuleNode(Node):
    def __init__(self, workflow_name: str, index: int, field_name: str, value: int, left: Node, right: Node):
        self.id_ = f"{workflow_name}-{index}"
        self._field = field_name
        self._value = value
        self._left = left
        self._right = right

    @abstractmethod
    def split(self, r: Range) -> tuple[Range, Range]:
        ...

    def evaluate(self, ratings: PartRatings) -> int:
        value_range: Range = getattr(ratings, self._field)
        range_left, range_right = self.split(value_range)
        ratings_left = dataclasses.replace(ratings, **{self._field: range_left})
        ratings_right = dataclasses.replace(ratings, **{self._field: range_right})
        return self._left.evaluate(ratings_left) + self._right.evaluate(ratings_right)

class LessNode(RuleNode):
    def split(self, r: Range) -> tuple[Range, Range]:
        left = Range(
            r.l,
            min(r.r, self._value-1),
        )
        right = Range(
            max(r.l, self._value),
            r.r,
        )
        return left, right

class GreaterNode(RuleNode):
    def split(self, r: Range) -> tuple[Range, Range]:
        left = Range(
            max(r.l, self._value + 1),
            r.r,
        )
        right = Range(
            r.l,
            min(r.r, self._value),
        )
        return left, right

def parse_rules(lines: list[str]) -> Node:
    raw_workflows = {
        parts[0]: parts[1][:-1].split(",")
        for line in lines
        if (parts := line.split("{", 1))
    }
    
    @ft.cache
    def parse_node(workflow_name: str, index: int) -> Node:
        if workflow_name == "A":
            return AcceptedNode()
        if workflow_name == "R":
            return RejectedNode()
        definition = raw_workflows[workflow_name][index]
        if ":" not in definition:
            return PassthroughNode(workflow_name, index, parse_node(definition, 0))
        cond, target = definition.split(":", 1)
        left = parse_node(target, 0)
        right = parse_node(workflow_name, index+1)
        if "<" in cond:
            name, x = cond.split("<")
            return LessNode(workflow_name, index, name, int(x), left, right)
        else:
            name, x = cond.split(">")
            return GreaterNode(workflow_name, index, name, int(x), left, right)

    return parse_node("in", 0)

with PuzzleContext(year=2023, day=19) as ctx:
    root_rule = parse_rules(ctx.groups[0].split("\n"))
    part_ratings = list(map(PartRatings.parse, ctx.groups[1].split("\n")))

    ans1 = sum(pr.total for pr in part_ratings if root_rule.evaluate(pr) > 0)
    ctx.submit(1, str(ans1))

    r = Range(1, 4000)
    ans2 = root_rule.evaluate(PartRatings(r,r,r,r))
    ctx.submit(2, str(ans2))
