from sqlalchemy import create_engine
from sqlalchemy import text


# create the engine interface.
engine = create_engine('sqlite+pysqlite:///:memory:', echo=True)


# create connection
with engine.connect() as conn:

    ##
    result = conn.execute(text("select 'Hello World'"))
    print(result.all())
    # create a table
    conn.execute(text(
        "create table axis ( x int, y int)"
    ))
    # insert into a table
    conn.execute(text(
        "insert into axis (x , y) values (:x, :y)"
    ), [{"x": 1, "y": 2}, {"x": 5, "y": 6}])
    conn.commit()
