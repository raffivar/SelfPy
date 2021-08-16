import random

import hangman_art

MAX_TRIES = 6
HANGMAN_PHOTOS = {1: hangman_art.picture1,
                  2: hangman_art.picture2,
                  3: hangman_art.picture3,
                  4: hangman_art.picture4,
                  5: hangman_art.picture5,
                  6: hangman_art.picture6,
                  7: hangman_art.picture7}


def print_hangman(num_of_tries):
    print(HANGMAN_PHOTOS[num_of_tries + 1])


def choose_word(file_path, index):
    words = []
    word_in_index = ""
    with open(file_path, "r") as file:
        words_from_file = file.read().split(' ')
        index = index % len(words_from_file)
    for i in range(0, len(words_from_file)):
        word = words_from_file[i]
        if word not in words:
            words.append(word)
        if i == index - 1:
            word_in_index = word
    return len(words), word_in_index


def show_hidden_word(secret_word, old_letters_guessed):
    result = ""
    for char in secret_word:
        if char in old_letters_guessed:
            result += char + ' '
        else:
            result += '_ '
    print(result, '\n')


def is_valid_input(letter_guessed, old_letters_guessed):
    return len(letter_guessed) == 1 and letter_guessed.isalpha() and letter_guessed.lower() not in old_letters_guessed


def try_update_letter_guessed(letter_guessed, old_letters_guessed):
    if not is_valid_input(letter_guessed, old_letters_guessed):
        print('X')
        print(' -> '.join(old_letters_guessed))
        return False
    else:
        old_letters_guessed.append(letter_guessed)
        return True


def check_win(secret_word, old_letters_guessed):
    for char in secret_word:
        if char not in old_letters_guessed:
            return False
    return True


def main():
    print("Welcome to the game Hangman\n", hangman_art.HANGMAN_ASCII_ART, "\n")
    index = random.randint(0, 500)
    secret_word = choose_word('words.txt', index)[1]
    old_letters_guessed = []
    tries = 0

    while not check_win(secret_word, old_letters_guessed) and tries < MAX_TRIES:
        print_hangman(tries)
        show_hidden_word(secret_word, old_letters_guessed)
        letter_guessed = input("Enter your guess: ")
        try_update_letter_guessed(letter_guessed, old_letters_guessed)
        tries += 1

    if check_win(secret_word, old_letters_guessed):
        print("YOU WON! :D")
    else:
        print("YOU LOST! T_T")

    print("The word was: '{}'".format(secret_word))


if __name__ == "__main__":
    main()
