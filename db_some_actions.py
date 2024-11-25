import sqlite3

DB_NAME = 'words_list.db'

with open('words-russian-nouns.sql', 'rt', encoding='utf-8') as f:
    sql_script = f.read()

with sqlite3.connect(DB_NAME) as conn:
    cursor = conn.cursor()
    cursor.executescript(sql_script)
    cursor.execute("ALTER TABLE nouns ADD COLUMN new_IID INTEGER;")
    cursor.execute("WITH numbered_rows AS (SELECT ROW_NUMBER() OVER (ORDER BY IID) AS new_id, ROWID "
                   "FROM nouns) UPDATE nouns SET new_IID = (SELECT new_id FROM numbered_rows WHERE numbered_rows.ROWID = nouns.ROWID);")
    conn.commit()
