import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
import psycopg2 as pg2
from datetime import datetime
from collections import defaultdict
import numpy as np


def load_data_from_query():
    """
    Connect to the database,
    execute a query and fetch the data.

    Arguments:
        None

    Returns:
        data (list): list of tuples
    """
    try:
        with open("char.sql", "r") as sql_file:
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

    retrieve the data from the database,
    and create three different charts
    """

    data = load_data_from_query()

    # First chart data
    purchase_counts = {}
    data_purchase = [(t[1], t[2]) for t in data if t[2] == "purchase"]

    for event_time, event_type in data_purchase:
        year, month, day = event_time.year, event_time.month, event_time.day
        date = datetime(year, month, day)
        date_str = date.strftime("%Y-%m-%d")
        if date_str not in purchase_counts:
            purchase_counts[date_str] = 0
        purchase_counts[date_str] += 1

    sorted_counts = sorted(purchase_counts.items())
    dates, counts = zip(*sorted_counts)

    # Second chart data
    monthly_sales = defaultdict(float)
    data_sales = [(t[1], t[2], t[3]) for t in data if t[2] == "purchase"]

    for event_time, event_type, price in data_sales:
        year, month = event_time.year, event_time.month
        month_str = datetime(year, month, 1).strftime('%b')
        monthly_sales[month_str] += price

    months = ['Oct', 'Nov', 'Dec', 'Jan']
    sales = [monthly_sales[month] * 0.8 for month in months]

    # Third chart data
    daily_sales = defaultdict(float)
    unique_customers = defaultdict(set)

    for user_id, event_time, event_type, price in data:
        if event_type == "purchase":
            date_str = event_time.strftime('%Y-%m-%d')
            daily_sales[date_str] += price
            unique_customers[date_str].add(user_id)

    dates_daily_sales = sorted(daily_sales.keys())
    average_spend = [daily_sales[date] * 0.8 / len(unique_customers[date])
                     for date in dates_daily_sales]

    plt.figure(figsize=(15, 5))

    # First chat layout
    plt.subplot(1, 3, 1)
    plt.plot(dates, counts, linestyle='-', color='blue', alpha=0.2)
    plt.ylabel("Number of customers")
    plt.gca().yaxis.set_major_formatter(FuncFormatter(
        lambda x, pos: f"{int(x / 10)}"))
    tick_postions = [0, len(dates) // 4,
                     2 * len(dates) // 4, 3 * len(dates) // 4]
    tick_labels = ["Oct", "Nov", "Dec", "Jan"]
    plt.xticks(tick_postions, tick_labels)
    plt.xlim(dates[0], dates[-1])

    # Second chart layout
    plt.subplot(1, 3, 2)
    plt.bar(months, sales,  color='blue', alpha=0.2)
    plt.ylabel("total sales in Altairian Dollars")
    plt.xlabel("month")

    # Third chart layout
    plt.subplot(1, 3, 3)
    plt.plot(dates_daily_sales, average_spend, color='blue', alpha=0.2)
    plt.fill_between(dates_daily_sales, average_spend, color='blue', alpha=0.2)
    plt.ylabel("average spend/customer in AD")
    plt.xticks(tick_postions, tick_labels)
    plt.xlim(dates[0], dates[-1])
    plt.yticks(np.arange(0, max(average_spend), 5))
    plt.ylim(0)

    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
