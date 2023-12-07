from __future__ import annotations
from collections import *
from typing import *
from heapq import *
from dataclasses import dataclass
from puzzle import PuzzleContext
from utils import *
import itertools as itt
import functools as ft
from enum import IntEnum

@dataclass
class Card:
    label: str

    def get_value(self, part: Literal[1, 2]) -> int:
        if part == 1:
            return "23456789TJQKA".index(self.label)
        return "J23456789TQKA".index(self.label)

class HandType(IntEnum):
    FIVE_OF_A_KIND = 6
    FOUR_OF_A_KIND = 5
    FULL_HOUSE = 4
    THREE_OF_A_KIND = 3
    TWO_PAIR = 2
    ONE_PAIR = 1
    HIGH_CARD = 0

@dataclass
class Hand:
    cards: list[Card]
    bid: int
    _alt_cards: Optional[list[list[Card]]] = None
    
    def _generate_alternatives(self, i: int = 0, curr: list[Card] = []) -> Generator[list[Card], None, None]:
        cards = self.cards
        if i >= len(cards):
            yield curr.copy()
            return
        if cards[i].label != "J":
            curr.append(cards[i])
            yield from self._generate_alternatives(i+1, curr)
            curr.pop()
        else:
            for c in "23456789TKQA":
                curr.append(Card(c))
                yield from self._generate_alternatives(i+1, curr)
                curr.pop()
    
    @property
    def alternative_cards(self) -> list[list[Card]]:
        if self._alt_cards is None:
            self._alt_cards = list(self._generate_alternatives())
        return self._alt_cards

    def get_type(self, part: Literal[1, 2]) -> HandType:
        if part == 1:
            counts = sorted(Counter(lmap(lambda c: c.label, self.cards)).values())
            match counts:
                case [5]: return HandType.FIVE_OF_A_KIND
                case [1, 4]: return HandType.FOUR_OF_A_KIND
                case [2, 3]: return HandType.FULL_HOUSE
                case [1, 1, 3]: return HandType.THREE_OF_A_KIND
                case [1, 2, 2]: return HandType.TWO_PAIR
                case [1, 1, 1, 2]: return HandType.ONE_PAIR
                case [1, 1, 1, 1, 1]: return HandType.HIGH_CARD
                case _: raise ValueError("Should not happen")
        else:
            return max(Hand(cs, self.bid).get_type(part=1) for cs in self.alternative_cards)
        
    def cmp(self, other: Hand, part: Literal[1, 2]) -> int:
        if self.get_type(part) < other.get_type(part):
            return -1
        if self.get_type(part) > other.get_type(part):
            return 1
        for c1, c2 in zip(self.cards, other.cards):
            if c1.get_value(part) < c2.get_value(part):
                return -1
            if c1.get_value(part) > c2.get_value(part):
                return 1
        return 0
        

    @classmethod
    def from_str(cls, s: str) -> Hand:
        parts = s.split(" ")
        return Hand(
            cards=lmap(lambda c: Card(c), parts[0]),
            bid=int(parts[1]),
        )

with PuzzleContext(year=2023, day=7) as ctx:
    hands = lmap(Hand.from_str, ctx.nonempty_lines)

    for part in [1, 2]:
        ans = sum(
            lmap(
                lambda x: (x[0]+1) * x[1].bid,
                enumerate(sorted(hands, key=ft.cmp_to_key(lambda a, b: a.cmp(b, part=part))))
            )
        )
        ctx.submit(part, str(ans))
