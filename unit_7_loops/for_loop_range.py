def numbers_letters_count(my_string):
    num_of_digits = 0
    num_of_letters = 0
    for char in my_string:
        if char.isdigit():
            num_of_digits += 1
        else:
            num_of_letters += 1
    return [num_of_digits, num_of_letters]


print(numbers_letters_count("Python 3.6.3"))
