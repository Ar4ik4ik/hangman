import sqlite3
import gzip


DB_NAME = 'words_list.db'


with open('words-russian-nouns.sql', 'rt', encoding='utf-8') as f:
    sql_script = f.read()

conn = sqlite3.connect(DB_NAME)
cursor = conn.cursor()

cursor.executescript(sql_script)
conn.commit()
conn.close()












