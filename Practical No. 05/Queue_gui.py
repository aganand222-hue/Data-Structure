import tkinter as tk
from tkinter import messagebox
from Queue_logic import Queue

q = None

def create_queue():
    global q
    try:
        size = int(size_entry.get())
        q = Queue(size)
        messagebox.showinfo("Success", "Queue Created Successfully")
        update_queue()
    except:
        messagebox.showerror("Error", "Enter Valid Queue Size")

def enqueue():
    if q is None:
        messagebox.showerror("Error", "Create Queue First")
        return

    item = item_entry.get()

    if item == "":
        messagebox.showwarning("Warning", "Enter an Item")
        return

    success, msg = q.enqueue(item)
    status.config(text=msg)

    if success:
        item_entry.delete(0, tk.END)

    update_queue()

def dequeue():
    if q is None:
        return

    success, msg = q.dequeue()
    status.config(text=msg)
    update_queue()

def peek():
    if q is None:
        return

    success, msg = q.peek()

    if success:
        messagebox.showinfo("Front Item", msg)
    else:
        messagebox.showwarning("Queue", msg)

def is_empty():
    if q is None:
        return

    if q.is_empty():
        messagebox.showinfo("Queue", "Queue is Empty")
    else:
        messagebox.showinfo("Queue", "Queue is Not Empty")

def is_full():
    if q is None:
        return

    if q.is_full():
        messagebox.showinfo("Queue", "Queue is Full")
    else:
        messagebox.showinfo("Queue", "Queue is Not Full")

def traverse():
    if q is None:
        return

    messagebox.showinfo("Queue", " -> ".join(map(str, q.traverse())))

def update_queue():
    queue_box.delete(0, tk.END)

    if q:
        for item in q.display_list():
            queue_box.insert(tk.END, item)

# ---------------- GUI ---------------- #

root = tk.Tk()
root.title("Queue GUI")
root.geometry("500x550")
root.configure(bg="#DDEEFF")

title = tk.Label(root,
                 text="QUEUE OPERATIONS",
                 font=("Arial", 20, "bold"),
                 bg="#DDEEFF",
                 fg="navy")

title.pack(pady=10)

frame = tk.Frame(root, bg="#DDEEFF")
frame.pack()

tk.Label(frame, text="Queue Size:", bg="#DDEEFF").grid(row=0, column=0)

size_entry = tk.Entry(frame, width=10)
size_entry.grid(row=0, column=1, padx=5)

tk.Button(frame,
          text="Create Queue",
          command=create_queue,
          bg="green",
          fg="white").grid(row=0, column=2)

frame2 = tk.Frame(root, bg="#DDEEFF")
frame2.pack(pady=15)

tk.Label(frame2,
         text="Item:",
         bg="#DDEEFF").grid(row=0, column=0)

item_entry = tk.Entry(frame2, width=20)
item_entry.grid(row=0, column=1)

button_frame = tk.Frame(root, bg="#DDEEFF")
button_frame.pack()

tk.Button(button_frame, text="Enqueue", width=12, command=enqueue).grid(row=0, column=0, padx=5, pady=5)
tk.Button(button_frame, text="Dequeue", width=12, command=dequeue).grid(row=0, column=1, padx=5, pady=5)
tk.Button(button_frame, text="Peek", width=12, command=peek).grid(row=1, column=0, padx=5, pady=5)
tk.Button(button_frame, text="Traverse", width=12, command=traverse).grid(row=1, column=1, padx=5, pady=5)
tk.Button(button_frame, text="Is Empty", width=12, command=is_empty).grid(row=2, column=0, padx=5, pady=5)
tk.Button(button_frame, text="Is Full", width=12, command=is_full).grid(row=2, column=1, padx=5, pady=5)

tk.Label(root,
         text="Queue Contents",
         font=("Arial", 12, "bold"),
         bg="#DDEEFF").pack(pady=10)

queue_box = tk.Listbox(root, width=40, height=10)
queue_box.pack()

status = tk.Label(root,
                  text="",
                  bg="#DDEEFF",
                  fg="blue",
                  font=("Arial", 11))

status.pack(pady=10)

tk.Button(root,
          text="Exit",
          command=root.destroy,
          bg="red",
          fg="white",
          width=15).pack(pady=10)

root.mainloop()
