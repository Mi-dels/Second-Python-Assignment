class Task:
    def __init__(self,Tasks,Details,Status):
        self.Tasks = Tasks
        self.Details = Details
        self.Status = Status

    def __str__(self):
        return f"{self.Tasks} | {self.Details} | Status: {self.Status}"

       
class taskFunctions: 
    def __init__(self):
            self.task = []

    def addTask(self):
        Tasks = input("Create a task:")
        Details = input("Enter the description of the new task:")
        Status = input("Enter the status of the new task e.g initialized, pending, done:")
        newTask = Task(Tasks,Details,Status)
        self.task.append(newTask)
        print("Task has been created")

    def listTask(self):
        if not self.task:
            print("There is no task currently.")
        else:
            for index, task in enumerate(self.task, 1):
                print(f" {index} . {task}") 

    def editTask(self):
        self.listTask()
        if not self.task:
            return self.addTask()
        else:
                idx = int(input("Enter task number to update: "))
                task = self.task[idx]
                choice = input("Choice: ")
            
        if choice == '1': task.Tasks = input("New Task: ")
        elif choice == '2': task.Details = input("New Details: ")
        elif choice == '3': task.Status = input("New Status: ")
        print("Updated!")


    def markTask(self):


    



            
          


        
manager = taskFunctions()
while(True):
    print("*** Main Menu ***")
    print("Please select any of the following options:")
    print("--------------------------------------------------------")
    print("1. Add a new task")
    print("2. List tasks")
    print("3. Edit an existing task")
    print("4. Mark a completed task")
    print("5. Delete an existing task")
    print("6. Exit")

    choice = input("Enter your choice :")
    if(choice == "1"):
       manager.addTask()
    elif(choice == "2"):
        manager.listTask()

    elif(choice == "3"):
        manager.editTask()

    elif(choice == "4"):
        manager.markTask()

    elif(choice == "5"):
        manager.deleteTask()

    elif(choice == "6"):
        print("Existing The Application........")
        exit()
    else:
        print("invalid syntax, Please enter a valid input")       


    