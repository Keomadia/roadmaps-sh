[github-user-activity](https://roadmap.sh/projects/github-user-activity)

---

# GitHub Activity CLI

Sample solution for the [github-user-activity](https://roadmap.sh/projects/github-user-activity) challenge from [Roadmap.sh User Activity](https://roadmap.sh)

A simple **Command-Line Interface (CLI)** application to fetch and display the **recent activity** of a GitHub user.

With this tool, you can:
- Provide a GitHub username.
- Fetch the user's recent public activity (pushes, stars, issues, forks, etc.).
- Display the activity cleanly in the terminal.
- View the first few activities immediately, and press Enter to reveal more.

---

## Features

- **Fetch Recent GitHub Events**: Retrieve a user's public activities (push events, issues, stars, forks, etc.).
- **CLI Argument**: Pass the GitHub username as a command-line argument.
- **Pagination**: Display the first 3 events, then show "..." and wait for the user to press Enter to continue.
- **Clean Output**: Nicely formatted activities for easy reading.
- **Pure Python**: No external libraries needed (uses built-in `urllib` and `json`).

---

## Usage

1. **Run the CLI**:

```bash
python cli.py <github-username>
```

Example:

```bash
python cli.py kamranahmedse
```

2. **Output Example**:

```
Output:
- Pushed 3 commit(s) to kamranahmedse/developer-roadmap
- Opened a new issue in kamranahmedse/developer-roadmap
- Starred kamranahmedse/roadmap.sh
...
Press Enter to see more...
- Forked kamranahmedse/free-for-dev
- Closed an issue in kamranahmedse/another-project
- WatchEvent on kamranahmedse/roadmap.sh
...
```

---

## Getting Started

1. **Clone the Repository**:

```bash
git clone <repository-url>
cd github-activity-cli
```

2. **Run the CLI**:

```bash
python cli.py <github-username>
```

Example:

```bash
python cli.py torvalds
```

---

## Project Structure

```plaintext
github-activity-cli/
├── main.py                
└── github_activity/
    └── cli.py      
    └── activity.py      
```

---

## Requirements

- Python 3.x
- Internet connection
- No external libraries needed (uses `urllib` and `json`)

---

## Contributing

Feel free to fork this repository and submit pull requests.  
Issues, suggestions, and improvements are welcome!

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

# 🚀
