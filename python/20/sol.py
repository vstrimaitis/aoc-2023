from collections import *
from typing import *
from heapq import *
from dataclasses import dataclass
from puzzle import PuzzleContext
from utils import *
import itertools as itt
import functools as ft

def solve(adj, start, cnt):
    inputs = defaultdict(lambda: [])
    for k, (_, v) in adj.items():
        for x in v:
            inputs[x].append(k)
    
    states = defaultdict(lambda: "off")
    prev_pulses = {k: {x: "low" for x in v} for k, v in inputs.items()}
    n_low = 0
    n_high = 0
    for _ in range(cnt):
        q = deque()
        q.append(("broadcaster", "button", "low"))
        while len(q) > 0:
            u, u_prev, freq = q.popleft()
            # print(f"{u_prev} -{freq}-> {u}")
            if freq == "low":
                n_low += 1
            else:
                n_high += 1
            t = adj[u][0]
            if t is None:
                for v in adj[u][1]:
                    q.append((v, u, freq))
            elif t == "%":
                if freq == "high":
                    continue
                if states[u] == "off":
                    states[u] = "on"
                    for v in adj[u][1]:
                        q.append((v, u, "high"))
                else:
                    states[u] = "off"
                    for v in adj[u][1]:
                        q.append((v, u, "low"))
            elif t == "&":
                prev_pulses[u][u_prev] = freq
                if all(x == "high" for x in prev_pulses[u].values()):
                    for v in adj[u][1]:
                        q.append((v, u, "low"))
                else:
                    for v in adj[u][1]:
                        q.append((v, u, "high"))
            else:
                assert False

    return n_low, n_high

def solve2(adj, start):
    inputs = defaultdict(lambda: [])
    for k, (_, v) in adj.items():
        for x in v:
            inputs[x].append(k)
    
    states = defaultdict(lambda: "off")
    prev_pulses = {k: {x: "low" for x in v} for k, v in inputs.items()}
    n_low = 0
    n_high = 0
    cnt = 0
    while True:
        cnt += 1
        if cnt % 100000 == 0:
            print(cnt)
            for x in ["th", "sv", "gh", "ch"]:
                s = []
                for k,v in prev_pulses[x].items():
                    if v == "high": v = 1
                    else: v = 0
                    s.append(f"{k}={v}")
                print(x, ",".join(s))
            print()
            for x in ["fd", "pl", "hm", "jc"]:
                s = []
                for k,v in prev_pulses[x].items():
                    if v == "high": v = 1
                    else: v = 0
                    s.append(f"{k}={v}")
                print(x, ",".join(s))
        q = deque()
        q.append((start, "button", "low"))
        while len(q) > 0:
            u, u_prev, freq = q.popleft()
            if u == "rx" and freq == "low":
                return cnt
            if freq == "low":
                n_low += 1
            else:
                n_high += 1
            t = adj[u][0]
            if t is None:
                for v in adj[u][1]:
                    q.append((v, u, freq))
            elif t == "%":
                if freq == "high":
                    continue
                if states[u] == "off":
                    states[u] = "on"
                    for v in adj[u][1]:
                        q.append((v, u, "high"))
                else:
                    states[u] = "off"
                    for v in adj[u][1]:
                        q.append((v, u, "low"))
            elif t == "&":
                prev_pulses[u][u_prev] = freq
                if all(x == "high" for x in prev_pulses[u].values()):
                    for v in adj[u][1]:
                        q.append((v, u, "low"))
                else:
                    if u in ["th", "sv", "gh", "ch"]:
                        print(f"{u} is sending high after {cnt}")
                    for v in adj[u][1]:
                        q.append((v, u, "high"))
                    # 3917, 7834, 11751, 15668
            else:
                assert False

    assert False


with PuzzleContext(year=2023, day=20) as ctx:
    ans1, ans2 = None, None

    adj = dict()
    for line in ctx.nonempty_lines:
        src, dst = line.split(" -> ", 1)
        dsts = dst.split(", ")
        if src[0] in "%&":
            t = src[0]
            src = src[1:]
            adj[src] = (t, dsts)
        else:
            adj[src] = (None, dsts)
    for _, l in adj.copy().values():
        for x in l:
            if x not in adj:
                adj[x] = (None, [])

    n_low, n_high = solve(adj, "broadcaster", 1000)
    print(n_low, n_high)
    ans1 = n_low * n_high

    ctx.submit(1, str(ans1) if ans1 else None)

    ans2 = solve2(adj, "broadcaster")
    ctx.submit(2, str(ans2) if ans2 else None)
