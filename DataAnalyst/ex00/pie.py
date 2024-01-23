import matplotlib.pyplot as plt
import psycopg2 as pg2


def pie_chart():
    """
    Connect to the database,
    make a pie chart of the event_type on the
    customers table.

    Arguments:
        None
    Returns:
        None
    """
    try:
        with open("pie.sql", "r") as sql_file:
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
        event_types = cursor.fetchall()
        db_connection.commit()
        print("Data fetched")
        cursor.close()
        db_connection.close()
        print("Connection closed")
        labels, sizes = zip(*event_types)
        print(labels)
        print(sizes)
        plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=0,
                wedgeprops={'linewidth': 1, 'edgecolor': 'white'})
        plt.axis('equal')

        plt.show()
    except Exception as e:
        print(f"{type(e).__name__}: {e}")


def main():
    """
    Main function
    """
    pie_chart()


if __name__ == "__main__":
    main()
