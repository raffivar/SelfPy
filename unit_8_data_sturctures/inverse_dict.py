def inverse_dict(my_dic):
    inverse = dict()
    for key in my_dic.keys():
        new_key = my_dic[key]
        new_value = key
        if new_key not in inverse.keys():
            inverse[new_key] = [new_value]
        else:
            inverse[new_key].append(new_value)
    return inverse


course_dict = {'I': 3, 'love': 3, 'self.py!': 2}
print(inverse_dict(course_dict))
