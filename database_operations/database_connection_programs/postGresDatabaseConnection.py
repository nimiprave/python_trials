import psycopg2
import os
from dotenv import load_dotenv


# load environment variables:
load_dotenv()


# load enviroment properties
def load_environment():

    postgres_properties = {}
    postgres_properties["database"] = os.getenv("POSTGRES_DATABASE")
    postgres_properties["password"] = os.getenv("POSTGRES_PWD")
    postgres_properties["host"] = os.getenv("POSTGRES_HOST")
    postgres_properties["port"] = os.getenv("POSTGRES_PORT")
    postgres_properties["user"] = os.getenv("POSTGRES_USER")
    return postgres_properties


# establish connection
def database_connection(properties):
    conn = psycopg2.connect(
        database=properties["database"],
        user=properties["user"],
        password=properties["password"],
        host=properties["host"],
        port=properties["port"]
    )
    return conn


if __name__ == "__main__":

    # read the properties
    properties = load_environment()
    print(properties)

    # read the connection
    connection = database_connection(properties)

    # Create the cursor object
    cursor = connection.cursor()

    # Execute a simple query
    cursor.execute("SELECT version();")

    # Fetch the result
    db_version = cursor.fetchone()
    print(f"PostgreSQL database version: {db_version}")

    # Close the cursor and connection
    cursor.close()
    connection.close()
