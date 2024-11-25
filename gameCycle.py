import sqlite3
from db_some_actions import DB_NAME
import random

def get_random_word():
    with sqlite3.connect(DB_NAME) as conn:
        word_n = random.randint(1, 65500)
        SQL_REQUEST = f"SELECT word FROM nouns WHERE new_IID={word_n}"
        word = conn.execute(SQL_REQUEST).fetchone()
        return word[0]


















