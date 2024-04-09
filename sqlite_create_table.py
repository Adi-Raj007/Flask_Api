import sqlite3

conn =sqlite3.connect('ipl.db')
#creating a cursor
c= conn.cursor()
#Creating a table
c.execute("""CREATE TABLE ipl_matches(
          id INTEGER PRIMARY KEY,
          date TEXT,
          winner TEXT,
          Loser TEXT,
          Score TEXT
)""")
conn.commit()
conn.close()