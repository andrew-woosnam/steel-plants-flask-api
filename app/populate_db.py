from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, exc
import psycopg2
from helpers import get_db_connection_str, infer_column_types
from time import sleep


def create_db_engine(retry_interval=5, max_retries=10):
    retries = 0
    while retries < max_retries:
        try:
            engine = create_engine(
                get_db_connection_str(),
                echo=True)
            # Attempt to connect to the database to check if it's ready
            with engine.connect() as conn:
                print("Database is ready!")
                return engine
        except (exc.SQLAlchemyError, psycopg2.OperationalError) as err:
            print("Database not ready, retrying in {} seconds ({}/{})...".format(
                retry_interval, retries+1, max_retries))
            retries += 1
            sleep(retry_interval)
    print("Error: Database did not become ready in time")
    return None


def create_tables(engine):
    metadata = MetaData()

    # Start with the primary key column
    columns = [Column('id', Integer, primary_key=True)]

    column_types = infer_column_types("data/steel-plants.csv")
    columns.extend([Column(header, col_type)
                   for header, col_type in column_types.items()])

    # Create the table with the dynamic columns
    table = Table('plants_table', metadata, *columns)

    try:
        metadata.create_all(engine)
        print("Tables created successfully.")
    except exc.SQLAlchemyError as err:
        print(f"Error creating tables: {err}")


if __name__ == "__main__":
    engine = create_db_engine()
    if engine:
        create_tables(engine)
