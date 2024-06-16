import tkinter as tk
from tkinter import filedialog
from tkinter import simpledialog
from tkinter import messagebox


class SimulatorGUI:
    def __init__(self, simulator):
        self.simulator = simulator
        self.root = tk.Tk()
        self.root.title("Simulator GUI")

        # Create a frame for buttons
        self.button_frame = tk.Frame(self.root)
        self.button_frame.pack(pady=10)

        self.load_button = tk.Button(
            self.button_frame, text="Load Program", command=self.load_program, width=15)
        self.load_button.grid(row=0, column=0, padx=5)

        self.run_button = tk.Button(
            self.button_frame, text="Run", command=self.run_program, width=15)
        self.run_button.grid(row=0, column=1, padx=5)

        self.quit_button = tk.Button(
            self.button_frame, text="Quit", command=self.root.quit, width=15)
        self.quit_button.grid(row=0, column=2, padx=5)

        # Create a text widget for output
        self.output_text_label = tk.Label(self.root, text="Output:")
        self.output_text_label.pack(pady=5)

        self.output_text = tk.Text(
            self.root, wrap=tk.WORD, width=80, height=20)
        self.output_text.pack(pady=5)

        # Create a scrollbar for the text widget
        self.scrollbar = tk.Scrollbar(
            self.root, command=self.output_text.yview)
        self.output_text.configure(yscrollcommand=self.scrollbar.set)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    def load_program(self):
        file_path = filedialog.askopenfilename(
            title="Select Program File", filetypes=[("Text Files", "*.txt")])
        if file_path:
            self.simulator.load_program_from_file(file_path)
            self.output_text.insert(
                tk.END, f"Program loaded from {file_path}\n")
        else:
            self.output_text.insert(tk.END, "No file selected\n")

    def run_program(self):
        self.output_text.insert(tk.END, "Running program...\n")
        self.simulator.run()
        self.output_text.insert(tk.END, "Program executed.\n")

    def output_function(self, message):
        if message.startswith("Enter a number"):
            return simpledialog.askstring("Input", message)
        else:
            self.output_text.insert(tk.END, message + "\n")
            self.root.update()

    def start(self):
        self.root.mainloop()
