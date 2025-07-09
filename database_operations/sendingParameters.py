# Sending Parameters
# SQL statements are usually accompanied by data that is to be passed with the statement itself,
# as we saw in the INSERT example previously. The Connection.execute() method therefore also accepts parameters, which are known as bound parameters.
# A rudimentary example might be if we wanted to limit our SELECT statement only to rows that meet a certain criteria,
# such as rows where the “y” value were greater than a certain value that is passed in to a function.
# In order to achieve this such that the SQL statement can remain fixed and that the driver can properly sanitize the value,
# we add a WHERE criteria to our statement that names a new parameter called “y”; the text() construct accepts these using a colon format “:y”.
# The actual value for “:y” is then passed as the second argument to Connection.execute() in the form of a dictionary:

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
