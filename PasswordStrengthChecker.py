password = input("Enter password: ")

length_ok = len(password) >= 8
upper = any(c.isupper() for c in password)
lower = any(c.islower() for c in password)
digit = any(c.isdigit() for c in password)
special = any(not c.isalnum() for c in password)

score = sum([length_ok, upper, lower, digit, special])

if score <= 2:
    print("Weak")
elif score == 3 or score == 4:
    print("Medium")
else:
    print("Strong")
