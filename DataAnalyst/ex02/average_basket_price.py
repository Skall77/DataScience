import numpy as np
import matplotlib.pyplot as plt
from mustache import load_data_from_query


def main():
    """
    Main function
    load data from the database,
    and create a boxplot that display the average basket price
    """
    data = load_data_from_query("average_basket_price.sql")
    average_basket_prices = [row[1] for row in data]

    plt.figure(figsize=(10, 6))
    plt.boxplot(average_basket_prices,
                vert=False,
                widths=0.5,
                notch=True,
                boxprops=dict(facecolor="lightblue",
                              edgecolor="black"),
                flierprops=dict(marker="D",
                                markerfacecolor="lightgray",
                                markersize=8,
                                markeredgecolor="none"),
                patch_artist=True,
                whis=0.2)
    plt.xticks(np.arange(int(min(average_basket_prices)),
                         int(max(average_basket_prices)) + 1,
                         step=2))
    plt.tight_layout()
    plt.xlim(min(average_basket_prices) - 1,
             max(average_basket_prices) + 1)
    plt.yticks([])
    plt.show()


if __name__ == "__main__":
    main()
