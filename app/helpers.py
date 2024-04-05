import csv
import os
from sqlalchemy import Integer, String


def get_db_connection_str():
    username = os.getenv('POSTGRES_USER')
    password = os.getenv('POSTGRES_PASSWORD')
    database_name = os.getenv('POSTGRES_DB')
    host = os.getenv('POSTGRES_HOST', 'localhost')
    port = os.getenv('POSTGRES_PORT', '5432')
    return f'postgresql://{username}:{password}@{host}:{port}/{database_name}'


def infer_column_types(csv_file):
    with open(csv_file, 'r') as file:
        reader = csv.reader(file)
        headers = next(reader)

        column_types = {}
        for header in headers:
            col_name = format_as_column_name(header)
            column_types[col_name] = String(255)  # assume all strings

        first_row = next(reader)  # sample data from 1st row
        for i, value in enumerate(first_row):
            col_name = format_as_column_name(headers[i])
            try:
                # Try to convert to integer
                int(value)
                column_types[col_name] = Integer()
            except ValueError:
                try:
                    # Try to convert to float
                    float(value)
                    column_types[headers[i]] = Float()
                except ValueError:
                    # keep as String
                    pass
        return column_types


def format_as_column_name(str):
    # Replace spaces with underscores, remove special characters, and convert to lowercase
    formatted_str = ''.join('_' if c.isspace() else c.lower()
                            for c in str if c.isalnum() or c.isspace())
    return formatted_str
