import string
import random
def passwordGenerator(length):
    letters = string.ascii_letters
    digits = string.digits
    symbols = string.punctuation

    if length < 8:
        print('Password must be at least 8 characters long')

    characters = letters + digits + symbols
    password = ''.join(random.choice(characters) for _ in range(length))

    return password

x = 1
while x <= 10:
    print(f'{[x]} {passwordGenerator(16)}')
    x += 1