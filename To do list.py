TASK_FILE ="tasks.text" 

#Function to load tasks from file
def load_tasks():
    try:
        with open(TASK_FILE, "r") as file:
            tasks =[line.strip() for line in file.readlines()]
    except FileNotFoundError:
        tasks =[]
        return tasks
    
    #Functions to save tasks to file
    def save_tasks(tasks):
        with open(TASK_FILE,"W") as file:
            for task in task:
                file.write(task+ "\n")
    
    #Function to show all tasks
    def show_tasks(tasks):
        print("\nYour task:")
        if not tasks:
            print("No tasks available.")
        else:
         for i,tasks in enumerate(tasks, 1):
                print(f"{i}.{tasks}")
        print()
    
    #Functions to add  new task
    def add_task(tasks):
        task = input("Enter a new task:").strip()
        if task:
            tasks.append(task)
            save_tasks(tasks)
            print("Task added!\n")
        else:
            print("as 1, Task cannot be empty !\n")
    
    #Functions to mark a task as done
    def mark_done(tasks):
        show_tasks(tasks)
        try:
            num = int(input("Enter task number to mark done:"))
            if 1 <= num <=len(tasks):
               done_task = tasks.pop (num - 1)
               save_tasks(tasks) 
               print(f"as 1, Task '{done_task}' marked as done!\n")
            else:  
                print("Invalid task number!\n")
        except ValueError:
            print("Please enter a valid number!\n")  
    
    #Functions to delete a task
    def   delete_task(tasks):
        show_tasks(tasks)
        try:
            num = int(input("Enter task number to delete :"))
            if 1 <= num <=len(tasks):
                removed = tasks.pop(num - 1)
                save_tasks(tasks)
                print(f"Task '{removed}' deleted!\n")
            else:
                print("Invalid task number!\n")   
        except ValueError:
            print ("please eneter a valid number!\n")  
    #Main program loop
    def main(): 
     tasks = load_tasks()

    while True:
        print("========TO-DO LIST MENU ========")
        print("1. Show tasks")
        print("2. Add Task")
        print("3. Mark Task as Done")
        print("4. Delete Task")
        print("4. Delete Task")
        print("5. Exit\n")
        print("================================")
        
        choice = input("Enter choice :")

        if choice == "1":
            show_tasks(tasks)
        
        elif choice == "2":
             add_task(tasks)
        
        elif choice == "3":
             mark_done(tasks) 
        
        elif choice == "4":
            delete_task(tasks)
        
        elif choice == "5":
             print("Exiting....Have a productive day!")
        break
    
           
                                                            

                          


        
