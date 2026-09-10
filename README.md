# Todo List App

A simple command-line todo list application built with Python.

## Features

- ✨ Add new todos with descriptions
- 📋 List all your todos
- ✓ Mark todos as completed
- 🗑️ Delete todos
- 💾 Persistent storage using JSON

## Installation

No external dependencies required! Just Python 3.6+

```bash
git clone https://github.com/kenji-ryozaki/todo-list-app.git
cd todo-list-app
```

## Usage

```bash
python todo.py
```

Then use these commands:

- **add** - Add a new todo
- **list** - Display all todos
- **complete** - Mark a todo as completed
- **delete** - Delete a todo
- **quit** - Exit the app

## Example

```
Welcome to Todo List App!
Commands: add, list, complete, delete, quit

Enter command: add
Todo title: Buy groceries
Description (optional): milk, eggs, bread
✓ Added: Buy groceries

Enter command: list

==================================================
TODO LIST
==================================================

[1] ○ Buy groceries
    milk, eggs, bread
    Created: 2026-09-10T10:30:45.123456

==================================================

Enter command: complete
Enter todo id: 1
✓ Completed: Buy groceries

Enter command: quit
Goodbye!
```

## License

MIT License - feel free to use this project for personal or commercial use.
