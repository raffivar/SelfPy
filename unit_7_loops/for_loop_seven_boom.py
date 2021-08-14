def seven_boom(end_number):
    res = list()
    for num in range(1, end_number + 1):
        if (num % 7 == 0) or ('7' in str(num)):
            res.append('BOOM')
        else:
            res.append(num)
    return res


print(seven_boom(17))
