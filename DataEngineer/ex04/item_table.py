import pandas as pd
from sqlalchemy import (
    BigInteger,
    create_engine,
    MetaData,
    Integer,
    String
)


def is_table_exist(engine, table_name):
    """
    Function that check if a table exist in a database

    Arguments:
        engine {sqlalchemy.engine.base.Engine} -- SQLAlchemy engine
        table_name {str} -- Table name

    Returns:
        bool -- True if the table exist, False otherwise
    """
    metadata = MetaData()
    metadata.reflect(bind=engine)
    if table_name in metadata.tables:
        print(f"Table {table_name} already exist.")
    return table_name in metadata.tables


def create_item_table(path, table_name):
    """
    Function that create a table in a database

    Arguments:
        engine {sqlalchemy.engine.base.Engine} -- SQLAlchemy engine
        table_name {str} -- Table name
    """
    try:
        engine = create_engine("postgresql://aaudevar:mysecretpassword@\
localhost:5432/piscineds")
        if not is_table_exist(engine, table_name):
            print(f"Creating table {table_name}...")
            data = pd.read_csv(path)
            data_types = {
                'product_id': Integer(),
                'category_id': BigInteger(),
                'category_code': String(length=255),
                'brand': String(length=255),
            }
            data.to_sql(table_name, engine, index=False, dtype=data_types)
            print(f"Table {table_name} created.")
        engine.dispose()
    except Exception as e:
        print(f"{type(e).__name__}: {e}")


def main():
    """
    Main function
    """
    create_item_table("/home/skall/item/item.csv", "items")


if __name__ == "__main__":
    main()
