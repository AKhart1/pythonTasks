import datetime
def ageCalclator(birthYear):
    current_year = datetime.now().year
    age = current_year - birthYear
    return age

print(ageCalclator(2000))