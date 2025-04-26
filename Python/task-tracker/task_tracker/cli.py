# cli.py
import sys
from task_tracker import tasks

def handle_command():
    args = sys.argv[1:]
    
    possible_commands = {
        "add", "list", "update", "delete","mark_todo", "mark_in_progress", "mark_done",
    }
    
    if not args:
        print("No command provided.")
        return
    
    command = args[0]
    arguments = args[1:]

    if command in possible_commands:

        function_name = f"{command}_task"
 
        if hasattr(tasks, function_name):
            func = getattr(tasks, function_name)
            func(arguments)
        else:
            print(f"The function {function_name} is not implemented yet.")
    else:
        print(f"Unknown command: {command}")
