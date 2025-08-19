# database Connection to the Hana Database
import os
from dotenv import load_dotenv
from hdbcli import dbapi
from rich.console import Console

# print console.
console = Console()

# load environemnt variables
load_dotenv()

# Fetch SAP HANA credentials
HANA_HOST = os.getenv("HANA_HOST")
HANA_PORT = os.getenv("HANA_PORT")
HANA_USER = os.getenv("HANA_USER")
HANA_PASSWORD = os.getenv("HANA_PASSWORD")

# Ensure all required variables are set
if not all([HANA_HOST, HANA_PORT, HANA_USER, HANA_PASSWORD]):
    raise ValueError(
        "Error: Missing SAP HANA credentials. Check your .env file.")
conn = ''


def connection():

    conn = dbapi.connect(
        address=HANA_HOST,
        port=int(HANA_PORT),
        user=HANA_USER,
        password=HANA_PASSWORD
    )

    console.print(conn)
    cursor = conn.cursor()
    console.print(cursor)
    return cursor


# Function to close the database connection
def close_connection():
    """Close the database connection."""
    if conn:
        cursor.close()
        conn.close()
        console.print("Connection closed.")

# Function to fetch input query from the user


def fetch_inputquery():
    """Fetch input query from the user."""
    input_query = input("Enter your SQL query: ")
    return input_query


# Function to execute the SQL query
def execute_query(query, cursor):
    try:
        cursor.execute(query)
        results = cursor.fetchall()
        for row in results:
            console.print(row)
    except dbapi.Error as e:
        console.print(f"Error executing query: {e}")


# Main loop to fetch and execute queries
if __name__ == "__main__":
    cursor = connection()
    query = ''
    while query != 'exit':
        query = fetch_inputquery()
        if query.lower() == 'exit':
            close_connection()
            break
        execute_query(query, cursor)
