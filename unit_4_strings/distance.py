def near(num1, num2):
    return abs(num1 - num2) <= 1


def first_far_from_others(num1, num2, num3):
    return abs(num1 - num2) > 1 and abs(num1 - num3) > 1


def distance(num1, num2, num3):
    return (near(num2, num1) or near(num3, num1)) and \
           (first_far_from_others(num2, num1, num3) or first_far_from_others(num3, num1, num2))


print(distance(1, 2, 10))
print(distance(4, 5, 3))
