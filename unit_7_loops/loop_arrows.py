def arrow(my_char, max_length):
    res = ""
    for amount in range(1, max_length + 1):
        res += (my_char + ' ') * amount
        res += '\n'
    for amount in range(max_length - 1, 0, -1):
        res += (my_char + ' ') * amount
        res += '\n'
    return res


print(arrow('*', 5))
