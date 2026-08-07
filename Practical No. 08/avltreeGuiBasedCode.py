import heapq
import tkinter as tk
from tkinter import ttk, messagebox

class AVLNode:
    def __init__(self, key):
        self.key = key
        self.height = 1
        self.left = None
        self.right = None

class AVLTree:
    def insert(self, root, key):
        if root is None:
            return AVLNode(key)

        if key < root.key:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)

        root.height = 1 + max(self.get_height(root.left),
                              self.get_height(root.right))

        balance = self.get_balance(root)

        if balance > 1 and key < root.left.key:
            return self.right_rotate(root)

        if balance < -1 and key > root.right.key:
            return self.left_rotate(root)

        if balance > 1 and key > root.left.key:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)

        if balance < -1 and key < root.right.key:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

        return root

    def left_rotate(self, z):
        y = z.right
        t2 = y.left

        y.left = z
        z.right = t2

        z.height = 1 + max(self.get_height(z.left),
                           self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left),
                           self.get_height(y.right))

        return y

    def right_rotate(self, z):
        y = z.left
        t3 = y.right

        y.right = z
        z.left = t3

        z.height = 1 + max(self.get_height(z.left),
                           self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left),
                           self.get_height(y.right))

        return y

    def get_height(self, root):
        return root.height if root else 0

    def get_balance(self, root):
        if root is None:
            return 0
        return self.get_height(root.left) - self.get_height(root.right)

    def preorder(self, root):
        result = []

        def traverse(node):
            if node:
                result.append(str(node.key))
                traverse(node.left)
                traverse(node.right)

        traverse(root)
        return " ".join(result)

class TaskManager:
    def __init__(self):
        self.pq = []

    def add_task(self, priority, description):
        heapq.heappush(self.pq, (priority, description))

    def process(self):
        result = []
        while self.pq:
            p, t = heapq.heappop(self.pq)
            result.append(f"Priority {p} → {t}")
        return result

avl = AVLTree()
root = None
manager = TaskManager()


def insert_avl():
    global root
    try:
        value = int(avl_entry.get())
        root = avl.insert(root, value)
        preorder_box.config(state="normal")
        preorder_box.delete("1.0", tk.END)
        preorder_box.insert(tk.END, avl.preorder(root))
        preorder_box.config(state="disabled")
        avl_entry.delete(0, tk.END)
    except ValueError:
        messagebox.showerror("Error", "Enter an integer.")

def make_heap():
    try:
        nums = list(map(int, heap_entry.get().split(",")))

        min_heap = nums.copy()
        heapq.heapify(min_heap)

        max_heap = [-x for x in nums]
        heapq.heapify(max_heap)
        max_heap = [-x for x in max_heap]

        heap_output.config(state="normal")
        heap_output.delete("1.0", tk.END)
        heap_output.insert(
            tk.END,
            f"Min Heap : {min_heap}\n\nMax Heap : {max_heap}"
        )
        heap_output.config(state="disabled")

    except:
        messagebox.showerror(
            "Error",
            "Enter numbers separated by commas."
        )

def add_task():
    try:
        p = int(priority_entry.get())
        task = task_entry.get()

        if task == "":
            return

        manager.add_task(p, task)

        task_list.insert(tk.END, f"{p} : {task}")

        priority_entry.delete(0, tk.END)
        task_entry.delete(0, tk.END)

    except:
        messagebox.showerror("Error", "Invalid priority.")

def process_tasks():
    result = manager.process()

    task_output.config(state="normal")
    task_output.delete("1.0", tk.END)

    for i in result:
        task_output.insert(tk.END, i + "\n")

    task_output.config(state="disabled")
    task_list.delete(0, tk.END)

window = tk.Tk()
window.title("AVL Tree, Heap & Priority Queue")
window.geometry("850x700")

title = tk.Label(
    window,
    text="AVL Tree, Heap and Priority Queue Visualizer",
    font=("Arial", 18, "bold"),
    fg="blue"
)
title.pack(pady=10)

frame1 = ttk.LabelFrame(window, text="AVL Tree")
frame1.pack(fill="x", padx=10, pady=5)

avl_entry = ttk.Entry(frame1, width=20)
avl_entry.pack(side="left", padx=10, pady=10)

ttk.Button(frame1, text="Insert", command=insert_avl).pack(side="left")

tk.Label(frame1, text="Preorder Traversal").pack()

preorder_box = tk.Text(frame1, height=3)
preorder_box.pack(fill="x", padx=10, pady=5)
preorder_box.config(state="disabled")
frame2 = ttk.LabelFrame(window, text="Heap")
frame2.pack(fill="x", padx=10, pady=5)

heap_entry = ttk.Entry(frame2, width=50)
heap_entry.pack(side="left", padx=10, pady=10)

heap_entry.insert(0, "9,5,6,2,3")

ttk.Button(frame2, text="Create Heap", command=make_heap).pack(side="left")

heap_output = tk.Text(frame2, height=5)
heap_output.pack(fill="x", padx=10, pady=5)
heap_output.config(state="disabled")

frame3 = ttk.LabelFrame(window, text="Priority Queue")
frame3.pack(fill="both", expand=True, padx=10, pady=5)

priority_entry = ttk.Entry(frame3, width=8)
priority_entry.grid(row=0, column=0, padx=5, pady=5)

task_entry = ttk.Entry(frame3, width=40)
task_entry.grid(row=0, column=1, padx=5)

ttk.Button(frame3, text="Add Task", command=add_task).grid(row=0, column=2)

task_list = tk.Listbox(frame3, height=6)
task_list.grid(row=1, column=0, columnspan=3,
               padx=10, pady=5, sticky="ew")

ttk.Button(frame3,
           text="Process Tasks",
           command=process_tasks).grid(row=2, column=1, pady=5)

task_output = tk.Text(frame3, height=8)
task_output.grid(row=3, column=0,
                 columnspan=3,
                 padx=10,
                 pady=5,
                 sticky="ew")
task_output.config(state="disabled")

window.mainloop()