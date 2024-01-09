import string
import re
def passwordValidator(password):
    # using list
    symbols = string.punctuation
    failed_criteria = []

    if not re.search('[A-Z]', password):
        failed_criteria.append("Password must contain at least one uppercase letter")
    if not re.search('[a-z]', password):
        failed_criteria.append("Password must contain at least one lowercase letter")
    if not re.search(f'[{symbols}]', password):
        failed_criteria.append("Password must contain at least one symbol")

    if failed_criteria is None:
        return "Password is sucessfully validated"
    else:
        for criteria in failed_criteria:
            print(f'[error] - {criteria}')

        return "Password is not pass all criterias"

print(passwordValidator("password"))
