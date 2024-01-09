def simpleCalculator():
    numbers = input("Enter the numbers separated by space: ")
    action = input("Enter the action to perform (add,sub,mul,div): ")

    numbers = numbers.split(' ')
    x = float(numbers[0])
    y = float(numbers[1])

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

print(simpleCalculator())

def simpleCalculator2(expression):
    print(eval(expression))

print(simpleCalculator2('1+2+(5*6)'))