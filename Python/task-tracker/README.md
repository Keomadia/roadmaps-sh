Link to the Project from roadmap.sh [Project url ](https://roadmap.sh/projects/task-tracker)

---

# Task Tracker CLI

A simple Command-Line Interface (CLI) application to manage and track your tasks.

With this tool, you can:
- Add, update, and delete tasks.
- Mark tasks as "in-progress" or "done".
- List tasks by their current status (todo, in-progress, completed).
- View detailed task information.

---

## Features

- **Add Task**: Create a new task with a description.
- **Update Task**: Modify the task description.
- **Mark Task Status**: Set the task to "todo", "in-progress", or "done".
- **List Tasks**: View tasks filtered by their current status.
- **Delete Task**: Remove a task from the list.

---

## Commands

### 1. **Add a Task**

Add a new task to the tracker.

```bash
$ task-cli add "Buy groceries"
```

**Output**:  
`Task 1 added successfully!`

---

### 2. **Update a Task**

Update the description of an existing task.

```bash
$ task-cli update <task-id> "<new-description>"
```

- Example: To update task 2's description to "Complete the report":

```bash
$ task-cli update 2 "Complete the report"
```

**Output**:  
`Task 2 description updated successfully!`

---

### 3. **Mark a Task as 'Todo'**

Mark a task as "todo" (pending).

```bash
$ task-cli mark-todo <task-id>
```

- Example: To mark task 5 as "todo":

```bash
$ task-cli mark-todo 5
```

**Output**:  
`Task 5 marked as todo!`

---

### 4. **Mark a Task as 'In Progress'**

Mark a task as "in-progress".

```bash
$ task-cli mark-in-progress <task-id>
```

- Example: To mark task 3 as "in-progress":

```bash
$ task-cli mark-in-progress 3
```

**Output**:  
`Task 3 marked as in-progress!`

---

### 5. **Mark a Task as 'Done'**

Mark a task as "done".

```bash
$ task-cli mark-done <task-id>
```

- Example: To mark task 7 as "done":

```bash
$ task-cli mark-done 7
```

**Output**:  
`Task 7 marked as done!`

---

### 6. **List All Tasks**

List all tasks in the tracker.

```bash
$ task-cli list
```

**Output**:  
```
ID   | Description          | Status      | Created At          
--------------------------------------------------------------
1    | Buy groceries        | todo        | 2025-04-23T15:30:00  
2    | Complete the report  | in-progress | 2025-04-23T16:00:00  
3    | Submit homework      | done        | 2025-04-23T17:00:00 
```

---

### 7. **List Tasks by Status**

Filter tasks by their current status.

- To list all **todo** tasks:

```bash
$ task-cli list todo
```

- To list all **in-progress** tasks:

```bash
$ task-cli list in-progress
```

- To list all **completed** tasks:

```bash
$ task-cli list completed
```

**Output**:  
For **todo** tasks:

```
ID   | Description        | Status   | Created At          
-----------------------------------------------------------
1    | Buy groceries      | todo     | 2025-04-23T15:30:00 
```

---

### 8. **Delete a Task**

Delete a task from the tracker.

```bash
$ task-cli delete <task-id>
```

- Example: To delete task 3:

```bash
$ task-cli delete 3
```

**Output**:  
`Task 3 deleted successfully!`

---

## Task Properties

Each task consists of the following properties:

- **id**: A unique identifier for the task.
- **description**: A short description of the task.
- **status**: The current status of the task (`todo`, `in-progress`, or `done`).
- **createdAt**: The date and time when the task was created.
- **updatedAt**: The date and time when the task was last updated.

---

## Getting Started

1. **Clone the Repository**:

   ```bash
   git clone <repository-url>
   cd task-tracker-cli
   ```

2. **Install Dependencies**:

   Make sure to install Python 3 and any necessary dependencies.

3. **Run the CLI**:

   The CLI can be executed from the command line using:

   ```bash
   python cli.py <command> <arguments>
   ```

   Example:

   ```bash
   python cli.py add "Buy groceries"
   ```

---

## Contributing

Feel free to fork this repository and submit pull requests. Issues and feedback are welcome.

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---
