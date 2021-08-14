def count_chars(my_str):
    my_str = my_str.replace(" ", "")
    dict_count_chars = dict()
    for char in my_str:
        value = 0
        if char in dict_count_chars.keys():
            value = dict_count_chars[char]
        value += 1
        dict_count_chars[char] = value
    return dict_count_chars


magic_str = "abra cadabra"
print(count_chars(magic_str))
