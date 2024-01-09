import datetime
import os
import requests

def palindromeCheker():
    string = input("Enter a string : ")
    clean_text = ''
    for char in string:
        if char.isalnum():
            clean_text += char.lower()

    return clean_text == clean_text[::-1]

# print(palindromeCheker())

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

# print(primeNumberFinder())

def logBook():
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


def toDoListApp():
    tasks = []
    action = input("Choose action ? (add/mark_done/list) ")

    if action == "add":
        toDo = input("Add a todo item : ")
        tasks.append({'task': toDo, 'done': False})
        with open('ToDoList.txt', 'a') as file:
            file.write(f'{tasks[0]["task"]} - {tasks[0]["done"]}')

    if action == "mark_done":
        task_num = int(input('Enter task number : '))
        tasks[task_num]['done'] = True
        with open('ToDoList.txt', 'a') as file:
            file.write(f'{tasks[task_num]["task"]}')

    if action == "list":
        with open('ToDoList.txt', 'r') as file:
            for task in file:
                print(task.strip())

# toDoListApp()

def textAnalyzer(path):
    with open(path, "r") as file:
        text = file.read()
        words_count = len(text.split())
        sentence_count = text.count('.')
        words = text.split()
        word_length = [len(word) for word in words]
        average_word_length = sum(word_length)/len(word_length)

        print(f' Word_count: {words_count}\n '
              f'sentence_count: {sentence_count}\n'
              f' average_word_length: {average_word_length}')

# file_path = 'sample_text'
# textAnalyzer(file_path)

def weatherCheker(city):
    api_key = os.getenv('API_KEY')
    base_url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'
    response = requests.get(base_url)
    data = response.json()
    if response.status_code == 200:
        print(f'Weather in {city} : {data["weather"][0]["description"]} (temp is {data["main"]["temp"]})')
    else:
        print(f'Failed to fetch weather inforamtion. {response}')

city = 'Warsaw'
weatherCheker(city)
