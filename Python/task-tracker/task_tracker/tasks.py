from task_tracker import storage as db
from task_tracker import models as obj
from datetime import datetime
from rich.console import Console
from rich.table import Table
from rich import box
import time

console = Console()

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
    console.print(f"[bold green]Task --'{new_task.id}'-- added successfully![/]")

def reindex_tasks():
    tasks = db.load_tasks()
    tasks.sort(key=lambda task: task["id"])

    for index, task in enumerate(tasks, start=1):
        task["id"] = index

    db.save_tasks(tasks)

def delete_task(arguments):
    tasks = db.load_tasks()

    if not tasks:
        console.print("[bold red]No tasks to delete.[/]")
        return

    task_id = int(arguments[0])
    task_to_delete = next((task for task in tasks if task["id"] == task_id), None)

    if task_to_delete:
        tasks.remove(task_to_delete)
        db.save_tasks(tasks=tasks)
        console.print(f"[bold green]Task {task_id} deleted successfully![/]")
        console.print("[bold yellow]Reindexing tasks...[/]")
        reindex_tasks()
        time.sleep(2)
        console.print("[bold green]Reindexing done.[/]")
        time.sleep(0.6)
        console.print("[bold blue]Current tasks -->[/]")
        list_task()
    else:
        console.print(f"[bold red]Task {task_id} not found.[/]")

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
            console.print("[bold red]Invalid argument. Use 'in-progress', 'todo', or 'done'.[/]")
            return

    if not tasks:
        console.print("[bold red]No tasks available.[/]")
        return

    for task in tasks:
        created_time = datetime.fromisoformat(task["createdAt"])
        task["createdAtFormatted"] = created_time.strftime("%Y-%m-%d %H:%M")

    table = Table(show_header=True, header_style="bold magenta", box=box.ROUNDED)
    table.add_column("ID", justify="center")
    table.add_column("Description")
    table.add_column("Created At")
    table.add_column("Status", justify="center")

    for task in tasks:
        table.add_row(
            str(task["id"]),
            task["description"],
            task["createdAtFormatted"],
            task["status"].capitalize()
        )

    console.print(table)

def update_task(arguments):
    if len(arguments) < 2:
        console.print("[bold red]Error: Not enough arguments. You must provide the task ID and description.[/]")
        return

    try:
        id = int(arguments[0])
    except ValueError:
        console.print("[bold red]Error: Invalid task ID. ID must be an integer.[/]")
        return

    desc = arguments[1]
    tasks = db.load_tasks()

    task_found = False

    for task in tasks:
        if task["id"] == id:
            task["description"] = desc
            task["updatedAt"] = datetime.now().isoformat()
            db.save_tasks(tasks=tasks)
            console.print(f"[bold green]Task {id} description updated successfully![/]")
            task_found = True
            break

    if not task_found:
        console.print(f"[bold red]Task {id} not found.[/]")

def mark_todo_task(arguments):
    return update_status(arguments, "todo")

def mark_in_progress_task(arguments):
    return update_status(arguments, "in-progress")

def mark_done_task(arguments):
    return update_status(arguments, "done")

def update_status(arguments, new_status):
    if len(arguments) < 1:
        console.print("[bold red]Error: Task ID is required.[/]")
        return

    try:
        id = int(arguments[0])
    except ValueError:
        console.print("[bold red]Error: Invalid task ID. ID must be an integer.[/]")
        return

    tasks = db.load_tasks()
    task_found = False

    for task in tasks:
        if task["id"] == id:
            task["status"] = new_status
            task["updatedAt"] = datetime.now().isoformat()
            db.save_tasks(tasks=tasks)
            console.print(f"[bold green]Task {id} marked as {new_status}![/]")
            list_task()
            task_found = True
            break

    if not task_found:
        console.print(f"[bold red]Task {id} not found.[/]")
