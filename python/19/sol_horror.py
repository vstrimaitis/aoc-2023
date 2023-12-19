from __future__ import annotations
from collections import *
from typing import *
from heapq import *
from dataclasses import dataclass
import dataclasses
from puzzle import PuzzleContext
from utils import *
import itertools as itt
import functools as ft
from models import PartRatings, Range

def parse_rules(lines: list[str]) -> dict[str, list[tuple[str | None, str]]]:
    def parse_rule(s: str) -> tuple[str | None, str]:
        if ":" not in s:
            return None, s
        cond, nxt = s.split(":", 1)
        return (cond, nxt)
    def parse_line(line: str) -> tuple[str, list[tuple[str | None, str]]]:
        name, rest = line.split("{", 1)
        rules = list(map(parse_rule, rest[:-1].split(",")))
        return name, rules

    workflows = dict(map(parse_line, lines))
    
    return workflows

def parse_ratings(lines: list[str]) -> list[PartRatings]:
    def parse_part(part: str) -> tuple[str, Range]:
        parts = part.split("=", 1)
        val = int(parts[1])
        return parts[0], Range(val, val)
    ans = []
    for line in lines:
        d = dict([parse_part(part) for part in line[1:-1].split(",")])
        ans.append(PartRatings(**d))
    return ans

def generate_workflow_fn_code(name: str, conditions: list[tuple[str | None, str]]) -> str:
    lines = [
        f"def wkfl_{name}(part_ratings: PartRatings) -> int:",
        "    ans = 0",
        "",
    ]
    assert conditions[-1][0] is None

    for i, (cond, nxt) in enumerate(conditions):
        if i == len(conditions) - 1:
            match nxt:
                case "A": extra_lines = [
                    "ans += part_ratings.total"
                ]
                case "R": extra_lines = []
                case _: extra_lines = [
                    f"ans += wkfl_{nxt}(part_ratings)"
                ]
        else:
            assert cond is not None
            if "<" in cond:
                field_name, val = cond.split("<", 1)
                val = int(val)
                temp_replacement = f"{field_name}=Range(part_ratings.{field_name}.l, min(part_ratings.{field_name}.r, {val-1}))"
                new_replacement = f"{field_name}=Range(max(part_ratings.{field_name}.l, {val}), part_ratings.{field_name}.r)"
            else:
                field_name, val = cond.split(">", 1)
                val = int(val)
                temp_replacement = f"{field_name}=Range(max(part_ratings.{field_name}.l, {val+1}), part_ratings.{field_name}.r)"
                new_replacement = f"{field_name}=Range(part_ratings.{field_name}.l, min(part_ratings.{field_name}.r, {val}))"
            extra_lines = [
                f"# {cond}:{nxt}",
                f"temp_ratings = dataclasses.replace(part_ratings, {temp_replacement})",
                f"part_ratings = dataclasses.replace(part_ratings, {new_replacement})",
            ]
            match nxt:
                case "A": extra_lines.extend([
                    "ans += temp_ratings.total"
                ])
                case "R": pass
                case _: extra_lines.extend([
                    f"ans += wkfl_{nxt}(temp_ratings)"
                ])
            extra_lines.append("")
        
        for line in extra_lines:
            lines.append(f"    {line}")
    
    lines.extend([
        "",
        "    return ans",
        "",
    ])
    clean_lines = []
    for i in range(len(lines)):
        if lines[i] != "" or (i+1 < len(lines) and lines[i] == "" and lines[i+1] != ""):
            clean_lines.append(lines[i])
    return "\n".join(lines)

def generate_code(workflows: dict) -> str:
    lines = [
        "import dataclasses",
        "from models import Range, PartRatings",
        "",
    ]
    for name, conds in rules.items():
        fn_code = generate_workflow_fn_code(name, conds)
        lines.append(fn_code)
    return "\n".join(lines)

def indent(code: str) -> str:
    return "\n".join(map(lambda line: f"    {line}",code.split("\n")))


with PuzzleContext(year=2023, day=19) as ctx:
    rules = parse_rules(ctx.groups[0].split("\n"))
    ratings = parse_ratings(ctx.groups[1].split("\n"))

    code = generate_code(rules)
    with open("generated.py", "w") as f:
        f.write(code)
    # exec(code)
    from generated import wkfl_in

    ans1 = 0
    for r in ratings:
        if wkfl_in(r) > 0:
            ans1 += r.x.l + r.m.l + r.a.l + r.s.l
    ctx.submit(1, str(ans1))

    r = Range(1, 4000)
    ans2 = wkfl_in(PartRatings(r, r, r, r))
    ctx.submit(2, str(ans2))
