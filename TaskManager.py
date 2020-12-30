
# Methods
def Post ( filename , Object ):
	f =  open( "..\\TaskManager\\" + filename, 'a' )
	f.write ( Object )
	f.write ( '\n' )
	f.close()

def ReadFile ( filename ):
	f =  open( "..\\TaskManager\\" + filename, 'r' )
	content = f.readlines()
	print( content )

def DisplayToUser ( message ):
	print ( '\n' + message )








# Main function of the application
menu = "  \n MENU \n \n 1 = Register a new user \n 2 = Create a new task \n 3 = View all Tasks \n 4 = View all Users \n 5 = Exit "
DisplayToUser( menu )
	
def RunFunctionsBasedOnMenuSelection ():
	userSelection = input ( "\n\n Make a selection from the menu. \n"  )
	if "1" in userSelection:
		CreateUserAccount ()
	elif "2" in userSelection:
		CreateNewTask()
	elif "3" in userSelection:
		ViewAllTasks()
	elif "4" in userSelection:
		ViewAllUsers()
	elif "5" in userSelection:
		exit()
	else:
		DisplayToUser ( ' You may have made an error. Please try again' )
		RunFunctionsBasedOnMenuSelection ()


def CreateUserAccount ():
	username = input( '\n\n' +  " Enter a User Name: ")
	password = input( " Enter a Password: ")
	confirmPassword = input ( " Confirm Password: ")
	userObject = 'Name: ' + username + " , " + 'Password: ' +  str ( password ) + '; '

	if confirmPassword != password:
		DisplayToUser ( ' Password confirmation is incorrect. Re-enter your details.' )
		CreateUserAccount ()
	else:
		Post( 'users.txt' , userObject )
		DisplayToUser ( ' Your account has been created succesfully.' )
		RunFunctionsBasedOnMenuSelection ()


def CreateNewTask ():
	owner = input( '\n\n' +  " Owner: ")
	title = input( " Title: ")
	description = input( " Description: ")
	created_date = input( " Created on: ")
	deadline = input( " Deadline date: ")
	status = input( " Has the task been completed. (Yes/No): " )
	Task = 'Owner: ' + owner + " , " + 'Title: ' + title + " , " +  'Created: ' + created_date + " , " +  'Deadline: ' + deadline + " , " +  'Status: ' + status +  " , " +  'Description: ' + description

	Post ( 'tasks.txt' , Task )
	DisplayToUser ( ' Your task has been entered succesfully.' )
	RunFunctionsBasedOnMenuSelection ()


def ViewAllTasks ():
	ReadFile ( 'tasks.txt' )
	RunFunctionsBasedOnMenuSelection ()

def ViewAllUsers ():
	ReadFile ( 'users.txt' )
	RunFunctionsBasedOnMenuSelection ()


# Call Functions
RunFunctionsBasedOnMenuSelection ()