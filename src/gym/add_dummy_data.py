import sqlite3
from pathlib import Path
# code for connecting sqlite database
resources_folder = Path(__file__).joinpath("../resources").resolve()
db_filepath = resources_folder.joinpath("paradox.db")

con = sqlite3.connect(db_filepath)
cur = con.cursor()

query = """
    Insert into Staffs (name,position,salary,date_joined) values 
    ('test', 'something', 2000, '2022-01-01 10:00:00'),
    ('test', 'something', 3000, '2022-02-01 10:00:00'),
    ('test', 'something', 4000, '2022-03-01 10:00:00'),
    ('test', 'something', 5000, '2022-07-01 10:00:00');
"""

cur.execute(query)

con.commit()
con.close()