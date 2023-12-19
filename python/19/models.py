from dataclasses import dataclass

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
    def total(self) -> int:
        return self.x.length * self.m.length * self.a.length * self.s.length
