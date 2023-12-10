from __future__ import annotations
from collections import *
from typing import *
from heapq import *
from dataclasses import dataclass
from puzzle import PuzzleContext
from utils import *
import itertools as itt
import functools as ft

UP = (-1, 0)
DOWN = (1, 0)
LEFT = (0, -1)
RIGHT = (0, 1)
DIRS = [UP, RIGHT, DOWN, LEFT]
PIPES = {
    "L": [UP, RIGHT],
    "J": [UP, LEFT],
    "7": [DOWN, LEFT],
    "F": [DOWN, RIGHT],
    "|": [UP, DOWN],
    "-": [LEFT, RIGHT],
}
ROTATIONS = {
    d: {
        pipe: [x for x in dirs if x != opposite_d][0]
        for pipe, dirs in PIPES.items()
        if (opposite_d := DIRS[(d_index + 2) % 4]) in dirs
    }
    for d_index, d in enumerate(DIRS)
}

def apply_dir(pos: Tuple[int, int], d: Tuple[int, int]) -> Tuple[int, int]:
    return (pos[0]+d[0], pos[1]+d[1])

@dataclass
class Grid:
    n_rows: int
    n_cols: int
    cells: list[list[str]]

    @classmethod
    def from_str(cls, s: str) -> Grid:
        lines = s.strip().split("\n")
        return Grid(
            n_rows=len(lines),
            n_cols=len(lines[0]),
            cells=[list(line) for line in lines]
        )
    
    def find_and_infer_start(self) -> Tuple[Tuple[int, int], Tuple[int, int]]:
        n = self.n_rows
        m = self.n_cols
        g = self.cells
        start_pos = None
        for i in range(n):
            for j in range(m):
                if g[i][j] == "S":
                    dirs = []
                    for (di, dj), rots in ROTATIONS.items():
                        ii = i + di
                        jj = j + dj
                        if 0 <= ii < n and 0 <= jj < m and g[ii][jj] in rots:
                            dirs.append((di, dj))
                    assert len(dirs) == 2
                    repl = [pipe for pipe, pipe_dirs in PIPES.items() if sorted(dirs) == sorted(pipe_dirs)][0]
                    g[i][j] = repl
                    start_pos = ((i, j), dirs[0])  # choose a starting direction arbitrarily
        assert start_pos is not None
        return start_pos
    
    def find_cycle(self, start_pos: Tuple[int, int], start_dir: Tuple[int, int], clean_up: bool = True) -> list[Tuple[int, int]]:
        cycle_nodes = [start_pos]
        curr = apply_dir(start_pos, start_dir)
        curr_dir = start_dir
        while curr != start_pos:
            cycle_nodes.append(curr)
            curr_dir = ROTATIONS[curr_dir][self.cells[curr[0]][curr[1]]]
            curr = apply_dir(curr, curr_dir)
        if clean_up:
            cycle = set(cycle_nodes)
            for i in range(self.n_rows):
                for j in range(self.n_cols):
                    if (i, j) not in cycle:
                        self.cells[i][j] = "."
        return cycle_nodes
    
    def find_inner_nodes(self, cycle_nodes: list[Tuple[int, int]], mark: bool = True) -> list[Tuple[int, int]]:
        cycle = set(cycle_nodes)
        ans = []
        for i in range(g.n_rows):
            is_inside = False
            for j in range(g.n_cols):
                if (i, j) in cycle:
                    if g.cells[i][j] in "|JL":
                        is_inside = not is_inside
                else:
                    if is_inside:
                        ans.append((i, j))
        if mark:
            for i, j in ans:
                self.cells[i][j] = "x"
        return ans
    
    def __str__(self) -> str:
        def to_pretty_char(c: str) -> str:
            match c:
                case "7": return "┐"
                case "F": return "┌"
                case "J": return "┘"
                case "L": return "└"
                case "-": return "─"
                case "|": return "│"
                case "x": return "𝕏"
                case _: return c
        return "\n".join(["".join(map(to_pretty_char, row)) for row in self.cells])
    

with PuzzleContext(year=2023, day=10) as ctx:
    g = Grid.from_str(ctx.data)
    start_pos, start_dir = g.find_and_infer_start()
    cycle = g.find_cycle(start_pos, start_dir, clean_up=True)

    ans1 = len(cycle) // 2
    ctx.submit(1, str(ans1))

    ans2 = len(g.find_inner_nodes(cycle))
    ctx.submit(2, str(ans2))

    # Using Pick's theorem:
    # area = 0
    # for i in range(len(cycle)):
    #     x1, y1 = cycle[i]
    #     x2, y2 = cycle[(i+1)%len(cycle)]
    #     d = x1*y2 - x2*y1
    #     area += d
    # area = abs(area // 2)
    # boundary_pt_count = len(cycle)
    # inner_pt_count = area - boundary_pt_count//2+1
    # print(inner_pt_count)

    # print(g)
