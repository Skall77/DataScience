import psycopg2 as pg2


def run_query(query_path):
    """
    Connect to the database
    execute the query
    commit the changes
    close the connection

    Arguments:
        query_path {str} -- Path to the query file

    Returns:
        None
    """
    try:
        with open(query_path, "r") as file:
            query = file.read()
        print("SQL query read from file")
        db_connection = pg2.connect(
            database="piscineds",
            user="aaudevar",
            password="mysecretpassword",
            host="localhost",
            port="5432"
        )
        print("Connected to database")
        cursor = db_connection.cursor()
        cursor.execute(query)
        print("Query executed")
        db_connection.commit()
        print("Changes committed")
    except Exception as e:
        print(f"{type(e).__name__}: {e}")
    finally:
        cursor.close()
        db_connection.close()
        print("Connection closed")


def main():
    """
    Main function
    run the query from customers_table.sql
    """
    run_query("customers_table.sql")


if __name__ == "__main__":
    main()
