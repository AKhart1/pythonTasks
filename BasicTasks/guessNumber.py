import random
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

print(guessNumber(random.randint(1, 100)))