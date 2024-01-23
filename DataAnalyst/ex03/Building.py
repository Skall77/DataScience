import psycopg2 as pg2
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
    load two different data from the database,
    and create two bar charts, the first one is
    the number of orders according to frequency.
    The second one is the Altairian Dollars
    spent on the site by customers.
    """
    data_frequency = load_data_from_query("Building.sql")
    data__a_dollars = load_data_from_query("ADspent.sql")

    frenquency = [row[1] for row in data_frequency if row[1] < 40]
    a_dollars = [row[1] for row in data__a_dollars]

    figure, axes = plt.subplots(1, 2, figsize=(12, 6))

    axes[0].grid(True, zorder=-1)
    axes[0].hist(frenquency, bins=5, edgecolor="k")
    axes[0].set_xlabel("frequency")
    axes[0].set_ylabel("customers")
    axes[0].set_title("Number of orders according to frequency")
    axes[0].set_xticks(range(0, 39, 10))
    axes[0].set_ylim(0, 65000)

    axes[1].grid(True, zorder=-1)
    axes[1].hist(a_dollars, bins=5, edgecolor="k")
    axes[1].set_xlabel("Monetary value in A$")
    axes[1].set_ylabel("customers")
    axes[1].set_title("Altairian Dollars spent on the site per customers")

    for axe in axes:
        axe.yaxis.grid(True, linestyle='-', alpha=0.7)
        axe.set_axisbelow(True)

    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
