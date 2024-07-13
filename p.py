tasks = []

def display_menu():

    print("\nWelcome to the To-Do List App!\n")
    print("Menu:")
    print("1. Add a task")
    print("2. View tasks")
    print("3. Mark a task as complete")
    print("4. Delete a task")
    print("5. Quit")

def add_title():
    task_title = input ("enter the task title : ")
    tasks.append({"title":task_title, "status": "Incomplete"})
    print("Task add successflly.")

def view_tasks():
    if not tasks:
        print("No tasks found.")
    else:
        print(tasks)

def mark_comomplet():
    view_tasks
    try:
        task_num = int(input("enter a task number to mark as comlete: "))
        if task_num < 1 or task_num > len(tasks):
            print ("invalid task number")
        else:
            tasks[task_num - 1]["status"]= "complete"
            print("task marked as complete")
    except ValueError :
        print("invalid number . please enter a number ")

def delete_task():
    view_tasks()
    try:
        task_num = int(input("enter a task number to delete: "))
        if task_num < 1 or task_num > len(tasks):
            print ("invalid task number")
        else:
            tasks.remove([task_num - 1])["status"]= "delete"
            print("task deleted successflly")
    except ValueError :
        print("invalid number . please enter a number ")

while True:
    display_menu()
    try:
        choice= int(input("enter the number : (1-5)"))

        if choice==1:
           add_title()
        elif choice==2:
           view_tasks()
        elif choice==3:
           mark_comomplet()
        elif choice==4:
           delete_task()
        elif choice==5:
            break
        else:
            print("invalid choice. please try agine")
    except ValueError:
        print("invalid input. please enter a number")






