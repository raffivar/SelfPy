s = input("degrees: ")
degree_val = float(s[:-1])
degree_type = s[-1]
degree_type = degree_type.lower()

if degree_type == 'c':
    print((9 * degree_val + 160)/5)
elif degree_type == 'f':
    print((5 * degree_val - 160) / 9)
else:
    print("Illegal degrees")
