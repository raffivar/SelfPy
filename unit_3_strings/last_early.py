def last_early(my_str):
    my_str = my_str.lower()
    last_char = my_str[-1]
    return my_str.count(last_char) > 1


print(last_early("happy birthday"))
print(last_early("best of luck"))
print(last_early("Wow"))
print(last_early("X"))
