
---

## Task Tracker CLI

---

# Task Tracker CLI

Sample solution for the [task-tracker](https://roadmap.sh/projects/task-tracker) challenge from [Roadmap.sh](https://roadmap.sh).

A simple and effective **Command-Line Interface (CLI)** application to manage, update, and track your daily tasks.

Built with **Python** for flexible and easy task tracking directly from your terminal.

---

## 📦 Features

- Add, update, and delete tasks
- Mark tasks as **todo**, **in-progress**, or **done**
- List all tasks or filter by status
- View detailed information about each task

---

## 🛠 Requirements

- Python 3.x
- Rich

---

## 🚀 How to Use

First, clone the repository and navigate into the project folder:

```bash
git clone <repository-url>
cd task-tracker-cli
```

Run the CLI commands:

```bash
python cli.py <command> <arguments>
```

Example:

```bash
python cli.py add "Buy groceries"
```

You can install the required package using:

```bash
pip install rich
```

---

## 📂 Project Structure

```
task-tracker-cli/
├── main.py
├── tasks.json
└── task_tracker/
    ├── cli.py
    └── models.py
    └── storage.py
    └── tasks.py
```

---

## 📖 Commands

| Action | Command |
|:---|:---|
| Add a new task | `python main.py add "Task description"` |
| Update a task | `python main.py update <task-id> "New description"` |
| Mark a task as "todo" | `python main.py mark-todo <task-id>` |
| Mark a task as "in-progress" | `python main.py mark-in-progress <task-id>` |
| Mark a task as "done" | `python main.py mark-done <task-id>` |
| List all tasks | `python main.py list` |
| List tasks by status | `python main.py list <status>` |
| Delete a task | `python main.py delete <task-id>` |

---

## 📋 Task Properties

Each task contains:

- **id**: Unique identifier
- **description**: Task description
- **status**: Task status (`todo`, `in-progress`, `done`)
- **createdAt**: Date/time created
- **updatedAt**: Date/time last updated

---

## ✨ Output Example

```
ID   | Description          | Status       | Created At
---------------------------------------------------------------
1    | Buy groceries         | todo         | 2025-04-23T15:30:00
2    | Complete the report   | in-progress  | 2025-04-23T16:00:00
3    | Submit homework       | done         | 2025-04-23T17:00:00
```

---

## 👨‍💻 Contributing

You are welcome to **fork** this repository and submit **pull requests**.  
Feedback, issues, and improvements are encouraged!

---

## ✨ Preview 

Check Preview.gif to see a quick demo

---

## 👨‍💻 Author

Made with ❤️ by **Keomadia**

---

## 📃 License

This project is licensed under the [MIT License](LICENSE).

---

## 🔗 Challenge Source

This project was built for the [Task Tracker](https://roadmap.sh/projects/task-tracker) challenge by [Roadmap.sh](https://roadmap.sh).

---

# 🚀

