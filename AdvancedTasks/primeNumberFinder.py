def isPrime(num):
    if num < 1:
        return False
    for i in range(2, int(num ** 1/2) + 1):
        if num % i == 0:
            return False
    return True

def primeNumberFinder():
    numbers = int(input("Enter the number of prime numbers : "))
    primes = [num for num in range(2, numbers+1) if isPrime(num)]
    return primes

print(primeNumberFinder())