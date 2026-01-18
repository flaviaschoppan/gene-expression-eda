# --- Projeto 3: Gene Expression EDA ---
# Fase 1 e 2: observar dados brutos e efeito do log

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


def main():
    print("Loading data...")

    counts = pd.read_csv("data/raw/counts.csv", index_col="gene")

    print("\nCounts matrix:")
    print(counts)

    # =====================================================
    # FASE 1 — Dados brutos
    # =====================================================

    print("\nEDA step 1: plotting raw expression distributions...")

    long_df = counts.reset_index().melt(
        id_vars="gene",
        var_name="sample",
        value_name="expression"
    )

    plt.figure(figsize=(7, 5))
    sns.histplot(long_df["expression"], bins=30)

    plt.title("Distribution of raw expression values")
    plt.xlabel("Expression (raw counts)")
    plt.ylabel("Frequency")

    plt.tight_layout()
    plt.savefig("outputs/figures/raw_expression_histogram.png", dpi=150)
    plt.close()

    print("Saved: outputs/figures/raw_expression_histogram.png")

    # =====================================================
    # FASE 2 — Efeito da transformação log
    # =====================================================

    print("\nEDA step 2: log2 transformation for inspection")

    log_counts = np.log2(counts + 1)

    print("\nLog-transformed matrix (preview):")
    print(log_counts.head())

    plt.figure(figsize=(8, 5))
    plt.hist(log_counts.values.flatten(), bins=20, edgecolor="black")

    plt.title("Distribution of log2-transformed expression values")
    plt.xlabel("log2(Expression + 1)")
    plt.ylabel("Frequency")

    plt.tight_layout()
    plt.savefig("outputs/figures/log_expression_histogram.png", dpi=150)
    plt.close()

    print("Saved: outputs/figures/log_expression_histogram.png")

    print("\nEDA finished.")


if __name__ == "__main__":
    main()
