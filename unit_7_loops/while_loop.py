def squared_numbers(start, stop):
    my_list = []
    while start <= stop:
        my_list.append(start ** 2)
        start += 1
    return my_list


print(squared_numbers(4, 8))
print(squared_numbers(-3, 3))
