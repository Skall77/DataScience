import psycopg2 as pg2
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans


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
    and make an elbow Method to find
    the optimal number of clusters
    """

    data = load_data_from_query("elbow.sql")
    wcss = []

    for k in range(1, 11):
        kmeans = KMeans(n_clusters=k, n_init=10, random_state=0)
        kmeans.fit(data)
        wcss.append(kmeans.inertia_)

    plt.plot(range(1, 11), wcss)
    plt.title("The Elbow Method")
    plt.xlabel("Number of clusters")
    plt.show()


if __name__ == '__main__':
    main()
