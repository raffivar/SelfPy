def shift_left1(my_list):
    return [my_list[1], my_list[2], my_list[0]]


def shift_left2(my_list):
    a, b, c = my_list
    return [b, c, a]


def shift_left3(my_list):
    if len(my_list) == 0:
        return list()
    else:
        return my_list[1:] + [my_list[0]]


print(shift_left2([0, 1, 2]))
print(shift_left2(['monkey', 2.0, 1]))
