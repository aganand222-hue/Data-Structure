import heapq
from collections import Counter
import tkinter as tk
from tkinter import ttk, messagebox

class Node:
    def __init__(self, char=None, freq=None):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq

def build_huffman_tree(frequencies):
    heap = [Node(char, freq) for char, freq in frequencies.items()]
    heapq.heapify(heap)

    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)

        merged = Node(freq=left.freq + right.freq)
        merged.left = left
        merged.right = right

        heapq.heappush(heap, merged)

    return heap[0]

def generate_codes(node, prefix="", codebook=None):
    if codebook is None:
        codebook = {}

    if node:
        if node.char is not None:
            codebook[node.char] = prefix

        generate_codes(node.left, prefix + "0", codebook)
        generate_codes(node.right, prefix + "1", codebook)

    return codebook

def huffman_encoding(data):
    if not data:
        return "", {}

    frequencies = Counter(data)
    root = build_huffman_tree(frequencies)
    codebook = generate_codes(root)

    encoded_data = "".join(codebook[ch] for ch in data)

    return encoded_data, codebook


def huffman_decoding(encoded_data, codebook):
    reverse = {v: k for k, v in codebook.items()}

    decoded = ""
    current = ""

    for bit in encoded_data:
        current += bit

        if current in reverse:
            decoded += reverse[current]
            current = ""

    return decoded

codebook = {}

def encode_text():
    global codebook

    text = input_box.get("1.0", tk.END).strip()

    if text == "":
        messagebox.showwarning("Warning", "Please enter some text.")
        return

    encoded, codebook = huffman_encoding(text)

    encoded_box.delete("1.0", tk.END)
    encoded_box.insert(tk.END, encoded)

    codebook_box.delete("1.0", tk.END)

    for ch, code in sorted(codebook.items()):
        if ch == " ":
            ch = "[space]"
        codebook_box.insert(tk.END, f"{ch} : {code}\n")

def decode_text():
    if not codebook:
        messagebox.showwarning("Warning", "Encode the text first.")
        return

    encoded = encoded_box.get("1.0", tk.END).strip()

    decoded = huffman_decoding(encoded, codebook)

    decoded_box.delete("1.0", tk.END)
    decoded_box.insert(tk.END, decoded)

def clear_all():
    input_box.delete("1.0", tk.END)
    encoded_box.delete("1.0", tk.END)
    decoded_box.delete("1.0", tk.END)
    codebook_box.delete("1.0", tk.END)

root = tk.Tk()
root.title("Huffman Coding Visualizer")
root.geometry("800x650")
root.resizable(False, False)

style = ttk.Style()
style.configure("TButton", font=("Arial", 11))

title = tk.Label(
    root,
    text="Huffman Coding Compression Tool",
    font=("Arial", 18, "bold"),
    fg="blue"
)
title.pack(pady=10)

tk.Label(root, text="Enter Text:", font=("Arial", 12, "bold")).pack()

input_box = tk.Text(root, height=4, width=80)
input_box.pack()

frame = tk.Frame(root)
frame.pack(pady=10)

ttk.Button(frame, text="Encode", command=encode_text).grid(row=0, column=0, padx=10)

ttk.Button(frame, text="Decode", command=decode_text).grid(row=0, column=1, padx=10)

ttk.Button(frame, text="Clear", command=clear_all).grid(row=0, column=2, padx=10)

tk.Label(root, text="Encoded Binary:", font=("Arial", 12, "bold")).pack()

encoded_box = tk.Text(root, height=4, width=80)
encoded_box.pack()

tk.Label(root, text="Decoded Text:", font=("Arial", 12, "bold")).pack()

decoded_box = tk.Text(root, height=4, width=80)
decoded_box.pack()

tk.Label(root, text="Huffman Codebook:", font=("Arial", 12, "bold")).pack()

codebook_box = tk.Text(root, height=10, width=40)
codebook_box.pack()

root.mainloop()