from table import create_table
import os


def create_all_tables(folder_path):
    """
    Function that create all tables in a database

    Arguments:
        folder_path {str} -- Folder path
    """
    for file in os.listdir(folder_path):
        if file.endswith(".csv"):
            table_name = file.split(".")[0]
            create_table(os.path.join(folder_path, file), table_name)


def main():
    create_all_tables("/home/skall/customer")


if __name__ == "__main__":
    main()
