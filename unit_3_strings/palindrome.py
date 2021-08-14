s = input("is palindrome: ")
s = s.lower()
s = s.replace(' ', '')

print(s + " == " + s[::-1] + " ? ")
if s == s[::-1]:
    print('OK')
else:
    print('NOT')
