import matplotlib.pyplot as plt
import numpy as np


# Render with:
#   MPLBACKEND=Agg MPLCONFIGDIR=/tmp/mpl-cache .venv/bin/python figures/skill_load_model.py
def main():
    x_min, x_max = 0, 10
    y_min, y_max = 0, 9
    x = np.linspace(x_min, x_max, 400)

    comfort_boundary = x - 1.5
    frustration_boundary = x + 1.5

    points = {
        "A1": (3.0, 6.0),  # unaided target
        "A2": (3.0, 3.7),  # productive struggle begins
        "A3": (4.45, 4.55),  # support begins to fade
        "A4": (6.5, 5.15),  # near-independent performance
        "A5": (8.5, 5.85),  # earned comfort
        "B": (3.0, 0.8),  # borrowed comfort through AI substitution
    }

    fig, ax = plt.subplots(figsize=(12, 8.2))

    ax.set_xlim(x_min, x_max)
    ax.set_ylim(y_min, y_max)
    ax.set_facecolor("#f8fafc")

    ax.fill_between(
        x,
        frustration_boundary,
        y_max,
        where=frustration_boundary < y_max,
        color="#f8d7da",
        alpha=0.95,
        label="Frustration Zone",
    )
    ax.fill_between(
        x,
        comfort_boundary,
        frustration_boundary,
        color="#fff3cd",
        alpha=0.95,
        label="Learning Zone",
    )
    ax.fill_between(
        x,
        y_min,
        comfort_boundary,
        color="#d4edda",
        alpha=0.95,
        label="Comfort Zone",
    )

    ax.plot(x, comfort_boundary, color="white", linewidth=4)
    ax.plot(x, frustration_boundary, color="white", linewidth=4)

    # Original unaided target challenge.
    task_y = points["A1"][1]
    ax.hlines(
        task_y,
        x_min + 0.25,
        x_max - 0.25,
        colors="#4b5563",
        linestyles=(0, (6, 5)),
        linewidth=2,
    )
    ax.text(
        0.43,
        task_y + 0.12,
        "unaided target challenge",
        fontsize=11,
        color="#374151",
        va="bottom",
    )

    start_color = "#f97316"
    learning_color = "#237a3b"
    bypass_color = start_color

    arrow = dict(arrowstyle="->", mutation_scale=18, linewidth=2)
    ax.annotate(
        "",
        xy=points["A2"],
        xytext=points["A1"],
        arrowprops={**arrow, "color": learning_color, "shrinkA": 10, "shrinkB": 10},
    )
    # Split the AI-bypass edge into a dashed shaft and a separate solid
    # arrowhead; Matplotlib's non-solid FancyArrowPatch heads render poorly.
    a2_x, a2_y = points["A2"]
    b_x, b_y = points["B"]
    bypass_tail_start_y = a2_y - 0.22
    bypass_tail_end_y = b_y + 0.58
    bypass_head_start_y = b_y + 0.58
    bypass_head_end_y = b_y + 0.16
    ax.plot(
        [a2_x, b_x],
        [bypass_tail_start_y, bypass_tail_end_y],
        color=bypass_color,
        linestyle=(0, (6, 4)),
        linewidth=2,
        zorder=3,
    )
    ax.annotate(
        "",
        xy=(b_x, bypass_head_end_y),
        xytext=(b_x, bypass_head_start_y),
        arrowprops={
            "arrowstyle": "->",
            "mutation_scale": 18,
            "linewidth": 2,
            "color": bypass_color,
        },
        zorder=4,
    )
    for start, end in [("A2", "A3"), ("A3", "A4"), ("A4", "A5")]:
        ax.annotate(
            "",
            xy=points[end],
            xytext=points[start],
            arrowprops={**arrow, "color": learning_color, "shrinkA": 10, "shrinkB": 10},
        )

    point_styles = {
        "A1": start_color,
        "A2": learning_color,
        "A3": learning_color,
        "A4": learning_color,
        "A5": learning_color,
        "B": bypass_color,
    }
    display_labels = {
        "A1": r"$A_1$",
        "A2": r"$A_2$",
        "A3": r"$A_3$",
        "A4": r"$A_4$",
        "A5": r"$A_5$",
        "B": r"$B$",
    }
    for label, (px, py) in points.items():
        ax.scatter(
            px,
            py,
            s=420,
            color=point_styles[label],
            edgecolor=point_styles[label],
            linewidth=1.8,
            zorder=5,
        )
        ax.text(px, py, display_labels[label], color="white", ha="center", va="center", fontsize=14, fontweight="bold", zorder=6)

    ax.text(3.1, 6.3, "Unaided target", fontsize=12, fontweight="bold", ha="left")
    # ax.text(2.36, 6.28, "too hard unaided", fontsize=10, ha="center", color="#374151")

    ax.text(3.15, 3.35, "Productive struggle begins", fontsize=12, fontweight="bold", color=learning_color, ha="left")
    # ax.text(1.7, 3.98, "same student,\nlower effective load", fontsize=10, ha="center", va="top", color="#374151")

    ax.text(3.15, 0.45, "Borrowed comfort", fontsize=12, fontweight="bold", color=bypass_color, ha="left")
    # ax.text(1.7, 0.95, "completion feels easy\nwithout skill growth", fontsize=10, ha="center", va="top", color="#374151")

    ax.text(5.3, 4.1, "Support begins to fade", fontsize=12, fontweight="bold", color=learning_color, ha="center")
    ax.text(7.7, 4.7, "Near-independent performance", fontsize=12, fontweight="bold", color=learning_color, ha="center")
    ax.text(8.4, 5.4, "Earned comfort", fontsize=12, fontweight="bold", color=learning_color, ha="left")
    # ax.text(8.0, 6.28, "same task,\nhigher competence", fontsize=10, ha="center", va="top", color="#374151")

    ax.text(2.9, 2.55, "AI bypass", ha="right", fontsize=11, fontweight="bold", color=bypass_color)
    # ax.text(5.35, 4.6, "moves learner right", fontsize=10, color="#374151", ha="center")

    ax.text(3, 8, "Frustration Zone", fontsize=18, fontweight="bold", ha="center")
    ax.text(3, 7.7, "too much load for current competence", fontsize=11, ha="center", color="#374151")

    ax.text(7.1, 7.0, "Learning Zone", fontsize=18, fontweight="bold", ha="center")
    ax.text(7.1, 6.7, "challenging but reachable with support", fontsize=11, ha="center", color="#374151")

    ax.text(7, 2, "Comfort Zone", fontsize=18, fontweight="bold", ha="center")
    ax.text(7, 1.7, "can do independently", fontsize=11, ha="center", color="#374151")

    ax.set_title(
        "Figure 1. Competence and Challenge Define the Learning Zone",
        fontsize=19,
        fontweight="bold",
        pad=18,
    )
    ax.set_xlabel("Independent Competence", fontsize=14, fontweight="bold", labelpad=14)
    ax.set_ylabel("Effective Challenge", fontsize=14, fontweight="bold", labelpad=14)

    ax.set_xticks([])
    ax.set_yticks([])
    for spine in ax.spines.values():
        spine.set_color("#111827")
        spine.set_linewidth(1.6)

    # ax.text(
    #     4,
    #     -0.72,
    #     "Pathwise Pedagogy aims to make the easiest successful path move students rightward, not merely downward.",
    #     fontsize=11.5,
    #     ha="center",
    #     color="#374151",
    #     transform=ax.transData,
    # )

    fig.tight_layout()
    fig.savefig("figures/skill_load_model.svg", format="svg", bbox_inches="tight")


if __name__ == "__main__":
    main()
