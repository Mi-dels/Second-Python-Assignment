# TO-DO-LIST ASSIGNMENT

Task = []

def addTask():
   try:
      task = input("Please enter a Task: \n")
      Task.append({"Task": task, "Status": "Pending "})
      print(f"Task '{task}' has been added to the list\n")
   except ValueError:
      print("Please Enter A Valid Task Number")

def listTasks():
   try:
      if not Task:
         print("There is no task currently.")
      elif len(Task) > 1:
         print("current tasks")
      for index, task in enumerate(Task, 1):
         print(f"{index}.{task["Task"]} - {task["Status"]}  \n")
         index += 1 
      else:
         print("current task")
      for index, task in enumerate(Task, 1):
         print(f"{index}.{task["Task"]} - {task["Status"]} \n")
   except ValueError:
      print("Please Enter A Valid Task Number")
     

def editTask():
   try:
      for index, task in enumerate(Task, 1):
         print(f"Task #{index}. {task}")
         index += 1
         edit = int(input("Enter the input to be edited:")) - 1
         Task[edit] = input("write the changes:")
      for index, task in enumerate(Task, 1):
         print(f"Task #{index}. {task["Task"]} - {task["Status"]}")
         index += 1
   except ValueError:
      print("Please Enter A Valid Task Number")


   
   

   


def markTask():
   for index, task in enumerate(Task, 1):
      print(f"Task #{index}. {task}")
      index += 1
   if len(Task) == 0:
      print("No Current Task \n")
   else:
      try:
         Mark = int(input("Enter the task number to be marked as complete:")) - 1
         if 0 <= Mark < len(Task):
            Task[Mark]["Status"] = "done"
            print(f"Task {Mark}{Task} has been done")
         else:
            print("Invalid Task Number")
      except ValueError:
         print("Please Enter A Valid Task Number")


def deleteTask():
   for index, task in enumerate(Task, 1):
      print(f"Task #{index}. {task}")
      index += 1
   if len(Task) == 0:
      print("No Current Task \n")
   else:
      try:
         remove = int(input("Enter the task number to be removed:")) - 1
         if 0 <= remove < len(Task):
            removedTasks = Task.pop(remove)
            print(f"Task removed: {removedTasks}")
         else:
            print("Invalid Task Number")
      except ValueError:
         print("Please Enter A Valid Task Number")
              


   
  
  
    
  


    


if __name__ == "__main__":
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
         addTask()
      elif(choice == "2"):
         listTasks()

      elif(choice == "3"):
         editTask()

      elif(choice == "4"):
         markTask()

      elif(choice == "5"):
         deleteTask()

      elif(choice == "6"):
         print("Existing The Application........")
         exit()
      else:
         print("invalid syntax, Please enter a valid input")
         
       
          
      
         
      
         
      

      
         
