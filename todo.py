import json
import os
from datetime import datetime

TODO_FILE = 'todos.json'

class TodoApp:
    def __init__(self):
        self.todos = self.load_todos()
    
    def load_todos(self):
        """Load todos from JSON file."""
        if os.path.exists(TODO_FILE):
            with open(TODO_FILE, 'r') as f:
                return json.load(f)
        return []
    
    def save_todos(self):
        """Save todos to JSON file."""
        with open(TODO_FILE, 'w') as f:
            json.dump(self.todos, f, indent=2)
    
    def add_todo(self, title, description=''):
        """Add a new todo item."""
        todo = {
            'id': len(self.todos) + 1,
            'title': title,
            'description': description,
            'completed': False,
            'created_at': datetime.now().isoformat()
        }
        self.todos.append(todo)
        self.save_todos()
        print(f"✓ Added: {title}")
    
    def list_todos(self, show_completed=False):
        """Display all todos."""
        if not self.todos:
            print("No todos yet!")
            return
        
        print("\n" + "="*50)
        print("TODO LIST")
        print("="*50)
        
        for todo in self.todos:
            if not show_completed and todo['completed']:
                continue
            
            status = "✓" if todo['completed'] else "○"
            print(f"\n[{todo['id']}] {status} {todo['title']}")
            if todo['description']:
                print(f"    {todo['description']}")
            print(f"    Created: {todo['created_at']}")
        
        print("\n" + "="*50 + "\n")
    
    def complete_todo(self, todo_id):
        """Mark a todo as completed."""
        for todo in self.todos:
            if todo['id'] == todo_id:
                todo['completed'] = True
                self.save_todos()
                print(f"✓ Completed: {todo['title']}")
                return
        print(f"Todo with id {todo_id} not found.")
    
    def delete_todo(self, todo_id):
        """Delete a todo."""
        for i, todo in enumerate(self.todos):
            if todo['id'] == todo_id:
                title = todo['title']
                self.todos.pop(i)
                self.save_todos()
                print(f"✓ Deleted: {title}")
                return
        print(f"Todo with id {todo_id} not found.")
    
    def run(self):
        """Run the interactive CLI."""
        print("\nWelcome to Todo List App!")
        print("Commands: add, list, complete, delete, quit\n")
        
        while True:
            command = input("Enter command: ").strip().lower()
            
            if command == 'quit':
                print("Goodbye!")
                break
            elif command == 'add':
                title = input("Todo title: ").strip()
                description = input("Description (optional): ").strip()
                self.add_todo(title, description)
            elif command == 'list':
                self.list_todos()
            elif command == 'complete':
                try:
                    todo_id = int(input("Enter todo id: "))
                    self.complete_todo(todo_id)
                except ValueError:
                    print("Invalid id.")
            elif command == 'delete':
                try:
                    todo_id = int(input("Enter todo id: "))
                    self.delete_todo(todo_id)
                except ValueError:
                    print("Invalid id.")
            else:
                print("Unknown command. Try: add, list, complete, delete, quit")

if __name__ == '__main__':
    app = TodoApp()
    app.run()
