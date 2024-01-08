import random
import time
from datetime import datetime
# from forex_python.converter import CurrencyRates

def stringReverser(text):
    return text[::-1]

# print(stringReverser("Hello World! My name is Alex"))

def listSorter():
    user_input = input("Enter the numbers separated by space: ")
    numbers = user_input.split(' ')
    numbers.sort()
    print('Sorted list: ', numbers )

# listSorter()

def ageCalclator(birthYear):
    current_year = datetime.now().year
    age = current_year - birthYear
    return age

# print(ageCalclator(2000))

def temperatureConverter():
    temperature = int(input("Enter the temperature: "))
    user_input = input("Enter the scale of temperature: ")

    match user_input:
        case "Fahrenheit":
            print((temperature * 9/5) + 32)
        case "Celsius":
            print((temperature - 32) * 5/9)

# temperatureConverter()

def simpleCalculator():
    numbers = input("Enter the numbers separated by space: ")
    action = input("Enter the action to perform (add,sub,mul,div): ")

    numbers = numbers.split(' ')
    x = int(numbers[0])
    y = int(numbers[1])

    match action:
        case 'add':
            return x + y
        case 'sub':
            return x - y
        case 'mul':
            return x * y
        case 'div':
            if y == 0:
                return "Cannot divide by zero"
            return x / y

# print(simpleCalculator())

def wordCounter():
    user_input = input("Enter the sentence: ")
    words = user_input.split()
    return len(words)

# print(wordCounter())

def daysUntilBirthday():
    user_birthday = input("Enter your birthday in YYYY-MM-DD format: ")
    birthday = datetime.strptime(user_birthday, "%Y-%m-%d")

    today = datetime.now()
    nextBirthday = birthday.replace(year=today.year)
    if nextBirthday < today:
        nextBirthday = nextBirthday.replace(year=today.year + 1)
    days_left = (nextBirthday - today).days
    return days_left

# print(daysUntilBirthday())

def guessNumber(random_number):
    guess = None

    while guess != random_number:
        guess = int(input("Guess a number between 1 and 100 : "))
        if guess < random_number:
            print("Too low, try again")
        elif guess > random_number:
            print("Too high, try again")
        else:
            print("Correct! You guessed the number.")
            break

# print(guessNumber(random.randint(1, 100)))

def setAlarm(alarm_time):
    while True:
        current_time = time.strftime("%H:%M")
        if current_time == alarm_time:
            return "Alarm! Wake up!"
        time.sleep(30)

# print(setAlarm("11:38"))

# def convert_currency(amount, from_currency, to_currency):
#     c = CurrencyRates()
#     result = c.convert(from_currency, to_currency, amount)
#     return f"{amount} {from_currency} is equal to {result} {to_currency}"