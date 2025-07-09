import tkinter as tk
from tkinter import messagebox

tasks = []

def load_tasks():
    """Load tasks from the tasks.txt file into the tasks list."""
    try:
        with open("tasks.txt", "r") as file:
            for line in file:
                tasks.append(line.strip())
        print("Tasks loaded successfully.")
    except FileNotFoundError:
        print("No previous tasks found. Starting fresh.")

def save_tasks():
    """Save the current list of tasks to tasks.txt."""
    with open("tasks.txt", "w") as file:
        for task in tasks:
            file.write(task + "\n")

def add_task(task_entry, task_listbox):
    """Add a new task to the list and update the GUI."""
    task = task_entry.get().strip()
    if not task:
        messagebox.showerror("Error", "Task cannot be empty.")
        return
    if task in tasks:
        messagebox.showinfo("Info", "Task already exists.")
    else:
        tasks.append(task)
        task_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
        messagebox.showinfo("Success", f"Task added: {task}")

def remove_task(task_listbox):
    """Remove the selected task from the list and update the GUI."""
    selected_task_index = task_listbox.curselection()
    if not selected_task_index:
        messagebox.showerror("Error", "No task selected.")
        return
    task = task_listbox.get(selected_task_index)
    tasks.remove(task)
    task_listbox.delete(selected_task_index)
    messagebox.showinfo("Success", f"Task removed: {task}")

def show_tasks(task_listbox):
    """Refresh the task listbox to display all tasks."""
    task_listbox.delete(0, tk.END)
    for task in tasks:
        task_listbox.insert(tk.END, task)

def on_exit():
    """Save tasks before exiting the application."""
    save_tasks()
    root.destroy()

# Create the main tkinter window
root = tk.Tk()
root.title("Task Manager")
root.geometry("400x500")

# Load tasks from file at the start
load_tasks()

# Create a frame for the input and buttons
frame = tk.Frame(root)
frame.pack(pady=10)

# Input field for adding a task
task_entry = tk.Entry(frame, width=30)
task_entry.grid(row=0, column=0, padx=5)

# Button to add a task
add_button = tk.Button(frame, text="Add Task", command=lambda: add_task(task_entry, task_listbox))
add_button.grid(row=0, column=1, padx=5)

# Listbox to display tasks
task_listbox = tk.Listbox(root, width=50, height=20)
task_listbox.pack(pady=10)

# Buttons for task operations
remove_button = tk.Button(root, text="Remove Task", command=lambda: remove_task(task_listbox))
remove_button.pack(pady=5)

refresh_button = tk.Button(root, text="Show Tasks", command=lambda: show_tasks(task_listbox))
refresh_button.pack(pady=5)

exit_button = tk.Button(root, text="Exit", command=on_exit)
exit_button.pack(pady=5)

# Populate the task listbox with existing tasks
show_tasks(task_listbox)

# Run the tkinter event loop
root.protocol("WM_DELETE_WINDOW", on_exit)
root.mainloop()