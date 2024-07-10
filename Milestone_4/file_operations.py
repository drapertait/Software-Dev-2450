import tkinter as tk
from tkinter import filedialog

def open_file(text_area):
    file_path = filedialog.askopenfilename()
    if file_path:
        with open(file_path, 'r') as file:
            content = file.read()
        text_area.delete(1.0, tk.END)
        text_area.insert(tk.END, content)
        return file_path
    return None

def save_file(text_area, current_file):
    if current_file:
        with open(current_file, 'w') as file:
            file.write(text_area.get(1.0, tk.END))
    else:
        save_file_as(text_area)

def save_file_as(text_area):
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
    if file_path:
        with open(file_path, 'w') as file:
            file.write(text_area.get(1.0, tk.END))
        return file_path
    return None
