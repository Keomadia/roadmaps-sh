import sys
from github_activity import activity

def handle_command():
    args = sys.argv[1:]

    if not args:
        print("No Username provided.")
        return
    arguments = args[0:]
    
    activity.get_user_events(username=arguments[0])