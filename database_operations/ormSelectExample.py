from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from sqlalchemy import text
from rich.console import Console

# console
console = Console()


# function to create a table
def create_table(session):
    session.execute(text('create table axis ( x int, y int)'))


def insert_table(session, params):
    session.execute(text('insert into axis ( x, y ) values (:x, :y)'), params)


def select_table(session, params):
    if params:
        return session.execute(text('select x, y from axis'))
    else:
        return session.execute(text('select x, y from axis'), params)


def dynamic_query(session):
    session.execute("update axis set x")


if __name__ == "__main__":

    # create engine
    engine = create_engine("sqlite+pysqlite:///:memory:")
    session = Session(engine)
    create_table(session)

    # insert into table
    insert_table(session, [{"x": 1, "y": 2}, {
                 "x": 3, "y": 4}, {"x": 5, "y": 6}])

    # select from table
    result = select_table(session, None)

    for row in result:
        console.print(row)
