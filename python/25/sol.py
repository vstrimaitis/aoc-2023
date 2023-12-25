from collections import *
from typing import *
from heapq import *
from dataclasses import dataclass
from puzzle import PuzzleContext
from utils import *
import itertools as itt
import functools as ft
import networkx as nx

with PuzzleContext(year=2023, day=25) as ctx:

    edges = []
    for line in ctx.nonempty_lines:
        u, rest = line.split(": ", 1)
        for v in rest.split(" "):
            edges.append((u, v))
            edges.append((v, u))

    G = nx.Graph(edges)
    cut = list(nx.minimum_edge_cut(G))
    assert len(cut) == 3
    for e in cut:
        print("removing", e)
        edges.remove(e)
        edges.remove(tuple(reversed(e)))

    G = nx.Graph(edges)
    c = list(nx.connected_components(G))
    assert len(c) == 2
    ans1 = len(c[0]) * len(c[1])

    ctx.submit(1, str(ans1) if ans1 else None)
    # immediately submit part 2
    ctx.submit(2, "0")
