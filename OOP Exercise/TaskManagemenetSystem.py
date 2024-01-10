from datetime import datetime
class Task:
    def __init__(self, title, description, status='Incomplete', priority="Low", due_date=None):
        self.title = title
        self.description = description
        self.status = status
        self.priority = priority
        self.due_date = due_date

    def __str__(self):
        return f'{self.title} - {self.description} - {self.status}\n{self.priority} - {self.due_date}\n'

    def markCompleted(self):
        self.status = "Completed"

    def markInProgress(self):
        self.status = "In Progress"

class TaskList:
    def __init__(self):
        self.tasks = []

    def addTask(self, task):
        self.tasks.append(task)

    def deleteTask(self, task):
        if task in self.tasks:
            self.tasks.remove(task)
        else:
            print("Task not found")

    def displayTasks(self):
        if len(self.tasks) == 0:
            print("No tasks found")

        for task in self.tasks:
            print(task)

    def sortByPriority(self, priority):
        filtered_tasks = [task for task in self.tasks if task.priority.lower() == priority.lower()]
        if not filtered_tasks:
            print("No tasks found")
        else:
            for task in filtered_tasks:
                print(task)

    def sortByDueDate(self):
        sortedTasks = sorted(self.tasks, key=lambda n: n.due_date if n.due_date else datetime.datetime.now())
        if not sortedTasks:
            print("No tasks found")
        else:
            for task in sortedTasks:
                print(task)

if __name__ == "__main__":
    task1 = Task("Project", "Finish the project tasks", priority="High", due_date=datetime(2024, 5, 15))
    task2 = Task("Exams", "Prepare for upcoming exams", priority="Medium", due_date=datetime(2024, 4, 30))
    task3 = Task("Gym", "Go for to the gym", due_date=datetime(2024, 4, 20))
    task4 = Task("Health&Care", "Visit heal center for health check up ", priority="High", due_date=datetime(2024, 1, 16))

    task_list = TaskList()
    task_list.addTask(task1)
    task_list.addTask(task2)
    task_list.addTask(task3)
    task_list.addTask(task4)

    print('Displaying all tasks:')
    task_list.displayTasks()

    print("\nFiltering tasks by priority (Medium):")
    task_list.sortByPriority("Medium")

    print("\nSorting tasks by due date:")
    task_list.sortByDueDate()

    print("\nMarking a task as complete:")
    task1.markCompleted()
    task_list.displayTasks()

    print("\nDeleting a task:")
    task_list.deleteTask(task3)
    task_list.displayTasks()











