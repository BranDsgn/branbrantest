
Subscribe to Pro for 5x more usage with Claude 3.5 Sonnet.
import json
import os

TODO_FILE = "todos.json"

def load_todos():
    if os.path.exists(TODO_FILE):
        with open(TODO_FILE, "r") as f:
            return json.load(f)
    return []

def save_todos(todos):
    with open(TODO_FILE, "w") as f:
        json.dump(todos, f)

def add_todo(todos, task):
    todos.append({"task": task, "completed": False})
    save_todos(todos)
    print(f"Added task: {task}")

def list_todos(todos):
    if not todos:
        print("No tasks in the list.")
    else:
        for i, todo in enumerate(todos, 1):
            status = "✓" if todo["completed"] else " "
            print(f"{i}. [{status}] {todo['task']}")

def complete_todo(todos, index):
    if 1 <= index <= len(todos):
        todos[index - 1]["completed"] = True
        save_todos(todos)
        print(f"Marked task {index} as completed.")
    else:
        print("Invalid task number.")

def main():
    todos = load_todos()
    while True:
        print("\n--- Todo List ---")
        print("1. Add task")
        print("2. List tasks")
        print("3. Mark task as completed")
        print("4. Quit")
        
        choice = input("Enter your choice (1-4): ")
        
        if choice == "1":
            task = input("Enter the task: ")
            add_todo(todos, task)
        elif choice == "2":
            list_todos(todos)
        elif choice == "3":
            list_todos(todos)
            index = int(input("Enter the task number to mark as completed: "))
            complete_todo(todos, index)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
Subscribe to Pro


Simple Todo List Application
