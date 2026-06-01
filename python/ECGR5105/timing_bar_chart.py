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
    width = 0.8 / max(1, n_series)

    fig, ax = plt.subplots(figsize=(8, 4 + n_series * 0.5))

    # center the grouped bars
    offsets = (np.arange(n_series) - (n_series - 1) / 2) * width
    for i, row in enumerate(data_rows):
        vals = row
        # if a row has fewer items than labels, pad with NaN
        if len(vals) < n_groups:
            vals = list(vals) + [np.nan] * (n_groups - len(vals))
        ax.bar(x + offsets[i], vals, width, label=f"Set {i+1}")
        # annotate values
        for xi, v in zip(x, vals):
            if not (v is None or (isinstance(v, float) and np.isnan(v))):
                ax.text(xi + offsets[i], v + max(1e-6, 0.01 * max(vals)), f"{v:.3f}",
                        ha="center", va="bottom", fontsize=8)

    ax.set_xticks(x)
    ax.set_xticklabels(labels)
    ax.set_xlabel("Assessment")
    ax.set_ylabel("Value")
    if title:
        ax.set_title(title)
    if n_series > 1:
        ax.legend()
    fig.tight_layout()
    fig.savefig(out_path, dpi=200)
    plt.close(fig)


def main():
    parser = argparse.ArgumentParser(description="Create a bar chart from timing_output2.txt")
    parser.add_argument("--input", "-i", default="timing_output2.txt", help="input data file")
    parser.add_argument("--output", "-o", default="timing_bar_chart.png", help="output image file")
    parser.add_argument("--title", "-t", default="Timing data", help="plot title")
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
