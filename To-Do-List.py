import tkinter as tk
from tkinter import ttk, messagebox

class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")
        self.root.geometry("500x500")
        self.tasks = []

        style = ttk.Style()
        style.configure("TButton", font=('Helvetica', 12))
        style.configure("TLabel", font=('Helvetica', 14))
        style.configure("TEntry", font=('Helvetica', 12))
        style.configure("TListbox", font=('Helvetica', 12))

        self.main_frame = ttk.Frame(root)
        self.main_frame.pack(pady=20)

        self.task_label = ttk.Label(self.main_frame, text="Enter a new task:")
        self.task_label.pack(pady=5)

        self.task_entry = ttk.Entry(self.main_frame, width=30)
        self.task_entry.pack(pady=5)

        self.add_task_btn = ttk.Button(self.main_frame, text="Add Task", command=self.add_task)
        self.add_task_btn.pack(pady=5)

        self.filter_var = tk.StringVar(value="All")
        self.filter_frame = ttk.Frame(root)
        self.filter_frame.pack(pady=10)

        self.all_radio = ttk.Radiobutton(self.filter_frame, text="All", variable=self.filter_var, value="All", command=self.update_listbox)
        self.all_radio.pack(side=tk.LEFT, padx=5)

        self.pending_radio = ttk.Radiobutton(self.filter_frame, text="Pending", variable=self.filter_var, value="Pending", command=self.update_listbox)
        self.pending_radio.pack(side=tk.LEFT, padx=5)

        self.done_radio = ttk.Radiobutton(self.filter_frame, text="Done", variable=self.filter_var, value="Done", command=self.update_listbox)
        self.done_radio.pack(side=tk.LEFT, padx=5)

        self.listbox_frame = ttk.Frame(root)
        self.listbox_frame.pack(pady=10)

        self.scrollbar = tk.Scrollbar(self.listbox_frame)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.listbox = tk.Listbox(self.listbox_frame, width=50, height=10, selectmode=tk.MULTIPLE, font=('Helvetica', 12), yscrollcommand=self.scrollbar.set)
        self.listbox.pack(pady=10, padx=10)

        self.scrollbar.config(command=self.listbox.yview)

        self.button_frame = ttk.Frame(root)
        self.button_frame.pack(pady=10)


        self.remove_task_btn = ttk.Button(self.button_frame, text="Remove Task", command=self.remove_task)
        self.remove_task_btn.pack(side=tk.LEFT, padx=5)

        self.mark_done_btn = ttk.Button(self.button_frame, text="Mark as Done", command=self.mark_task_done)
        self.mark_done_btn.pack(side=tk.LEFT, padx=5)

        self.exit_btn = ttk.Button(self.button_frame, text="Exit", command=root.quit)
        self.exit_btn.pack(side=tk.LEFT, padx=5)

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append({"task": task, "done": False})
            self.task_entry.delete(0, tk.END)
            self.update_listbox()
        else:
            messagebox.showwarning("Warning", "Please enter a task.")

    def remove_task(self):
        selected_tasks = self.listbox.curselection()
        if not selected_tasks:
            messagebox.showwarning("Warning", "Please select a task to remove.")
            return
        for index in selected_tasks[::-1]:
            del self.tasks[index]
        self.update_listbox()

    def mark_task_done(self):
        selected_tasks = self.listbox.curselection()
        if not selected_tasks:
            messagebox.showwarning("Warning", "Please select a task to mark as done.")
            return
        for index in selected_tasks:
            self.tasks[index]["done"] = True
        self.update_listbox()

    def update_listbox(self):
        self.listbox.delete(0, tk.END)
        filter_option = self.filter_var.get()
        for idx, task in enumerate(self.tasks, 1):
            status = "Done" if task["done"] else "Not Done"
            if filter_option == "All" or (filter_option == "Pending" and not task["done"]) or (filter_option == "Done" and task["done"]):
                self.listbox.insert(tk.END, f"{idx}. {task['task']} - {status}")

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()
