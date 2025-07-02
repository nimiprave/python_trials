from sqlalchemy import create_engine
from sqlalchemy import text

# interface for the database
engine = create_engine("sqlite+pysqlite:///:memory:", echo=True)

# begin once approach
with engine.begin() as conn:
    conn.execute(
        text("create table axis( x int, y int)")
    )
    conn.execute(text("insert into axis( x, y ) values ( :x , :y)"), [
        {'x': 2, 'y':  4}, {'x': 6, 'y':  8}])
    # conn.commit()
    result = conn.execute(text(" select * from axis "))
    print(result.all())
