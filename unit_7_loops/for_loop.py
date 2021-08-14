def is_greater(my_list, n):
    res = list()
    for number in my_list:
        if number > n:
            res.append(number)
    return res


result = is_greater([1, 30, 25, 60, 27, 28], 28)
print(result)
