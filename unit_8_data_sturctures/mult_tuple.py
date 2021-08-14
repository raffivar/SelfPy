def mult_tuple(tuple1, tuple2):
    pair_list = list()
    for x in tuple1:
        for y in tuple2:
            pair_list.append((x, y))
            pair_list.append((y, x))
    return tuple(pair_list)


def mult_tuple2(tuple1, tuple2):
    tuples = [tuple1, tuple2]
    pair_list = [(i, j) for x in tuples for y in tuples for i in x for j in y if x is not y]
    return tuple(pair_list)


first_tuple = (1, 2)
second_tuple = (4, 5)
print(mult_tuple(first_tuple, second_tuple))

first_tuple = (1, 2, 3)
second_tuple = (4, 5, 6)
print(mult_tuple(first_tuple, second_tuple))
