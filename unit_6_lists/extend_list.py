def extend_list_x(list_x, list_y):
    list_x[0:0] = list_y


x = [4, 5, 6]
y = [1, 2, 3]
extend_list_x(x, y)
print(x)
