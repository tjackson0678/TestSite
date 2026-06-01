#!/usr/bin/env python3
"""Plot the two timing values from each line as side-by-side comparisons."""

import argparse
import re
from pathlib import Path

import numpy as np
import matplotlib.pyplot as plt


def parse_timing_file(path):
    """Extract labels and two timing values from each line."""
    labels = []
    values1 = []
    values2 = []
    
    pattern = re.compile(r"^(.+?)\s+([0-9]*\.?[0-9]+)\s+([0-9]*\.?[0-9]+)\s+total$")
    
    with path.open("r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()
            if not line:
                continue
            match = pattern.search(line)
            if match:
                labels.append(match.group(1).strip())
                values1.append(float(match.group(2)))
                values2.append(float(match.group(3)))
            else:
                print(f"Skipping unrecognized line: {line}")
    
    return labels, values1, values2


def plot_comparison(labels, values1, values2, output_path=None):
    """Plot two values side-by-side for each label."""
    x = np.arange(len(labels))
    width = 0.35
    
    fig, ax = plt.subplots(figsize=(10, 6))
    
    ax.bar(x - width/2, values1, width, label="Laptop", color="#4c78a8")
    ax.bar(x + width/2, values2, width, label="Target", color="#e45756")
    
    ax.set_xlabel("Label")
    ax.set_ylabel("Seconds")
    ax.set_title("Timing Comparison")
    ax.set_xticks(x)
    ax.set_xticklabels(labels)
    ax.legend()
    ax.grid(axis="y", linestyle="--", alpha=0.5)
    
    fig.tight_layout()
    
    if output_path:
        plt.savefig(output_path)
        print(f"Saved plot to {output_path}")
    
    plt.show()


def main():
    parser = argparse.ArgumentParser(
        description="Plot two timing values from each line as side-by-side comparisons."
    )
    parser.add_argument(
        "file",
        nargs="?",
        default="timing_output.txt",
        help="Timing output file to parse"
    )
    parser.add_argument(
        "--output", "-o",
        help="Optional path to save the figure"
    )
    args = parser.parse_args()
    
    path = Path(args.file)
    if not path.exists():
        raise FileNotFoundError(f"Could not find file: {path}")
    
    labels, values1, values2 = parse_timing_file(path)
    
    if not labels:
        raise ValueError(f"No timing entries found in {path}")
    
    output_path = args.output or "Timing.pdf"
    plot_comparison(labels, values1, values2, output_path=output_path)


if __name__ == "__main__":
    main()
