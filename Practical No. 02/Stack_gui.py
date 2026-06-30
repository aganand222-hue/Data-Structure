import tkinter as tk
from tkinter import messagebox
from Stack_operation import *

stack = Stack()

def push_item():
    value = entry.get()

    if value == "":
        messagebox.showwarning("Warning", "Enter a value")
        return

    stack.push(value)
    update_display()
    entry.delete(0, tk.END)


def pop_item():
    result = stack.pop()
    messagebox.showinfo("Pop: ", {"is Popped", result})
    update_display()

def peek_item():
    messagebox.showinfo("Peek: ", stack.peek())


def update_display():
    listbox.delete(0, tk.END)

    for item in stack.display():
        listbox.insert(tk.END, item)


def check_delimiter():
    exp = expr_entry.get()

    if delimiter_matching(exp):
        messagebox.showinfo("Result", "Balanced Expression")
    else:
        messagebox.showerror("Result", "Not Balanced")


def convert_prefix():
    exp = prefix_entry.get()

    try:
        result = prefix_to_postfix(exp)
        postfix_label.config(text="Postfix : " + result)
    except:
        postfix_label.config(text="Invalid Expression")


def evaluate():
    exp = postfix_entry.get()

    try:
        result = evaluate_postfix(exp)
        result_label.config(text="Result : " + str(result))
    except:
        result_label.config(text="Invalid Expression")

root = tk.Tk()
root.title("Stack Operations")
root.geometry("550x650")

title = tk.Label(root,
                 text="STACK IMPLEMENTATION",
                 font=("Arial", 18, "bold"))
title.pack(pady=10)

entry = tk.Entry(root, font=("Arial", 14))
entry.pack()

tk.Button(root,
          text="Push",
          width=15,
          command=push_item).pack(pady=5)

tk.Button(root,
          text="Pop",
          width=15,
          command=pop_item).pack()

tk.Button(root,
          text="Peek",
          width=15,
          command=peek_item).pack(pady=5)

listbox = tk.Listbox(root,
                     width=25,
                     height=8,
                     font=("Arial", 13))

listbox.pack(pady=10)

tk.Label(root,
         text="Delimiter Matching",
         font=("Arial", 14, "bold")).pack()

expr_entry = tk.Entry(root, width=35)
expr_entry.pack()

tk.Button(root,
          text="Check",
          command=check_delimiter).pack(pady=5)

tk.Label(root,
         text="Prefix to Postfix",
         font=("Arial", 14, "bold")).pack()

prefix_entry = tk.Entry(root, width=35)
prefix_entry.pack()

tk.Button(root,
          text="Convert",
          command=convert_prefix).pack()

postfix_label = tk.Label(root, text="")
postfix_label.pack()


tk.Label(root,
         text="Evaluate Postfix",
         font=("Arial", 14, "bold")).pack()

postfix_entry = tk.Entry(root, width=35)
postfix_entry.pack()

tk.Button(root,
          text="Evaluate",
          command=evaluate).pack()

result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()