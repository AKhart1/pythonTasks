def listSorter():
    user_input = input("Enter the numbers separated by space: ")
    numbers = user_input.split(' ')
    numbers.sort()
    print('Sorted list: ', numbers )

listSorter()
