from sqlalchemy import create_engine
from sqlalchemy import text

# Engine is the interface to the database
engine = create_engine("sqlite+pysqlite:///:memory:", echo=True)

# Connection object non scoped type.
connection = engine.connect()
result = connection.execute(text("select 'hello world'"))
print(result.all())


# from sqlalchemy import create_engine
# from sqlalchemy import MetaData, Table
# from rich.console import Console

# console = Console()
# engine = create_engine('sqlite:///census_nyc.sqlite')
# # print(engine.table_names())
# connection = engine.connect()

# # Metadata
# metadata = MetaData()
# census = Table('census', metadata, autoload_with=engine)
# print(repr(census))
