import sqlite3

conn = sqlite3.connect('myquotes.db')
curr = conn.cursor()

# curr.execute(""" create table quotes_db(
#                 content text,
#                 author text,
#                 tag text
#                 )""")

conn.commit()
conn.close()