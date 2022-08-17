import sqlite3

conn = sqlite3.connect('data.db')
curs = conn.cursor()

create_table = "CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username text, password text, email text)"
curs.execute(create_table)

create_table = "CREATE TABLE IF NOT EXISTS articles (title text, body text)"
curs.execute(create_table)

conn.commit()
conn.close()
