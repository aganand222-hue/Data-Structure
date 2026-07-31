import tkinter as tk
from tkinter import ttk, messagebox
from priority_queue import PriorityQueue

root = tk.Tk()
root.withdraw()

capacity_window = tk.Toplevel()
capacity_window.title("Priority Queue Capacity")
capacity_window.geometry("300x150")
capacity_window.resizable(False, False)

capacity = tk.IntVar()

def start_program():
    global pq
    try:
        cap = int(capacity.get())
        if cap <= 0:
            raise ValueError
        pq = PriorityQueue(cap)
        capacity_window.destroy()
        root.deiconify()
    except:
        messagebox.showerror("Error", "Enter a valid capacity.")

tk.Label(capacity_window, text="Enter Maximum Capacity",
         font=("Arial", 12)).pack(pady=10)

tk.Entry(capacity_window, textvariable=capacity,
         justify="center").pack()

tk.Button(capacity_window, text="Start",
          command=start_program).pack(pady=15)

root.title("Priority Queue GUI")
root.geometry("700x550")
root.resizable(False, False)


title = tk.Label(root,
                 text="PRIORITY QUEUE MANAGEMENT",
                 font=("Arial",18,"bold"),
                 fg="blue")

title.pack(pady=10)

frame = tk.Frame(root)
frame.pack()

tk.Label(frame,text="Item",font=("Arial",11)).grid(row=0,column=0,padx=10,pady=5)
item_entry=tk.Entry(frame,width=20)
item_entry.grid(row=0,column=1)

tk.Label(frame,text="Priority",font=("Arial",11)).grid(row=1,column=0,padx=10,pady=5)
priority_entry=tk.Entry(frame,width=20)
priority_entry.grid(row=1,column=1)

tree=ttk.Treeview(root,columns=("Item","Priority"),show="headings",height=10)

tree.heading("Item",text="Item")
tree.heading("Priority",text="Priority")

tree.column("Item",width=250,anchor="center")
tree.column("Priority",width=150,anchor="center")

tree.pack(pady=15)


status=tk.Label(root,text="Status : Ready",
                fg="green",
                font=("Arial",11))

status.pack()

def refresh(queue):

    tree.delete(*tree.get_children())

    for item,priority in queue:
        tree.insert("",tk.END,values=(item,priority))


def enqueue():

    item=item_entry.get()

    try:
        priority=int(priority_entry.get())
    except:
        messagebox.showerror("Error","Priority must be integer")
        return

    if pq.enqueue(item,priority):

        refresh(pq.traverse())

        status.config(text=f"Status : {item} inserted successfully",
                      fg="green")

        item_entry.delete(0,tk.END)
        priority_entry.delete(0,tk.END)

    else:
        messagebox.showwarning("Full","Priority Queue is Full")

def dequeue():

    value=pq.dequeue()

    if value is None:
        messagebox.showwarning("Empty","Priority Queue is Empty")
    else:

        refresh(pq.traverse())

        status.config(text=f"Status : Removed {value[0]}",
                      fg="red")

def traverse():

    refresh(pq.traverse())

def ascending():

    refresh(pq.ascending())

def descending():

    refresh(pq.descending())

def empty():

    if pq.is_empty():
        messagebox.showinfo("Status","Priority Queue is Empty")
    else:
        messagebox.showinfo("Status","Priority Queue is Not Empty")

def full():

    if pq.is_full():
        messagebox.showinfo("Status","Priority Queue is Full")
    else:
        messagebox.showinfo("Status","Priority Queue is Not Full")

button_frame=tk.Frame(root)
button_frame.pack(pady=10)

tk.Button(button_frame,text="Enqueue",width=15,
          command=enqueue,bg="lightgreen").grid(row=0,column=0,padx=5,pady=5)

tk.Button(button_frame,text="Dequeue",width=15,
          command=dequeue,bg="tomato").grid(row=0,column=1,padx=5,pady=5)

tk.Button(button_frame,text="Traverse",width=15,
          command=traverse).grid(row=1,column=0,padx=5,pady=5)

tk.Button(button_frame,text="Ascending",width=15,
          command=ascending).grid(row=1,column=1,padx=5,pady=5)

tk.Button(button_frame,text="Descending",width=15,
          command=descending).grid(row=2,column=0,padx=5,pady=5)

tk.Button(button_frame,text="Check Empty",width=15,
          command=empty).grid(row=2,column=1,padx=5,pady=5)

tk.Button(button_frame,text="Check Full",width=15,
          command=full).grid(row=3,column=0,padx=5,pady=5)

tk.Button(button_frame,text="Exit",width=15,
          bg="red",fg="white",
          command=root.destroy).grid(row=3,column=1,padx=5,pady=5)

root.mainloop()