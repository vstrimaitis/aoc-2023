from collections import *
from typing import *
from heapq import *
from dataclasses import dataclass
from puzzle import PuzzleContext
from utils import *
import itertools as itt
import functools as ft

Grid = list[list[int]]
State = tuple[
    int,  # row
    int,  # column
    str,  # last direction
    int,  # how many steps were taken using the last direction
]
DELTAS = {
    ">": (0, 1),
    "<": (0, -1),
    "^": (-1, 0),
    "v": (1, 0),
}

def get_allowed_directions(prev_dir: str) -> list[str]:
    if prev_dir in "><":
        return ["^", "v"]
    elif prev_dir in "^v":
        return [">", "<"]
    elif prev_dir == "?":
        return [">", "<", "^", "v"]
    assert False, f"invalid dir {prev_dir}"


def solve(g: Grid, min_steps: int, max_steps: int) -> int:
    n = len(g)
    m = len(g[0])

    dists: dict[State, int] = defaultdict(lambda: 10**100)
    pq = []
    heapify(pq)

    start_state = (0, 0, "?", 0)
    heappush(pq, (0, start_state))
    dists[start_state] = 0

    while pq:
        dist, state = heappop(pq)
        i, j, prev_dir, _ = state
        if dist > dists[state]:
            continue
        if i == n-1 and j == m-1:
            return dist
        dirs = get_allowed_directions(prev_dir)
        for d in dirs:
            di, dj = DELTAS[d]
            extra_dist = 0
            ii, jj = i, j
            for cnt in range(1, max_steps+1):
                ii += di
                jj += dj
                if not (0 <= ii < n and 0 <= jj < m):
                    break
                extra_dist += g[ii][jj]
                if cnt < min_steps:
                    continue
                new_dist = dist + extra_dist
                new_state = (ii, jj, d, cnt)
                if new_dist < dists[new_state]:
                    dists[new_state] = new_dist
                    heappush(pq, (new_dist, new_state))

    assert False, "didn't reach goal"


with PuzzleContext(year=2023, day=17) as ctx:
    g = list([lmap(int, list(l)) for l in ctx.nonempty_lines])

    ans1 = solve(g, min_steps=1, max_steps=3)
    ctx.submit(1, str(ans1))

    ans2 = solve(g, min_steps=4, max_steps=10)
    ctx.submit(2, str(ans2))
