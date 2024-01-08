import matplotlib.pyplot as plt
import seaborn as sns


def count_plot(df_name, column_name: str):
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


def group_plot(df_name, column_name: str):
    fig, ax = plt.subplots(1, 3, figsize=(8, 4))

    sns.countplot(
        data=df_name[df_name["diagnosis"] == "melanocytic nevi"],
        x=column_name,
        ax=ax[0],
    )
    sns.countplot(
        data=df_name[df_name["diagnosis"] == "other"], x=column_name, ax=ax[1]
    )
    sns.countplot(
        data=df_name[df_name["diagnosis"] == "melanoma"], x=column_name, ax=ax[2]
    )

    ax[0].set_title("melanocytic nevi")
    ax[1].set_title("other")
    ax[2].set_title("melanoma")

    fig.suptitle(f"Distribution of {column_name}")
    fig.tight_layout()
    plt.show()
