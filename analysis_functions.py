import matplotlib.pyplot as plt
import pandas as pd


def count_plot(df_name, column_name):
    plt.figure(figsize=(8, 4), dpi=200)
    ax = df_name[column_name].value_counts().plot(kind="bar")
    plt.xticks(rotation=0)
    for label in ax.containers:
        ax.bar_label(label)
    plt.title(f"Distribution of {column_name}")
    plt.ylabel("count")
    plt.tight_layout()
    plt.show()


def diagnose(diagnosis):
    if diagnosis == "nv":
        return "melanocytic nevi"
    elif diagnosis == "mel":
        return "melanoma"
    else:
        return "other"
