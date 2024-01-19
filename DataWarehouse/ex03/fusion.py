from customers_table import run_query


def main():
    """
    Main function
    create a new items table without duplicates
    and then fusion items and customers tables
    """
    run_query("remove_dup.sql")
    run_query("fusion.sql")


if __name__ == "__main__":
    main()
