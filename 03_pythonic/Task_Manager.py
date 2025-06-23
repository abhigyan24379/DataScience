import os 
#file to store a task
FileName = "task.txt"

#load tasks from file

def load_task():
    tasks = {}
    if os.path.exists(FileName):
        with open(FileName, "r") as file:
            for line in file:
                task_id , title, status = line.strip().split(" | ")
                tasks[int(task_id)] = {"title":title, "status": status }
    return tasks

#save task to file

def save_tasks(tasks):
    with open(FileName, "w") as file :
        for task_id , task in tasks.items():
            file.write(f"{task_id} | {task['title']} | {task['status']} \n")

# add a new task 

def add_task(tasks):
    title = input("enter the task title")
    task_id = max(tasks.keys(), default =0) + 1
    tasks[task_id] = {"title": title , "status":"incomplete"}
    print (f"Tasks `{title}` added.")
    
    
#view all tasks 

def view_task(tasks):
    if not tasks :
        print ("no tasks available")
    else:
        for task_id , task in tasks.items():
            print (f"[{task_id}] {task['title']} - {task['status']}")
            
            
#mark task as complete 

def mark_task_complete(tasks):
    task_id = int (input("enteer the task id to mark as complete"))
    if task_id in tasks:
        tasks[task_id]["status"] = "complete"
        print (f"task `{tasks[task_id]['title']}` marked as complete ")
    else:
        print ("task is is not found ")
        
#delete a task 

def delete_task(tasks):
    task_id = int (input("enteer the task id to delete :"))
    if task_id in tasks:
        delete_task = tasks.pop(task_id)
        print (f"task `{delete_task["title"]}`  deleted ")
    else:
        print ("task is is not found ")
        
# main menu 

def main ():
    task = load_task()
    while True:
        print ("\n Task  Manager ")
        print ("1. Add Task")
        print ("2. view Task  ")
        print ("3. Mark Task as complete")
        print ("4. delete task ")
        print ("5. exit")
        
        choice = input ("Enter your choice ") 
        
        if choice == "1":
            add_task(task)
        elif choice == "2":
            view_task(task)    
        elif choice =="3":
            mark_task_complete(task)
        elif choice =="4":
            delete_task(task)
        elif choice =="5":
            save_tasks(task)
            print("goodbye ")
        else:
            print ("invalide choice, please try again ")
            
if __name__ == "__main__":
    main()