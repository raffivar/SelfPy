def sequence_del(my_str):
    if len(my_str) == 0:
        return my_str
    else:
        res = my_str[0]
        curr_char = my_str[0]
        for char in my_str:
            if char != curr_char:
                curr_char = char
                res += char
        return res


print(sequence_del("ppyyyyythhhhhooonnnnn"))
print(sequence_del("SSSSsssshhhh"))
print(sequence_del("Heeyyy   yyouuuu!!!"))
