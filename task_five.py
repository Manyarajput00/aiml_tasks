# import tkinter as tk
# from tkinter import messagebox

# # Main data list: stores tasks as (task_name, status)
# todo_list = []

# # --- Functions ---

# def add_task():
#     task_name = entry_task.get().strip()
#     if task_name:
#         todo_list.append((task_name, "Pending"))
#         entry_task.delete(0, tk.END)
#         refresh_tasks()
#     else:
#         messagebox.showwarning("Warning", "Task cannot be empty!")

# def refresh_tasks():
#     listbox_tasks.delete(0, tk.END)
#     for task, status in todo_list:
#         listbox_tasks.insert(tk.END, f"{task} [{status}]")

# def mark_done():
#     selected = listbox_tasks.curselection()
#     if selected:
#         index = selected[0]
#         task_name = todo_list[index][0]
#         todo_list[index] = (task_name, "Done")
#         refresh_tasks()
#     else:
#         messagebox.showinfo("Info", "Select a task to mark as done.")

# def remove_task():
#     selected = listbox_tasks.curselection()
#     if selected:
#         index = selected[0]
#         removed = todo_list.pop(index)
#         refresh_tasks()
#         messagebox.showinfo("Removed", f"Removed: {removed[0]}")
#     else:
#         messagebox.showinfo("Info", "Select a task to remove.")

# def show_slice():
#     try:
#         start = int(entry_start.get()) - 1
#         end = int(entry_end.get())
#         sliced = todo_list[start:end]
#         sliced_text = "\n".join([f"{i+1}. {task} [{status}]" for i, (task, status) in enumerate(sliced, start=start)])
#         messagebox.showinfo("Task Slice", sliced_text if sliced_text else "No tasks in this range.")
#     except:
#         messagebox.showerror("Error", "Invalid index range!")

# # --- GUI Setup ---
# window = tk.Tk()
# window.title("📝 To-Do List Manager")
# window.geometry("500x450")
# window.config(bg="white")

# # Task Entry
# entry_task = tk.Entry(window, font=("Arial", 14))
# entry_task.pack(pady=10)

# btn_add = tk.Button(window, text="Add Task", command=add_task, bg="#4CAF50", fg="white", font=("Arial", 12))
# btn_add.pack()

# # Task List
# listbox_tasks = tk.Listbox(window, width=50, height=10, font=("Arial", 12))
# listbox_tasks.pack(pady=10)

# # Buttons for actions
# frame_buttons = tk.Frame(window, bg="white")
# frame_buttons.pack(pady=5)

# btn_done = tk.Button(frame_buttons, text="Mark as Done", command=mark_done, bg="#2196F3", fg="white", width=15)
# btn_done.grid(row=0, column=0, padx=5)

# btn_remove = tk.Button(frame_buttons, text="Remove Task", command=remove_task, bg="#f44336", fg="white", width=15)
# btn_remove.grid(row=0, column=1, padx=5)

# # Slice Section
# frame_slice = tk.Frame(window, bg="white")
# frame_slice.pack(pady=10)

# tk.Label(frame_slice, text="Slice (start):", bg="white").grid(row=0, column=0)
# entry_start = tk.Entry(frame_slice, width=5)
# entry_start.grid(row=0, column=1, padx=5)

# tk.Label(frame_slice, text="Slice (end):", bg="white").grid(row=0, column=2)
# entry_end = tk.Entry(frame_slice, width=5)
# entry_end.grid(row=0, column=3, padx=5)

# btn_slice = tk.Button(frame_slice, text="Show Slice", command=show_slice, bg="#9C27B0", fg="white")
# btn_slice.grid(row=0, column=4, padx=10)

# # Start GUI
# window.mainloop()


print('hi manya here is your to do list manager')

tasks=[]

def add_task(task):
    add = (task,'pending')
    tasks.append(add)
    print(f'task {task} added sucessfully')

def remove_task(index):
    if 0<=index < len(tasks):
        removed_task = tasks.pop(index)
        print(f'task {removed_task[0]} remmoved task sucessfully')
    else:
        print('invalid task index')

def mark_done(task):
    for i,(t,status)in enumerate(tasks):
        if t==task:
            task[i]=(t,'done')
            print(f'task{task} is marked completely')
    else:
        print(f'task {task} not found')

def show_tasks():
    if not tasks:
        print('no task available')
    else:
        for i,(t,status) in enumerate(tasks):
            print(f'{i+1}. {t} [{status}]')
        
def show_slice(start, end):
    for i ,(t,status) in enumerate(tasks[start:end], start=start):
        print(f'{i+1}. {t} [{status}]')

# --- Sample Usage ---
add_task("Study DSA")
add_task("Buy groceries")
add_task("Read AI paper")
add_task("Workout")

show_tasks()

mark_done(2)  # Mark "Read AI paper" as done

remove_task(1)  # Remove "Buy groceries"

show_tasks()

# Show a slice (e.g., first two tasks)
show_slice(0, 2)

mark_done(2) 

