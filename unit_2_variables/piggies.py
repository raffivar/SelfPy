digits = input("Enter three digits (each digit for one pig): ")
digits = int(digits)
ones = digits % 10
tens = (digits // 10) % 10
hundreds = digits // 100
total = ones + tens + hundreds

print(total)
print(total // 3)
print(total % 3)
print(total % 3 == 0)
