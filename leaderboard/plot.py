import csv
from pathlib import Path
from collections import defaultdict

if __name__ == "__main__":
    results = defaultdict(lambda: dict())
    all_users = set()
    for day in range(1, 25+1):
        p = Path(f"./data/leaderboard/day_{day}.csv")
        if not p.exists():
            break
        with p.open("r") as f:
            reader = csv.DictReader(f)
            for row in reader:
                if int(row["position"]) < 100**100:
                    all_users.add(row["user"])
                    results[day][row["user"]] = int(row["position"])
    all_users = sorted(all_users)
    df = []
    for day in sorted(results.keys()):
        row = [day]
        for user in all_users:
            row.append(str(results[day].get(user, "")))
        df.append(row)

    import matplotlib.pyplot as plt
    xs = sorted(results.keys())
    for user in all_users:
        ys = [results[x].get(user, None) for x in xs]
        alpha = 0.3
        linewidth = 1
        plot_text = lambda: None
        # TODO: possible to plot multiple users if needed
        if user in ["vstrimaitis"]:
            alpha = 1
            linewidth = 3
            plot_text = lambda: plt.text(
                xs[-1],
                ys[-1]+10,
                f"{user}: {ys[-1]}",
                horizontalalignment="right",
                verticalalignment="bottom",
                color=plt.gca().get_lines()[-1].get_c(),
                weight="bold"
            )
        plt.plot(xs, ys, alpha=alpha, linewidth=linewidth)
        plot_text()
    plt.axhline(y=50, color="red", linestyle="dashed")
    plt.axhline(y=100, color="black", linestyle="dashed")
    plt.xlabel("Day")
    plt.ylabel("Position")
    LEADERBOARD_SIZE = 200
    plt.ylim(bottom=0, top=LEADERBOARD_SIZE)
    plt.yticks([1, *range(10, LEADERBOARD_SIZE+1, 10)])
    plt.gca().invert_yaxis()
    plt.tight_layout()
    plt.margins(x=0)

    plt.savefig("leaderboard.png", dpi=200)
