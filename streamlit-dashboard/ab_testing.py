import pandas as pd
import numpy as np

from scipy.stats import chi2_contingency

np.random.seed(42)

df = pd.read_csv(
    "data/dataset_pretext.csv"
)

if "Unnamed: 0" in df.columns:
    df = df.drop(
        columns=["Unnamed: 0"]
    )


df["variant"] = np.random.choice(
    ["A", "B"],
    size=len(df)
)

df["success"] = (
    df["problem_category"]
    != "direction_confused"
).astype(int)

summary = (
    df.groupby("variant")["success"]
    .agg(
        total="count",
        success="sum"
    )
)

summary["failure"] = (
    summary["total"]
    - summary["success"]
)

print(summary)

contingency_table = [
    [
        summary.loc["A", "success"],
        summary.loc["A", "failure"]
    ],
    [
        summary.loc["B", "success"],
        summary.loc["B", "failure"]
    ]
]

chi2, p_value, dof, expected = (
    chi2_contingency(
        contingency_table
    )
)

print("\nHASIL A/B TEST")
print(f"Chi Square : {chi2:.4f}")
print(f"P-Value    : {p_value:.4f}")

if p_value < 0.05:
    print(
        "Terdapat perbedaan signifikan antara A dan B"
    )
else:
    print(
        "Tidak terdapat perbedaan signifikan antara A dan B"
    )

summary.to_csv(
    "outputs/ab_test_result.csv"
)