import os

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
    """
    Prints current state of hangman
    depending on num of failed guesses.
    :param num_of_tries: number of failed guesses
    :type num_of_tries: int
    """
    print(HANGMAN_PHOTOS[num_of_tries + 1])


def choose_word(file_path, index):
    """
    Calculates the number of distinct words in a file and
    chooses a word to be the 'secret word'.
    :param file_path: path of file
    :type file_path: string
    :param index: index of a word in file (1 = first word)
    :type index: int
    :return: number of distinct words in file + the 'secret word'
    :rtype: tuple
    """
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
    """
    Prints out the current state of the word
    depending on the letters already guessed.
    :param secret_word: the secret word
    :type secret_word: string
    :param old_letters_guessed: a list of all the letters guessed so far
    :type old_letters_guessed: list
    :return: The number of distinct words in file + the chosen word
    :rtype: tuple
    """
    result = ""
    for char in secret_word:
        if char in old_letters_guessed:
            result += char + ' '
        else:
            result += '_ '
    print(result, '\n')


def is_valid_input(letter_guessed, old_letters_guessed):
    """
    Determines whether or not the input is 'valid'
    the letter is 'valid' of all the following conditions apply:
        1. The letter is one character
        2. The letter is not as special character
        3. The letter has never been guessed before
    :param letter_guessed: current guessed letter
    :type letter_guessed: string
    :param old_letters_guessed: a list of all the letters guessed so far
    :type old_letters_guessed: list
    :return: True if valid, False if otherwise
    :rtype: bool
    """
    return len(letter_guessed) == 1 and \
        letter_guessed.isalpha() and \
        letter_guessed.lower() not in old_letters_guessed


def try_update_letter_guessed(letter_guessed, old_letters_guessed):
    """
    Updates list of already guessed letters
    with currently guessed letter
    depending on whether or not the letter is valid.
    :param letter_guessed: current guessed letter
    :type letter_guessed: string
    :param old_letters_guessed: a list of all the letters guessed so far
    :type old_letters_guessed: list
    :return: True if guessed_letter is valid (addition was successful),
             False otherwise
    :rtype: bool
    """
    if not is_valid_input(letter_guessed, old_letters_guessed):
        print('X\n{}'.format(' -> '.join(old_letters_guessed)))
        return False
    else:
        old_letters_guessed.append(letter_guessed.lower())
        return True


def is_win(secret_word, old_letters_guessed):
    """
    Determines whether or not the player has won
    depending if all the words in the secret word
    have already been guessed.
    :param secret_word: the secret word
    :type secret_word: string
    :param old_letters_guessed: a list of all the letters guessed so far
    :type old_letters_guessed: list
    :return: True if player has won, False otherwise
    :rtype: bool
    """
    for char in secret_word:
        if char not in old_letters_guessed:
            return False
    return True


def main():
    print("Welcome to the game Hangman\n", hangman_art.HANGMAN_ASCII_ART, "\n")

    file_path = input("Please supply file path: ")
    while not os.path.isfile(file_path):
        file_path = input("File does not exist, please try again: ")

    index = input("Please supply index: ")
    while not index.isnumeric() or int(index) < 1:
        index = input("Invalid index (must be 1+), please try again: ")
    index = int(index)

    secret_word = choose_word(file_path, index)[1]
    old_letters_guessed = []
    tries = 0

    print_hangman(tries)
    show_hidden_word(secret_word, old_letters_guessed)
    while not is_win(secret_word, old_letters_guessed) and tries < MAX_TRIES:
        letter_guessed = input("Enter your guess: ")
        valid = try_update_letter_guessed(letter_guessed, old_letters_guessed)
        if not valid:
            continue
        if letter_guessed not in secret_word:
            print(':(')
            tries += 1
            print_hangman(tries)
        show_hidden_word(secret_word, old_letters_guessed)

    if is_win(secret_word, old_letters_guessed):
        print("WIN!")
    else:
        print("LOSE")

    print("The word was: '{}'".format(secret_word))


if __name__ == "__main__":
    main()
