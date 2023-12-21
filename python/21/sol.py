from collections import *
from typing import *
from heapq import *
from dataclasses import dataclass
from puzzle import PuzzleContext
from utils import *
import itertools as itt
import functools as ft

def print_stuff(g, cells, d):
    i_s = [i for i, _ in cells]
    j_s = [j for _, j in cells]
    i_start = 0
    i_end = len(g)-1
    j_start = 0
    j_end = len(g[0])-1
    # i_start = min(0, min(i_s))
    # i_end = max(len(g)-1, max(i_s))
    # j_start = min(0, min(j_s))
    # j_end = max(len(g[0])-1, max(j_s))
    counts = defaultdict(lambda: 0)
    for i, j in cells:
        counts[(i%len(g), j%len(g[0]))] += 1

    print(f"After {d}:")
    cnt = 0
    for i in range(0, len(g)):
        for j in range(0, len(g[0])):
            if (i, j) in cells:
                print("O", end="")
                cnt += 1
            else:
                print(g[i][j], end="")
        print()
    print(f"count: {cnt}")
    # for i in range(i_start, i_end+1):
    #     for j in range(j_start, j_end+1):
    #         c = g[i%len(g)][j%len(g[0])]
    #         cnt = counts[(i%len(g), j%len(g[0]))]
    #         if cnt > 0:
    #             print(cnt, end="")
    #         else:
    #             print(c, end="")
    #     print()
    print()

with PuzzleContext(year=2023, day=21) as ctx:
    ans1, ans2 = None, None

    g, n, m = to_grid(ctx.data)
    start = None
    for i in range(n):
        for j in range(m):
            if g[i][j] == "S":
                start = (i, j)
    assert start is not None

    reachable = [set([start])]
    NEED = 64
    for d in range(1, NEED+1):
        reachable.append(set())
        for i, j in reachable[d-1]:
            for di, dj in DIRS_4:
                ii = i + di
                jj = j + dj
                if g[ii%n][jj%m] in ".S":
                    reachable[d].add((ii, jj))

    ans1 = len(reachable[NEED])

    ctx.submit(1, str(ans1) if ans1 else None)

    # pn = n
    # # for N in range(1, 10+1):
    # N = 5000
    # reachable = [{(0, 0): set([start])}]
    # finished = dict()
    # for d in range(1, N+1):
    #     reachable.append(dict())
    #     if d % 100 == 0:
    #         print(d, len(finished), len(reachable[d-1]), sum([len(s) for s in reachable[d-1].values()]))
    #     if (d-1) % n == 0:
    #         nn = d-1
    #         x = sum([len(s) for s in reachable[nn].values()]) + sum(v[nn%2] for v in finished.values())
    #         print("!", nn, x)
    #     # for k in finished.keys():
    #     #     a, b = finished[k]
    #     #     finished[k] = b, a
    #     for (big_i, big_j), s in reachable[d-1].items():
    #         for i, j in s:
    #             for di, dj in DIRS_4:
    #                 ii = i + di
    #                 jj = j + dj
    #                 new_big_i = big_i
    #                 new_big_j = big_j
    #                 if ii < 0:
    #                     new_big_i -= 1
    #                 elif ii >= n:
    #                     new_big_i += 1
    #                 if jj < 0:
    #                     new_big_j -= 1
    #                 elif jj >= m:
    #                     new_big_j += 1
    #                 if (new_big_i, new_big_j) in finished:
    #                     continue
    #                 ii %= n
    #                 jj %= m
    #                 if g[ii][jj] in ".S":
    #                     if (new_big_i, new_big_j) not in reachable[d]:
    #                         reachable[d][(new_big_i, new_big_j)] = set()
    #                     reachable[d][(new_big_i, new_big_j)].add((ii, jj))
    #     # print_stuff(g, reachable[d], d)
    #     # print(d, reachable[d])
    #     # print(d)
    #     # for k, v in reachable[d].items():
    #     #     print(f"  {k}: {v}")
    #     # print()
    #     if d >= 3:
    #         for k in reachable[d].keys():
    #             if k in finished:
    #                 continue
    #             x0 = len(reachable[d][k])
    #             x1 = len(reachable[d-1].get(k, []))
    #             x2 = len(reachable[d-2].get(k, []))
    #             x3 = len(reachable[d-3].get(k, []))
    #             if x0 == x2 and x1 == x3:
    #                 # print("!!! found loop in ", k)
    #                 if d % 2 == 0:
    #                     finished[k] = (x0, x1)
    #                 else:
    #                     finished[k] = (x1, x0)

    #         for k in finished.keys():
    #             reachable[d].pop(k, None)

    # ans = sum([len(s) for s in reachable[N].values()]) + sum(v[N%2] for v in finished.values())
    # print(ans)

    #     # # r = dict()
    #     # reachable.append(set())
    #     # for (i, j), curr_d in reachable[d-1]:
    #     #     for di, dj in DIRS_4:
    #     #         ii = i + di
    #     #         jj = j + dj
    #     #         if ii%n != ii or jj%m != jj:
    #     #             crosses_border = True
    #     #             new_d = curr_d + 1
    #     #         else:
    #     #             crosses_border = False
    #     #             new_d = curr_d
    #     #         ii %= n
    #     #         jj %= m
    #     #         if g[ii][jj] in ".S":
    #     #             reachable[d].add(((ii, jj), new_d))
    #     #             # if (ii, jj) not in r:
    #     #             #     r[(ii, jj)] = new_d
    #     #             # elif new_d > r[(ii, jj)]:
    #     #             #     r[(ii, jj)] = new_d
    #     # # reachable.append(set(r.items()))
    #     # print(d, reachable[d], sum(d for _, d in reachable[d]))
    #     # print()
    # # x = len(reachable[N])
    # ctx.submit(2, str(ans2) if ans2 else None)


    reachable = set([start])
    NEED = 26501365

    counts = []
    prev_len = 0
    for d in range(1, 1000000):
        if len(counts) >= 3:
            break
        new_reachable = set()
        for i, j in reachable:
            for di, dj in DIRS_4:
                ii = i + di
                jj = j + dj
                if g[ii%n][jj%m] in ".S":
                    new_reachable.add((ii, jj))
        reachable = new_reachable
        if d % n == NEED % n:
            counts.append(len(reachable))
            prev_len = len(reachable)
   
    a0, a1, a2 = counts
    b0 = a0
    b1 = a1-a0
    b2 = a2-a1
    n_cycles = NEED // n
    ans2 = b0 + b1*n_cycles + (n_cycles*(n_cycles-1)//2)*(b2-b1)
    
    ctx.submit(2, str(ans2))
