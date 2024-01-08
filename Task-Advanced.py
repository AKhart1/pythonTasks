import datetime


def PalindromeCheker():
    str = input("Enter a string : ")
    clean_text = ''
    for char in str :
        if char.isalnum():
            clean_text += char.lower()

    return clean_text == clean_text[::-1]

# print(PalindromeCheker())

def IsPrime(num):
    if num < 1:
        return False
    for i in range(2,int(num ** 1/2) + 1):
        if num % i == 0:
            return False
    return True

def primeNumberFinder():
    numbers = int(input("Enter the number of prime numbers : "))
    primes = [num for num in range(2,numbers+1) if IsPrime(num)]
    return primes

# print(primeNumberFinder())

def LogBook():
    action = input("Do you want to 'write' or 'display' ? ")

    if action == "write":
        log = input("Enter the log to the logbook : ")
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open("logbook.txt", "a") as file:
            file.write(f'{timestamp} - {log}\n')

    if action == "display":
        with open("logbook.txt", "r") as file:
            for line in file:
                print(line.strip())

# LogBook()







