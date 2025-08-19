import sqlite3
from sqlite3 import Error
import os
from dotenv import load_dotenv
from rich.console import Console


# load tables
console = Console()

# load environment.
load_dotenv()
path = os.getenv("SQLITEPATH")
print(path)


def create_connection(path):
    connection = None
    try:
        return sqlite3.connect(path)

    except Error as e:
        print(f"The Error '{e}' occurred")


def query_tables(cursor):
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()
    for table in tables:
        console.print(f"Table: {table}", style="red")


def execute_query(query, cursor):
    try:
        cursor.execute(query)
        results = cursor.fetchall()
        for result in results:
            console.print(result)
    except Exception as e:
        console.print(f"Error: {e}")


if __name__ == "__main__":
    conn = create_connection(path)
    cursor = conn.cursor()
    # query_tables(cursor)
    query = ''
    while query != None and query.upper() != 'EXIT':
        query = input("Please enter the Query: ")
        if query.upper() != 'EXIT':
            execute_query(query, cursor)

    cursor.close()
    conn.close()
