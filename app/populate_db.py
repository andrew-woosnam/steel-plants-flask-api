from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, exc
import psycopg2
from helpers import get_db_connection_str


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

    test_table = Table(
        'test_table', metadata,
        Column('id', Integer, primary_key=True),
        Column('value', String(255)),
    )

    try:
        metadata.create_all(engine)
        print("Tables created successfully.")
    except exc.SQLAlchemyError as err:
        print(f"Error creating tables: {err}")


if __name__ == "__main__":
    engine = create_db_engine()
    if engine:
        create_tables(engine)
