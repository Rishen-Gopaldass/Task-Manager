# TITLE: Task Manager
# AIM: To create software for a company to manager their tasks.
# AUTHOR: Rishen Gopaldass

# START 
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------


# USER MENU:
# fuction defined
# user input requested. 
# prompt another function to run.

def menu():
    menuinput = input("\n Please enter a selection below: \n \n r = register user \n n = new task \n a = view all tasks \n m = view my tasks \n e = exit \n \n").lower()
    if "r" in menuinput:
        register()
    elif "n" in menuinput:
        new_task()
    elif "a" in menuinput:
        alltasks()
    elif "m" in menuinput:
        mytasks()
    elif "e" in menuinput:
        exit_programe()
    else:
        print("Please enter from the list: ")
        menu()




# REGISTRATION:
# fuction defined
#  open a text file
# user input requested. 
#  if statement compares conditions between passwords.
#  write to text file
# prompt another function to run.
# else statement controls user's errors.

def register():
    fuser =  open("C:\\Users\Rishen\\\Desktop\\Task Manager\\user.txt", "a")
    username = input("Enter a User Name: ")
    password = input("Enter a Password: ")
    password_confirm = input("Confirm Password: ")
    if password_confirm == password:
        fuser.write(username + ", " + str(password) + "\n")
        fuser.close()
        menu()
    else:
        print("Password does not match. Try again! ")
        register()




# NEW TASK INPUTS:
# fuction defined
# open text file.
# user input requested. 
#  write to text file
# prompt another function to run.

def new_task():
    ftask =  open("C:\\Users\\Rishen\\Desktop\\Task Manager\\task.txt", "a")
    task_holder = input("Enter the task owner: ")
    task_title = input("Enter the task title: ")
    task_description = input("Enter the task description: ")
    task_created_date = input("Enter the date the task is created on: ")
    task_deadline = input("Enter the deadline date: ")
    task_complete = input("Has the task been completed. (Yes/No): ")
    ftask.write("Task owner:               \t" + task_holder + "\n")
    ftask.write("Task Tile:                    \t" + task_title + "\n")
    ftask.write("Task Description:      \t" + task_description + "\n" )
    ftask.write("Task Created Date:   \t" + task_created_date + "\n" )
    ftask.write("Task Deadline:           \t" + task_deadline + "\n" )
    ftask.write("Task Completed:       \t" + task_complete + "\n" )
    ftask.write("\n")
    ftask.close()
    menu()



# VIEW ALL TASKS IN TEXT FILE:
# fuction defined
# open text file.
#  read file.
# prompt another function to run.

def alltasks():
    ftask = open("C:\\Users\\Rishen\\Desktop\\Task Manager\\task.txt","r")
    x = ftask.readlines()
    print(x)
    menu()



# VIEW EACH USER'S TASK ONLY:
# fuction defined
# open text file.
#  read file.
# prompt another function to run.

def mytasks():
    ftask = open("C:\\Users\\Rishen\\Desktop\\Task Manager\\user.txt", "r")
    x = ftask.readlines()
    print(x)
    menu()



# EXIT PROGRAM:
# fuction defined
# prompt another function to run.

def exit_programe():
    exit()




# RUNNING OF PROGRAMS ABOVE:
menu()



# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#  END
