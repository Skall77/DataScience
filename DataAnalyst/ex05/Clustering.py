import numpy as np
import psycopg2 as pg2
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.discriminant_analysis import StandardScaler


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
    and use a clustering algorithm to find
    groups of type of customers.
    """
    data = load_data_from_query("Clustering.sql")
    groups = {
        0: "Loyal: Gold",
        1: "Inactive",
        2: "new customer",
        3: "Loyal: Silver",
        4: "Loyal: Platinum"
    }

    data_for_cluster = np.array([[row[1]] for row in data])

    scaler = StandardScaler()
    scaled_data = scaler.fit_transform(data_for_cluster)

    num_clusters = 5
    kmeans = KMeans(n_clusters=num_clusters, n_init=10, random_state=42)
    clusters_labels = kmeans.fit_predict(scaled_data)

    clusters_average = []
    for i in range(num_clusters):
        cluster_points = np.array([data[j][1] for j in range(len(data))
                                   if clusters_labels[j] == i])
        clusters_average.append(np.mean(cluster_points))
    sorted_clusters = np.argsort(clusters_average)

    plt.figure(figsize=(10, 5))
    for i, idx in enumerate(sorted_clusters):
        cluster_points = np.array([data[j][1] for j in range(len(data))
                                   if clusters_labels[j] == idx])
        color = plt.cm.viridis(i / num_clusters)
        plt.barh(i, np.mean(cluster_points), color=color, alpha=0.7)
        plt.text(np.mean(cluster_points) + 0.8, i, groups[idx], ha='left',
                 va='center', fontsize=10, color='black', weight='bold')

    plt.ylabel("Cluster")
    plt.xlabel("Numbers of Customers")
    plt.title("Customers per clusters")
    plt.yticks(range(num_clusters),
               [f'Cluster {i+1}' for i in range(num_clusters)])
    plt.grid(True)
    plt.show()


if __name__ == "__main__":
    main()
