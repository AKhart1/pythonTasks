import datetime
def daysUntilBirthday():
    user_birthday = input("Enter your birthday in YYYY-MM-DD format: ")
    birthday = datetime.strptime(user_birthday, "%Y-%m-%d")

    today = datetime.now()
    nextBirthday = birthday.replace(year=today.year)
    if nextBirthday < today:
        nextBirthday = nextBirthday.replace(year=today.year + 1)
    days_left = (nextBirthday - today).days
    return days_left

print(daysUntilBirthday())