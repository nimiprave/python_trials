# Sending parameters
from sqlalchemy import create_engine
from sqlalchemy import text
from rich.console import Console

# console
console = Console()

# create engine
engine = create_engine('sqlite+pysqlite:///:memory:', echo=True)


def create_table(conn):
    conn.execute(text("create table axis ( x  int, y int)"))
    conn.execute(text("insert into axis ( x , y ) values ( :x ,:y )"), [
                 {"x": 2, "y": 4}, {"x": 6, "y": 8}, {"x": 10, "y": 12}])


def read_table(conn):
    result = conn.execute(text('select x, y from axis'))
    console.print(result.all())


def dynamic_query(conn, sql, params):
    if sql and params:
        result = conn.execute(text(sql), params)
        console.print(result.all())


if __name__ == "__main__":
    connection = engine.connect()
    create_table(connection)
    read_table(connection)
    dynamic_query(connection, "select x, y from axis where y > :y", {"y": 6})
