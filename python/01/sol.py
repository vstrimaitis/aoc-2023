from collections import *
from typing import *
from heapq import *
from dataclasses import dataclass
from puzzle import PuzzleContext
from utils import *
import itertools as itt
import functools as ft

def find_first(s: str, digit_mapping: dict[str, int]) -> int:
    positions = [
        (pos, v)
        for k, v in digit_mapping.items()
        if (pos := s.find(k)) != -1
    ]
    return min(positions, key=lambda x: x[0])[1]


def find_last(s: str, digit_mapping: dict[str, int]) -> int:
    return find_first(
        s[::-1],
        {k[::-1]: v for k, v in digit_mapping.items()}
    )


def get_calibration_value(line: str, digit_mapping: dict[str, int]) -> int:
    a = find_first(line, digit_mapping)
    b = find_last(line, digit_mapping)
    return 10*a + b

with PuzzleContext(year=2023, day=1) as ctx:
    ans1, ans2 = 0, 0

    DIGITS = {str(i): i for i in range(1, 10)}
    NAMES = {
        name: i+1
        for i, name in enumerate(
            ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
        )
    }

    for line in ctx.nonempty_lines:
        ans1 += get_calibration_value(line, DIGITS)
        ans2 += get_calibration_value(line, DIGITS | NAMES)

    ctx.submit(1, str(ans1) if ans1 else None)
    ctx.submit(2, str(ans2) if ans2 else None)
