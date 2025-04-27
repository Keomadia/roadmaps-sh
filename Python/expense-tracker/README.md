
---


# Expense Tracker CLI

Sample solution for the [Expense Tracker](https://roadmap.sh/projects/expense-tracker) challenge from [Roadmap.sh](https://roadmap.sh).
A simple and lightweight **Command-Line Interface (CLI)** application to manage your personal expenses easily.

Built with **Python**, using **argparse** and **Rich** for beautiful output formatting.

---

## 📦 Features

- Add new expenses
- List all recorded expenses
- Delete an expense by ID
- View monthly expense summaries
- Export expenses to a CSV file

---

## 🛠 Requirements

- Python 3.8 or higher
- Packages:
  - `rich`
  - `argparse`

You can install the required package using:

```bash
pip install rich
```
```bash
pip install argparse
```

---

## 🚀 How to Use

First, navigate into the project folder.

Then run the following commands:

| Action | Command |
|:---|:---|
| Add a new expense | `python Main.py add --amount 45.50 --description "Lunch at café"` |
| List all expenses | `python Main.py list` |
| Delete an expense | `python Main.py delete --id 3` |
| View monthly summary | `python Main.py summary --month 4` |
| Export all expenses to CSV | `python Main.py export` |

---

## 📂 Project Structure

```
expense-tracker-cli/
├── Main.py
├── expense_tracker/
│   ├── cli.py
│   ├── tracker.py
│   ├── models.py
│   └── storage.py
└── data/
    └── expenses.json
```

- `Main.py`: Entry point
- `cli.py`: Handles command-line parsing
- `tracker.py`: Handles all tracking logic
- `models.py`: Defines data structures
- `storage.py`: Manages data saving and loading
- `data/expenses.json`: Stores your expenses

---

## 📤 Export

Exports your expenses to a CSV file inside the `data/` folder when you run:

```bash
python Main.py export
```

---

## ✨ Preview 

Check Preview.gif to see a quick demo

---

## 👨‍💻 Author

Made with ❤️ by **Keomadia**

---

<!-- ## 📃 License

This project is licensed under the [MIT License](LICENSE).

--- -->

## 🔗 Challenge Source

This project was built for the [Expense Tracker](https://roadmap.sh/projects/expense-tracker) challenge by [Roadmap.sh](https://roadmap.sh).

---

 
