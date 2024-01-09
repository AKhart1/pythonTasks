import datetime
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

logBook()