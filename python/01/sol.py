from collections import *
from typing import *
from heapq import *
from dataclasses import dataclass
from puzzle import PuzzleContext
from utils import *
import itertools as itt
import functools as ft
import re

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

# alternative solution using regex
def get_calibration_value_2(line: str, digit_mapping: dict[str, int]) -> int:
    pattern = "|".join(digit_mapping.keys())
    pattern = f"(?=({pattern}))"
    # generates this for the second part
    # (?=(1|2|3|4|5|6|7|8|9|one|two|three|four|five|six|seven|eight|nine))
    matches = re.findall(pattern, line)
    a = digit_mapping[matches[0]]
    b = digit_mapping[matches[-1]]
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
