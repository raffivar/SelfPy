data = ("self", "py", 1.543)

format_string1 = 'Hello %s.%s learner, ' \
                 'you have only %.1f units left before you master the course!'
print(format_string1 % data)

format_string2 = 'Hello {}.{} learner, ' \
                 'you have only {:.1f} units left before you master the course!'
print(format_string2.format("self", "py", 1.543))



