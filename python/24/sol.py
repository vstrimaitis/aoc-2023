from collections import *
from typing import *
from heapq import *
from dataclasses import dataclass
from puzzle import PuzzleContext
from utils import *
import itertools as itt
import functools as ft
from decimal import Decimal, getcontext

getcontext().prec = 200
eps = Decimal("0.000000000000000000000000000001")

def cross(a, b):
    x1, y1, z1, vx1, vy1, vz1 = list(map(Decimal, a))
    x2, y2, z2, vx2, vy2, vz2 = list(map(Decimal, b))
    assert vx1 != 0 and vx2 != 0
    lhs = y1+vy1*((x2-x1)/vx1)-y2
    rhs = vy2-vy1*vx2/vx1
    if abs(rhs) < eps:
        assert abs(lhs) > eps
        return None
    t2 = lhs / rhs
    t1 = (x2-x1)/vx1+(vx2/vx1)*t2
    if t1 < eps or t2 < eps:
        return None
    X1 = x1+vx1*t1
    Y1 = y1+vy1*t1
    X2 = x2+vx2*t2
    Y2 = y2+vy2*t2
    if abs(X1-X2) < eps and abs(Y1-Y2) < eps:
        return X1, Y1, 0
    return None

def solve2(stones):
    from z3 import Solver, Or, Abs, sat, And, BitVec, Int

    # MyInt = lambda x: Int(x)
    # apparently BitVec is much faster :shrug:
    MyInt = lambda x: BitVec(x, 64)

    x, y, z = MyInt("x_0"), MyInt("y_0"), MyInt("z_0")
    vx, vy, vz = MyInt("vx_0"), MyInt("vy_0"), MyInt("vz_0")

    s = Solver()
    stones = stones[:3]
    for i in range(len(stones)):
        xx, yy, zz, vxx, vyy, vzz = stones[i]
        t = MyInt(f"t_{i+1}")
        s.add(And([
            t>=0,
            xx+vxx*t == x+vx*t,
            yy+vyy*t == y+vy*t,
            zz+vzz*t == z+vz*t,
        ]))
    print(s)
    assert s.check() == sat
    m = s.model()
    print(m)
    x0, y0, z0 = m[x], m[y], m[z]
    return x0.as_long() + y0.as_long() + z0.as_long()


def solve2_sympy(stones):
    from sympy import symbols, solve
    stones = stones[:3]
    x, y, z, vx, vy, vz, t1, t2, t3 = symbols("x, y, z, vx, vy, vz, t1, t2, t3")

    x1, y1, z1, vx1, vy1, vz1 = stones[0]
    x2, y2, z2, vx2, vy2, vz2 = stones[1]
    x3, y3, z3, vx3, vy3, vz3 = stones[2]
    """
    x + vx * t1 == x1 + vx1 * t1
    y + vy * t1 == y1 + vy1 * t1
    z + vz * t1 == z1 + vz1 * t1

    x + vx * t2 == x2 + vx2 * t2
    y + vy * t2 == y2 + vy2 * t2
    z + vz * t2 == z2 + vz2 * t2

    x + vx * t3 == x3 + vx3 * t3
    y + vy * t3 == y3 + vy3 * t3
    z + vz * t3 == z3 + vz3 * t3
    """
    eqs = [
        x + vx * t1 - (x1 + vx1 * t1),
        y + vy * t1 - (y1 + vy1 * t1),
        z + vz * t1 - (z1 + vz1 * t1),
        x + vx * t2 - (x2 + vx2 * t2),
        y + vy * t2 - (y2 + vy2 * t2),
        z + vz * t2 - (z2 + vz2 * t2),
        x + vx * t3 - (x3 + vx3 * t3),
        y + vy * t3 - (y3 + vy3 * t3),
        z + vz * t3 - (z3 + vz3 * t3),
    ]
    res = solve(eqs)
    res = res[0]
    return res[x] + res[y] + res[z]


with PuzzleContext(year=2023, day=24) as ctx:
    ans1, ans2 = None, None

    stones = []
    for line in ctx.nonempty_lines:
        stones.append(ints(line))

    ans1 = 0
    if ctx._is_running_on_sample():
        mn = 7
        mx = 27
    else:
        mn = 200000000000000
        mx = 400000000000000
    print(mn, mx, len(stones))
    for i in range(len(stones)):
        for j in range(i+1, len(stones)):
            c = cross(stones[i], stones[j])
            if c is None:
                continue
            x, y, z = c
            if mn-eps <= x <= mx+eps and mn-eps <= y <= mx+eps:
                ans1 += 1

    ctx.submit(1, str(ans1))

    ans2 = solve2_sympy(stones)
    ctx.submit(2, str(ans2))