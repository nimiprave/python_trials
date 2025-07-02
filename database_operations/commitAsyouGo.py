from sqlalchemy import create_engine
from sqlalchemy import text

# Engine is the interface to the database
engine = create_engine("sqlite+pysqlite:///:memory:", echo=True)

# commit as you go
with engine.connect() as conn:
    conn.execute(text("CREATE TABLE axis( x int, y int)"))
    conn.execute(
        text("INSERT INTO axis (x, y) values (:x, :y)"),
        [{"x": 1, "y": 2}, {"x": 3, "y": 5}]
    )
    result = conn.execute(text("SELECT * from axis"))
    print(result.all())
    conn.commit()
