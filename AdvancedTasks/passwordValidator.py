import string
import re
def passwordValidator(password):
    symbols = string.punctuation

    if not re.search('[A-Z]', password):
        return "Password must contain at least one uppercase letter"
    if not re.search('[a-z]', password):
        return "Password must contain at least one lowercase letter"
    if not re.search(f'[{symbols}]', password):
        return "Password must contain at least one symbol"

    return "Password is sucessfully validated"

print(passwordValidator("password"))
