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

    # creating a select query:
    result = conn.execute(text("select x, y from axis"))
    for row in result:
        print(row)
        print(row[0])
        print(f"x : {row.x} y : {row.y}")

    # Note: The Result object is mutable, once the values are read it become null.
    # example of using the row mapping, therefore rows becomes an dictionary.
    copy_result = conn.execute(text("select x, y from axis"))
    if copy_result is not None:
        for dict_row in copy_result.mappings():
            print(f"Dictionary mapping of a row")
            print(f"x: {dict_row["x"]}  , y:{dict_row["y"]}")
