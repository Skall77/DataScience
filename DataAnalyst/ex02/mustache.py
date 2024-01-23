import psycopg2 as pg2
import numpy as np
import matplotlib.pyplot as plt


def load_data_from_query(path):
    """
    Connect to the database,
    execute a query and fetch the data.

    Arguments:
        path (str): path to the sql file

    Returns:
        data (list): list of tuples
    """
    try:
        with open(path, "r") as sql_file:
            sql_script = sql_file.read()
        db_connection = pg2.connect(
                database="piscineds",
                user="aaudevar",
                password="mysecretpassword",
                host="localhost",
                port="5432"
            )
        cursor = db_connection.cursor()
        print("Connected to database")
        cursor.execute(sql_script)
        print("Query executed")
        data = cursor.fetchall()
        db_connection.commit()
        print("Data fetched")
        cursor.close()
        db_connection.close()
        print("Connection closed")
        return data
    except Exception as e:
        print(f"{type(e).__name__}: {e}")


def main():
    """
    Main function
    load data from the database,
    Print the mean, median, min, max, first, second and third quartile
    of the price of the items purchased.
    Make boxplots that display the price of the items purchased.
    """
    data = load_data_from_query("mustache.sql")
    prices = [price for event_type, price in data if event_type == "purchase"]

    count = len(prices)
    mean = np.mean(prices)
    std = np.std(prices)
    min = np.min(prices)
    quartiles = np.percentile(prices, [25, 50, 75])
    max = np.max(prices)

    print(f"count: {count:.6f}")
    print(f"mean: {mean:.6f}")
    print(f"std: {std:.6f}")
    print(f"min: {min:.6f}")
    print(f"25%: {quartiles[0]:.6f}")
    print(f"50%: {quartiles[1]:.6f}")
    print(f"75%: {quartiles[2]:.6f}")
    print(f"max: {max:.6f}")

    figure, (axe1, axe2) = plt.subplots(1, 2, figsize=(10, 5))
    axe1.boxplot(prices,
                 vert=False,
                 widths=0.5,
                 notch=True,
                 boxprops=dict(facecolor="lightgray",
                               edgecolor="none"),
                 flierprops=dict(marker="D",
                                 markerfacecolor="lightgray",
                                 markersize=8,
                                 markeredgecolor="none"),
                 patch_artist=True)
    axe1.set_yticks([])
    axe1.set_xlabel("Price")
    axe1.set_title("Full Box Plot")

    boxprops = dict(facecolor="lightgreen", edgecolor="black")
    medianprops = dict(linestyle='-', linewidth=2, color="black")
    axe2.boxplot(prices,
                 vert=False,
                 widths=0.5,
                 notch=True,
                 boxprops=boxprops,
                 showfliers=False,
                 medianprops=medianprops,
                 patch_artist=True)
    axe2.set_yticks([])
    axe2.set_xlabel("Price")
    axe2.set_title("Box Plot without Outliers")

    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
