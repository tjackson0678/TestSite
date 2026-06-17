#!/usr/bin/env python3
"""Read timing_output2.txt and create a grouped bar chart.

Saves plot to `timing_bar_chart.png` in the same directory.
"""
import csv
from pathlib import Path
import argparse
import numpy as np
import matplotlib.pyplot as plt


def read_timing_file(path: Path):
    with path.open("r", encoding="utf-8") as f:
        reader = csv.reader(f)
        rows = [r for r in reader if any(cell.strip() for cell in r)]
    if not rows:
        raise SystemExit(f"No data found in {path}")
    header = [h.strip() for h in rows[0]]
    numeric_rows = []
    for r in rows[1:]:
        # Convert each cell to float, ignore empty trailing cells
        numeric = [float(cell) for cell in r if cell.strip()]
        if numeric:
            numeric_rows.append(numeric)
    return header, numeric_rows


def plot_grouped_bars(labels, data_rows, out_path: Path, title=None):
    n_groups = len(labels)
    n_series = len(data_rows)
    x = np.arange(n_groups)

    fig, ax = plt.subplots(figsize=(8, 5 + n_series * 0.5))

    if n_series == 2:
        series_labels = ["Laptop", "Target"]
        series_colors = ["#4c78a8", "#e45756"]
    else:
        series_labels = [f"Series {j+1}" for j in range(n_series)]
        series_colors = [f"#{i:06x}" for i in np.linspace(0, 0xFFFFFF, n_series, dtype=int)]

    for i, row in enumerate(data_rows):
        vals = list(row)
        # if a row has fewer items than labels, pad with NaN
        if len(vals) < n_groups:
            vals += [np.nan] * (n_groups - len(vals))

        ax.plot(x, vals, marker='o', label=series_labels[i], color=series_colors[i])
        # annotate values
        max_val = np.nanmax(vals) if any(not (isinstance(v, float) and np.isnan(v)) for v in vals) else 0
        for xi, v in zip(x, vals):
            if not (v is None or (isinstance(v, float) and np.isnan(v))):
                ax.text(xi, v + max(1e-6, 0.01 * max_val), f"{v:.3f}",
                        ha="center", va="bottom", fontsize=8)

    ax.set_xticks(x)
    ax.set_xticklabels(labels)
    ax.set_xlabel("Test Cases")
    ax.set_ylabel("Time (seconds)")
    if title:
        ax.set_title(title)
    if n_series > 1:
        ax.legend()
    fig.tight_layout()
    fig.savefig(out_path, dpi=200)
    plt.close(fig)


def main():
    parser = argparse.ArgumentParser(description="Create a bar chart from TimeOut.txt")
    parser.add_argument("--input", "-i", default="TimeOutA1.txt", help="input data file")
    parser.add_argument("--output", "-o", default="TimeOutA1.png", help="output image file")
    parser.add_argument("--title", "-t", default="Timing Data - A1 - SML", help="plot title")
    args = parser.parse_args()

    path = Path(args.input)
    if not path.exists():
        raise SystemExit(f"Input file not found: {path}")

    labels, numeric_rows = read_timing_file(path)
    if not numeric_rows:
        raise SystemExit("No numeric rows found in input file")

    out_path = Path(args.output)
    plot_grouped_bars(labels, numeric_rows, out_path, title=args.title)
    print(f"Saved chart to {out_path.resolve()}")


if __name__ == "__main__":
    main()
