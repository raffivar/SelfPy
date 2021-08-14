def format_list(whole_list):
    even_list = whole_list[::2]
    list_as_str = ', '.join(even_list)
    list_as_str += ', and ' + whole_list[-1]
    return list_as_str


my_list = ["hydrogen", "helium", "lithium", "beryllium", "boron", "magnesium"]
print(format_list(my_list))
