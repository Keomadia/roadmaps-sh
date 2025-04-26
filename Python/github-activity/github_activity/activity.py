
import json
import urllib.request
import urllib.error

def get_user_events(username):
    url = f"https://api.github.com/users/{username}/events"

    try:
        with urllib.request.urlopen(url) as response:
            if response.status != 200:
                print(f"Error: Cannot fetch activity for user '{username}'. Status Code: {response.status}")
                return

            data = response.read()
            events = json.loads(data)

            if not events:
                print(f"No recent activity found for user '{username}'.")
                return

            print("\nOutput:")

            for idx, event in enumerate(events):
                if idx == 3:
                    print("...")
                    input("Press Enter to see more...")
                
                event_type = event.get('type')
                repo_name = event.get('repo', {}).get('name', 'Unknown Repo')

                if event_type == "PushEvent":
                    commits = event.get('payload', {}).get('commits', [])
                    message = f"- Pushed {len(commits)} commit(s) to {repo_name}"
                elif event_type == "IssuesEvent":
                    action = event.get('payload', {}).get('action', 'acted on')
                    message = f"- {action.capitalize()} a new issue in {repo_name}"
                elif event_type == "WatchEvent":
                    message = f"- Starred {repo_name}"
                elif event_type == "ForkEvent":
                    message = f"- Forked {repo_name}"
                else:
                    message = f"- {event_type} on {repo_name}"

                print(message)

    except urllib.error.HTTPError as e:
        print(f"HTTP Error: {e.code} - {e.reason}")
    except urllib.error.URLError as e:
        print(f"URL Error: {e.reason}")
    except Exception as e:
        print(f"Unexpected error: {e}")
