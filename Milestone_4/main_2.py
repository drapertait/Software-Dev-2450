import tkinter as tk
from file_operations import open_file, save_file, save_file_as
from color_scheme import load_color_scheme, apply_color_scheme, set_color_scheme
import configparser

class UVSimGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("UVSim GUI")

        self.config = configparser.ConfigParser()
        self.config.read('config.txt')

        self.primary_color, self.off_color = load_color_scheme()
        self.current_file = None

        self.create_widgets()
        self.apply_color_scheme()

    def create_widgets(self):
        self.menu = tk.Menu(self.root)
        self.root.config(menu=self.menu)

        file_menu = tk.Menu(self.menu, tearoff=0)
        file_menu.add_command(label="Open", command=self.open_file)
        file_menu.add_command(label="Save", command=self.save_file)
        file_menu.add_command(label="Save As", command=self.save_file_as)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.root.quit)
        self.menu.add_cascade(label="File", menu=file_menu)

        edit_menu = tk.Menu(self.menu, tearoff=0)
        edit_menu.add_command(label="Cut", command=lambda: self.text_area.event_generate("<<Cut>>"))
        edit_menu.add_command(label="Copy", command=lambda: self.text_area.event_generate("<<Copy>>"))
        edit_menu.add_command(label="Paste", command=lambda: self.text_area.event_generate("<<Paste>>"))
        self.menu.add_cascade(label="Edit", menu=edit_menu)

        settings_menu = tk.Menu(self.menu, tearoff=0)
        settings_menu.add_command(label="Color Scheme", command=self.set_color_scheme)
        self.menu.add_cascade(label="Settings", menu=settings_menu)

        # Main GUI components
        self.text_area = tk.Text(self.root, wrap="word")
        self.text_area.pack(fill="both", expand=True)

        # Add additional GUI components
        self.additional_widgets()

    def additional_widgets(self):
        # Add your original GUI components here
        # For example, adding labels, buttons, and other widgets
        self.label = tk.Label(self.root, text="UVSim", font=("Helvetica", 16))
        self.label.pack(pady=10)

        self.run_button = tk.Button(self.root, text="Run", command=self.run_program)
        self.run_button.pack(pady=5)

        # You can continue adding more components as needed

    def run_program(self):
        # Implement the functionality for running the UVSim program
        pass

    def apply_color_scheme(self):
        apply_color_scheme(self.root, self.text_area, self.primary_color, self.off_color)

    def open_file(self):
        self.current_file = open_file(self.text_area)

    def save_file(self):
        save_file(self.text_area, self.current_file)

    def save_file_as(self):
        self.current_file = save_file_as(self.text_area)

    def set_color_scheme(self):
        set_color_scheme(self.root, self.text_area, self.config)

if __name__ == "__main__":
    root = tk.Tk()
    app = UVSimGUI(root)
    root.mainloop()
