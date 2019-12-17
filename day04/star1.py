from main import is_valid

valid_passwords = 0
for password in range(123257, 647015):

    if is_valid(str(password)):
        valid_passwords += 1


print(f"Number of valid passwords: {valid_passwords}")
