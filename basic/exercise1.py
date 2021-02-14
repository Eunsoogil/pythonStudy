username = input('username?')
password = input('password')
passwordLength = len(password)
passwordEncrypt = '*' * passwordLength

print(f'{username}, your password {passwordEncrypt} is {passwordLength} letters long')
