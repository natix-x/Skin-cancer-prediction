import matplotlib.pyplot as plt
import seaborn as sns


def count_plot(df_name, column_name: str):
    """
    creates count plot
    :param df_name: DataFrame in which column interested us exist
    :param column_name: feature of which we want to see distribution
    :return: count plot
    """
    plt.figure(figsize=(8, 4), dpi=200)
    ax = df_name[column_name].value_counts().plot(kind="bar", color="#660066")
    plt.xticks(rotation=0)
    for label in ax.containers:
        ax.bar_label(label)
    plt.title(f"Distribution of {column_name}")
    plt.ylabel("count")
    plt.tight_layout()


def diagnose(diagnosis):
    """
    assigns patient's diagnosis to particular category
    :param diagnosis: type of skin lesion
    :return: str: name of category
    """
    if diagnosis == "nv":
        return "melanocytic nevi"
    elif diagnosis == "mel":
        return "melanoma"
    else:
        return "other"


def group_plot(df_name, column_name: str):
    """
    groups three plots for three different categories
    :param df_name: used DataFrame
    :param column_name: feature of which we want to see distributions
    :return: merged three count plots
    """
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
