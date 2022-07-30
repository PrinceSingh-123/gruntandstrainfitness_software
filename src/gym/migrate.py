from importlib import resources
import sqlite3
from pathlib import Path
# code for connecting sqlite database
resources_folder = Path(__file__).joinpath("../resources").resolve()
db_filepath = resources_folder.joinpath("paradox.db")
sql_filepath = resources_folder.joinpath("schema.sql")

# making the connection with database...
con = sqlite3.connect(db_filepath)
cur = con.cursor()

with open(sql_filepath) as f:
    cur.executescript(f.read())

con.close()