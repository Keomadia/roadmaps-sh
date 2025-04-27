---

## GitHub Activity CLI

---

# GitHub Activity CLI

Sample solution for the [github-user-activity](https://roadmap.sh/projects/github-user-activity) challenge from [Roadmap.sh](https://roadmap.sh).

A simple and lightweight **Command-Line Interface (CLI)** application to fetch and display the **recent activity** of a GitHub user.

Built with **Python**, using only **standard libraries** (`urllib`, `json`) for smooth and clean terminal interaction.

---

## 📦 Features

- Fetch recent GitHub events (pushes, issues, stars, forks, etc.)
- Pass GitHub username via CLI arguments
- Display the first few events, then press **Enter** to view more (pagination)
- Nicely formatted clean output
- Pure Python — **no external libraries needed**

---

## 🛠 Requirements

- Python 3.x
- Internet connection
- No additional packages required

---

## 🚀 How to Use

First, clone the repository and navigate into the project folder:

```bash
git clone <repository-url>
cd github-activity-cli
```

Run the CLI with a GitHub username:

```bash
python cli.py <github-username>
```

Example:

```bash
python cli.py torvalds
```

---

## 📂 Project Structure

```
github-activity-cli/
├── main.py                
└── github_activity/
    ├── cli.py      
    └── activity.py      
```

---

## Output Example

```
- Pushed 3 commit(s) to torvalds/linux
- Starred torvalds/subsurface
- Opened a new issue in torvalds/tinycc
...
Press Enter to see more...
- Forked torvalds/qemu
- Closed an issue in torvalds/linux
...
```

---

## 👨‍💻 Contributing

Feel free to **fork** this repository and **submit pull requests**.  
Issues, feedback, and suggestions are highly welcome!

---



## ✨ Preview 

Check Preview.gif to see a quick demo

---

## 👨‍💻 Author

Made with ❤️ by **Keomadia**

<!-- ## 📃 License

This project is licensed under the [MIT License](LICENSE).

--- -->
---

## 🔗 Challenge Source

This project was built for the [GitHub User Activity](https://roadmap.sh/projects/github-user-activity) challenge by [Roadmap.sh](https://roadmap.sh).

---
