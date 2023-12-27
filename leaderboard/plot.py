import csv
from pathlib import Path
from collections import defaultdict
from dataclasses import dataclass
import matplotlib.pyplot as plt

PREV_YEAR_KEY = "__vstrimaitis__2022__"

@dataclass
class Highlight:
    text: str
    color: str

def read_results():
    results = defaultdict(lambda: dict())
    # results from 2022
    prev_results = {1: None, 2: None, 3: None, 4: None, 5: 333, 6: 371, 7: 410, 8: 448, 9: 444, 10: 265, 11: 285, 12: 143, 13: 152, 14: 161, 15: 169, 16: 183, 17: 193, 18: 192, 19: 144, 20: 149, 21: 105, 22: 100, 23: 78, 24: 70, 25: 73}
    for day in range(1, 25+1):
        p = Path(f"./data/leaderboard/day_{day}.csv")
        if not p.exists():
            break
        with p.open("r") as f:
            reader = csv.DictReader(f)
            for row in reader:
                results[day][row["user"]] = int(row["position"])

        # attach previous year's result
        if (r := prev_results[day]) is not None:
            results[day][PREV_YEAR_KEY] = r
    return results

def plot(results, highlights: dict[str, Highlight], goal_position: int, cutoff_position: int = 100, output_file: Path | None = None, leaderboard_size: int = 200) -> None:
    all_users = set(
        user
        for r in results.values()
        for user in r.keys()
    )
    xs = sorted(results.keys())
    for user in all_users:
        ys = [results[x].get(user, None) for x in xs]
        alpha = 0.3
        linewidth = 1
        color = None
        if user in highlights:
            alpha = 1
            linewidth = 3
            color = highlights[user].color
            plt.text(
                xs[-1]+0.5,
                ys[-1],
                highlights[user].text + f" ({ys[-1]})",
                color=color,
                weight="bold"
            )
        plt.plot(xs, ys, alpha=alpha, linewidth=linewidth, color=color)

    plt.text(xs[-1]+0.5, goal_position, "goal", color="red", weight="bold")
    plt.axhline(y=goal_position, color="red", linestyle="dashed")

    plt.text(xs[-1]+0.5, cutoff_position, "cutoff", color="black", weight="bold")
    plt.axhline(y=cutoff_position, color="black", linestyle="dashed")

    plt.xlabel("Day")
    plt.ylabel("Position")
    plt.ylim(bottom=0, top=leaderboard_size)
    plt.yticks([1, *range(10, leaderboard_size+1, 10)])
    plt.gca().invert_yaxis()
    plt.margins(x=0)
    plt.tight_layout()
    if output_file:
        plt.savefig(output_file, dpi=200)
    else:
        plt.show()


if __name__ == "__main__":
    results = read_results()
    plot(
        results,
        highlights={
            "vstrimaitis": Highlight(
                text="2023 result",
                color="blue",
            ),
            PREV_YEAR_KEY: Highlight(
                text="2022 result",
                color="gray"
            ),
        },
        goal_position=50,
        output_file=Path("./leaderboard.png"),
    )
