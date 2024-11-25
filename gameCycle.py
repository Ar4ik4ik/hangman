import sqlite3
from db_some_actions import DB_NAME
import random


def get_random_word():
    with sqlite3.connect(DB_NAME) as conn:
        word_n = random.randint(1, 65500)
        SQL_REQUEST = f"SELECT word FROM nouns WHERE new_IID={word_n}"
        word = conn.execute(SQL_REQUEST).fetchone()
        return word[0]


def set_game(word: str):
    hidden_word = '_' * len(word)
    mistakes_count = 0
    hangman_img = print_hangman(0)
    while mistakes_count != 6:
        print(hidden_word)
        input_chr = input("Please enter the char: ")
        if input_chr in word:
            for char, i in enumerate(word):
                if input_chr == char:
                    converted_word = list(word)
                    converted_word[i] = char
                    hidden_word = str(converted_word)
        # else:


# ._____
# |    |
# |    o
# |   /|\
# |   / \
# |
def print_hangman(mistakes: int) -> str:
    start_img = ("                  ._____\n"
                 "                  |    |\n"
                 "                  |     \n"
                 "                  |     \n"
                 "                  |     \n"
                 "                  |")
    stripped_img = start_img.split('\n')
    if mistakes == 1:
        stripped_img[2] = "                  |    o     "
    elif mistakes == 2:
        stripped_img[2] = "                  |    o     "
        stripped_img[3] = "                  |    |     "
    elif mistakes == 3:
        stripped_img[2] = "                  |    o     "
        stripped_img[3] = "                  |   /|     "
    elif mistakes == 4:
        stripped_img[2] = "                  |    o     "
        stripped_img[3] = "                  |   /|\\   "
    elif mistakes == 5:
        stripped_img[2] = "                  |    o     "
        stripped_img[3] = "                  |   /|\\   "
        stripped_img[4] = "                  |   /      "
    elif mistakes == 6:
        stripped_img[2] = "                  |    o     "
        stripped_img[3] = "                  |   /|\\   "
        stripped_img[4] = "                  |   / \\   "
    print('\n'.join(stripped_img))


print_hangman(1)