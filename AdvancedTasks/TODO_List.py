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

toDoListApp()