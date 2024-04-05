from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, exc
import psycopg2
from helpers import get_db_connection_str, infer_column_types


def create_db_engine():
    try:
        engine = create_engine(
            get_db_connection_str(),
            echo=True)
        return engine
    except exc.SQLAlchemyError as err:
        print(f"Error creating the database engine: {err}")


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
