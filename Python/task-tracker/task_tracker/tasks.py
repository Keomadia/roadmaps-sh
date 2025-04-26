from task_tracker import storage as db
from task_tracker import models as obj
from datetime import datetime
import time


def add_task(arguments):
    tasks = db.load_tasks()
    
    if tasks:
        max_id = max(task["id"] for task in tasks)
        new_id = max_id + 1
    else:
        new_id = 1

    new_task = obj.Task(
        id=new_id,
        description=arguments[0],
        status='todo',
    )
    
    tasks.append(new_task.to_dict()) 
    db.save_tasks(tasks=tasks)
    print(f"Task ID '{new_task.id}' added successfully!")


def reindex_tasks():
    tasks = db.load_tasks()
    tasks.sort(key=lambda task: task["id"])

    for index, task in enumerate(tasks, start=1):
        task["id"] = index   

    db.save_tasks(tasks)
    
    
def delete_task(arguments):
    tasks = db.load_tasks()
    
    if not tasks:
        print("No tasks to delete.")
        return
    
    task_id = int(arguments[0])
    task_to_delete = next((task for task in tasks if task["id"] == task_id), None)
    
    if task_to_delete:
        tasks.remove(task_to_delete)
        db.save_tasks(tasks=tasks)
        print(f"Task {task_id} deleted successfully!")
        print("Reindexing tasks...")
        reindex_tasks()
        time.sleep(2)
        print("Reindexing done.")
        time.sleep(0.6)
        print("Current tasks -->")
        list_task()
    else:
        print(f"Task {task_id} not found.")

def list_task(arguments=None):
    tasks = db.load_tasks()

    if arguments:
        if arguments[0] == "in-progress":
            tasks = [task for task in tasks if task["status"] == "in-progress"]
        elif arguments[0] == "todo":
            tasks = [task for task in tasks if task["status"] == "todo"]
        elif arguments[0] == "done":
            tasks = [task for task in tasks if task["status"] == "done"]
        else:
            print("❌ Invalid argument. Use 'in-progress', 'todo', or 'done'.")
            return

    if not tasks:
        print("🚫 No tasks available.")
        return

    for task in tasks:
        created_time = datetime.fromisoformat(task["createdAt"])
        task["createdAtFormatted"] = created_time.strftime("%Y-%m-%d %H:%M")

    id_width = max(len("ID"), max(len(str(task["id"])) for task in tasks))
    desc_width = max(len("Description"), max(len(task["description"]) for task in tasks)) + 10
    status_width = max(len("Status"), max(len(task["status"]) for task in tasks)) + 5
    created_width = max(len("Created At"), max(len(task["createdAtFormatted"]) for task in tasks)) + 3

    print(f"{'ID'.ljust(id_width)} | {'Description'.ljust(desc_width)} | {'Created At'.ljust(created_width)} | {'Status'.ljust(status_width)} ")
    print("-" * (id_width + desc_width + status_width + created_width + 9))


    for task in tasks:
        print(
            f"{str(task['id']).ljust(id_width)} | "
            f"{task['description'].ljust(desc_width)} | "
            f"{task['createdAtFormatted'].ljust(created_width)} | "
            f"{task['status'].capitalize().ljust(status_width)} "
        )

def update_task(arguments):
    if len(arguments) < 2:
        print("❌ Error: Not enough arguments. You must provide the task ID and description.")
        return

    try:
        id = int(arguments[0]) 
    except ValueError:
        print("❌ Error: Invalid task ID. ID must be an integer.")
        return

    desc = arguments[1]
    tasks = db.load_tasks()

    task_found = False

    for task in tasks:
        if task["id"] == id:
            task["description"] = desc 
            task["updatedAt"] = datetime.now().isoformat()
            db.save_tasks(tasks=tasks)
            print(f"✅ Task {id} description updated successfully!")
            task_found = True
            break

    if not task_found:
        print(f"❌ Task {id} not found.")

def mark_todo_task(arguments):
    return update_status(arguments, "todo")

def mark_in_progress_task(arguments):
    return update_status(arguments, "in-progress")

def mark_done_task(arguments):
    return update_status(arguments, "done")

def update_status(arguments, new_status):
    if len(arguments) < 1:
        print("❌ Error: Task ID is required.")
        return

    try:
        id = int(arguments[0])  
    except ValueError:
        print("❌ Error: Invalid task ID. ID must be an integer.")
        return

    tasks = db.load_tasks()
    task_found = False

    for task in tasks:
        if task["id"] == id:
            task["status"] = new_status
            task["updatedAt"] = datetime.now().isoformat()
            db.save_tasks(tasks=tasks)
            print(f"✅ Task {id} marked as {new_status}!")
            list_task()
            task_found = True
            break

    if not task_found:
        print(f"❌ Task {id} not found.")
