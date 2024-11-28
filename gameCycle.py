import sqlite3
from db_some_actions import DB_NAME
import random


def get_random_word():
    with sqlite3.connect(DB_NAME) as conn:
        word_n = random.randint(1, 65500)
        SQL_REQUEST = f"SELECT word FROM nouns WHERE new_IID={word_n}"
        word = conn.execute(SQL_REQUEST).fetchone()
        return word[0]


def show_char(input_word, hidden_word, entered_char):
    for i, char in enumerate(input_word):
        if char == entered_char:
            hidden_word[i] = entered_char
    return hidden_word


def set_game():
    word = get_random_word()
    hidden_word = ['_'] * len(word)
    mistakes_count = 0
    exists_chrs = []
    while mistakes_count != 6:
        print(' '.join(hidden_word))
        input_chr = input("Please enter the char: ").lower()
        code = ord(input_chr)
        if not input_chr.isalpha() or (code < 1040 or code > 1103):
            continue
        if input_chr in exists_chrs:
            continue
        exists_chrs.append(input_chr)

        if input_chr in word:
            show_char(word, hidden_word, input_chr)
        else:
            mistakes_count += 1
            print_hangman(mistakes_count)
            print('\n')
            print('\n')
            print(f"Количество ошибок: {mistakes_count}")

        if ''.join(hidden_word) == word:
            print("Ты выиграл !")
            exit_or_start()

    print(f"Ты проиграл !\n"
          f"{' '.join(hidden_word)}")
    exit_or_start()
    return


def print_hangman(mistakes: int):
    start_img = ("          __._____\n"
                 "            |    |\n"
                 "            |     \n"
                 "            |     \n"
                 "            |     \n"
                 "           /|\\\n"
                 "===================")
    stripped_img = start_img.split('\n')
    if mistakes == 1:
        stripped_img[2] = "            |    o     "
    elif mistakes == 2:
        stripped_img[2] = "            |    o     "
        stripped_img[3] = "            |    |     "
    elif mistakes == 3:
        stripped_img[2] = "            |    o     "
        stripped_img[3] = "            |   /|     "
    elif mistakes == 4:
        stripped_img[2] = "            |    o     "
        stripped_img[3] = "            |   /|\\   "
    elif mistakes == 5:
        stripped_img[2] = "            |    o     "
        stripped_img[3] = "            |   /|\\   "
        stripped_img[4] = "            |   /      "
    elif mistakes == 6:
        stripped_img[2] = "            |    o     "
        stripped_img[3] = "            |   /|\\   "
        stripped_img[4] = "            |   / \\   "
    print('\n'.join(stripped_img))


def exit_or_start():
    if input('Exit or start new game ?: ') == 'start':
        set_game()


exit_or_start()
