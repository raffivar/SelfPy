s = input("Please insert input: AAAA")
mid = len(s)//2
first_half = s[:mid]
second_half = s[mid:]
print(first_half.lower() + second_half.upper())
