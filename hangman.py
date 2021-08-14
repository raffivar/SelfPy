import hangman_art

MAX_TRIES = 6


def is_valid_input(guess, old_guesses):
    return len(guess) == 1 and guess.isalpha() and guess.lower() not in old_guesses


def try_update_letter_guessed(letter_guessed, old_letters_guessed):
    if not is_valid_input(letter_guessed, old_letters_guessed):
        print('X')
        print(' -> '.join(old_letters_guessed))
        return False
    else:
        old_letters_guessed.append(letter_guessed)
        return True


def show_hidden_word(secret_word, old_letters_guessed):
    result = ""
    for char in secret_word:
        if char in old_letters_guessed:
            result += char + ' '
        else:
            result += '_ '
    return result


def check_win(secret_word, old_letters_guessed):
    for char in secret_word:
        if char not in old_letters_guessed:
            return False
    return True


print("Welcome to the game Hangman\n", hangman_art.HANGMAN_ASCII_ART, "\n")

# old_letters = ['a', 'p', 'c', 'f']
# print(is_valid_input('C', old_letters))
# print(is_valid_input('ep', old_letters))
# print(is_valid_input('$', old_letters))
# print(is_valid_input('s', old_letters))
# print()
# print(try_update_letter_guessed('A', old_letters), "\n")
# print(try_update_letter_guessed('s', old_letters), "\n")
# print(old_letters, "\n")
# print(try_update_letter_guessed('$', old_letters), "\n")
# print(try_update_letter_guessed('d', old_letters), "\n")
# print(old_letters)

# print(show_hidden_word("mammals", ['s', 'p', 'j', 'i', 'm', 'k']))

# print(check_win("friends", ['m', 'p', 'j', 'i', 's', 'k']))
# print(check_win("yes", ['d', 'g', 'e', 'i', 's', 'k', 'y']))
