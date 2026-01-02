# Display All Function

def showMenu():
    print("--- Welcome To Task Management System ---")
    print("1) Add Task")
    print("2) Remove Task")
    print("3) Update Task")
    print("4) Show Task")
    print("5) Show all Tasks")
    print("6) Exit")

# Take input

def getChoice():
    showMenu()
    try:
        choice = int(input("Enter your Choice: "))
        return choice
    except ValueError:
        print("Invalid Choice Try Again")

# Make Empty list

tasks = []

# Add task
def addTask():
    task = input("Enter your Task: ")
    tasks.append(task)
    print("Task Added")

# Remove Task

def removeTask():
    index = int(input("Enter id of Task to remove: "))
    try:
        if index <= len(tasks):
            tasks.pop(index - 1)
            print("Task Removed")
    except IndexError:
        print("Index out of Range")

# Show specific task

def showTask():
    index = int(input("Enter id of Task to show: "))
    try:
        if index <= len(tasks):
            print(tasks[index-1])
    except IndexError:
        print("Index out of Range")

# Update task

def updateTask():
    index = int(input("Enter id of Task to update: "))
    try:
        if(index <= len(tasks)):
            task = input("Enter new Task: ")
            tasks[index-1] = task
            print("Task Updated")
    except IndexError:
        print("Index out of Range")

# Show all tasks

def showAllTasks():
    if len(tasks) == 0:
        print("No Tasks Added")
    else:
        print("--- All Tasks ---")
        i = 1
        for task in tasks:
            print(i, ") " ,task)
            i+=1

# Main funciton

def main():
    while True:
        choice = getChoice()
        if choice == 1:
            addTask()
        elif choice == 2:
            removeTask()
        elif choice == 3:
            updateTask()
        elif choice == 4:
            showTask()
        elif choice == 5:
            showAllTasks()
        elif choice == 6:
            exit()

main()