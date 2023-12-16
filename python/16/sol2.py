from __future__ import annotations
from collections import *
from typing import *
from heapq import *
from dataclasses import dataclass
from puzzle import PuzzleContext
from utils import *
from abc import ABC, abstractmethod
from enum import StrEnum

class Direction(StrEnum):
    UP = "^"
    DOWN = "v"
    LEFT = "<"
    RIGHT = ">"

@dataclass(unsafe_hash=True)
class State:
    row: int
    col: int
    direction: Direction
    
    @property
    def next(self) -> State:
        i = self.row
        j = self.col
        d = self.direction
        match d:
            case Direction.UP: return State(i-1, j, d)
            case Direction.DOWN: return State(i+1, j, d)
            case Direction.LEFT: return State(i, j-1, d)
            case Direction.RIGHT: return State(i, j+1, d)

    def with_direction(self, d: Direction) -> State:
        return State(self.row, self.col, d)

class Tile(ABC):
    SYMBOL = "?"

    @abstractmethod
    def get_next_states(self, state: State) -> list[State]:
        ...

    def __repr__(self) -> str:
        return self.SYMBOL

class Empty(Tile):
    SYMBOL = "."
    
    def get_next_states(self, state: State) -> list[State]:
        return [state.next]

class MirrorLR(Tile):
    SYMBOL = "/"
    
    def get_next_states(self, state: State) -> list[State]:
        match state.direction:
            case Direction.UP: next_dirs = [Direction.RIGHT]
            case Direction.DOWN: next_dirs = [Direction.LEFT]
            case Direction.LEFT: next_dirs = [Direction.DOWN]
            case Direction.RIGHT: next_dirs = [Direction.UP]
        return [state.with_direction(d).next for d in next_dirs]

class MirrorRL(Tile):
    SYMBOL = "\\"
    
    def get_next_states(self, state: State) -> list[State]:
        match state.direction:
            case Direction.UP: next_dirs = [Direction.LEFT]
            case Direction.DOWN: next_dirs = [Direction.RIGHT]
            case Direction.LEFT: next_dirs = [Direction.UP]
            case Direction.RIGHT: next_dirs = [Direction.DOWN]
        return [state.with_direction(d).next for d in next_dirs]

class SplitterH(Tile):
    SYMBOL = "-"
    
    def get_next_states(self, state: State) -> list[State]:
        match state.direction:
            case Direction.UP: next_dirs = [Direction.LEFT, Direction.RIGHT]
            case Direction.DOWN: next_dirs = [Direction.LEFT, Direction.RIGHT]
            case Direction.LEFT: next_dirs = [Direction.LEFT]
            case Direction.RIGHT: next_dirs = [Direction.RIGHT]
        return [state.with_direction(d).next for d in next_dirs]

class SplitterV(Tile):
    SYMBOL = "|"
    
    def get_next_states(self, state: State) -> list[State]:
        match state.direction:
            case Direction.UP: next_dirs = [Direction.UP]
            case Direction.DOWN: next_dirs = [Direction.DOWN]
            case Direction.LEFT: next_dirs = [Direction.DOWN, Direction.UP]
            case Direction.RIGHT: next_dirs = [Direction.DOWN, Direction.UP]
        return [state.with_direction(d).next for d in next_dirs]

class Grid:
    def __init__(self, tiles: list[list[Tile]]):
        self._tiles = tiles
        self.n_rows = len(tiles)
        self.n_cols = len(tiles[0])
        
    @classmethod
    def from_str(cls, s: str) -> Grid:
        def to_tile(c: str) -> Tile:
            return [t_cls for t_cls in Tile.__subclasses__() if t_cls.SYMBOL == c][0]()
        
        return Grid([
            [to_tile(c) for c in r]
            for r in s.split("\n")
        ])
    
    def get_current_tile(self, state: State) -> Tile:
        return self._tiles[state.row][state.col]
    
    def is_state_valid(self, state: State) -> bool:
        return 0 <= state.row < self.n_rows and 0 <= state.col < self.n_cols


def count_energized_tiles(grid: Grid, start: State) -> int:
    visited: set[State] = set()
    def dfs(g: Grid, u: State) -> None:
        if u in visited:
            return
        if not g.is_state_valid(u):
            return
        visited.add(u)
        for v in g.get_current_tile(u).get_next_states(u):
            dfs(g, v)
    dfs(grid, start)
    return len(set((s.row, s.col) for s in visited))

with PuzzleContext(year=2023, day=16) as ctx:
    g = Grid.from_str(ctx.data)

    ans1 = count_energized_tiles(g, State(0, 0, Direction.RIGHT))
    ctx.submit(1, str(ans1) if ans1 else None)
    
    start_states = []
    for i in range(g.n_rows):
        start_states.append(State(i, 0, Direction.RIGHT))
        start_states.append(State(i, g.n_cols-1, Direction.LEFT))
    for j in range(g.n_cols):
        start_states.append(State(0, j, Direction.DOWN))
        start_states.append(State(g.n_rows-1, j, Direction.UP))
    ans2 = max(map(lambda s: count_energized_tiles(g, s), start_states))
    ctx.submit(2, str(ans2) if ans2 else None)
