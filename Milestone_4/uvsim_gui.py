import tkinter as tk
from tkinter import filedialog
from tkinter import simpledialog
from tkinter import messagebox


class UVsim:
    def __init__(self, simulator):
        self.simulator = simulator
        self.root = tk.Tk()
        self.root.title("UVsim GUI")

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

        # Create a text widget for user outputs
        self.user_output_label = tk.Label(self.root, text="User Output:")
        self.user_output_label.pack(pady=5)

        self.user_output_text = tk.Text(
            self.root, wrap=tk.WORD, width=80, height=10)
        self.user_output_text.pack(pady=5)

        # Create a scrollbar for the user output text widget
        self.user_scrollbar = tk.Scrollbar(
            self.root, command=self.user_output_text.yview)
        self.user_output_text.configure(yscrollcommand=self.user_scrollbar.set)
        self.user_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # Create a text widget for diagnostic messages
        self.diagnostic_output_label = tk.Label(
            self.root, text="Diagnostic Output:")
        self.diagnostic_output_label.pack(pady=5)

        self.diagnostic_output_text = tk.Text(
            self.root, wrap=tk.WORD, width=80, height=10)
        self.diagnostic_output_text.pack(pady=5)

        # Create a scrollbar for the diagnostic output text widget
        self.diagnostic_scrollbar = tk.Scrollbar(
            self.root, command=self.diagnostic_output_text.yview)
        self.diagnostic_output_text.configure(
            yscrollcommand=self.diagnostic_scrollbar.set)
        self.diagnostic_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    def clear_outputs(self):
        self.user_output_text.delete(1.0, tk.END)
        self.diagnostic_output_text.delete(1.0, tk.END)

    def load_program(self):
        file_path = filedialog.askopenfilename(
            title="Select Program File", filetypes=[("Text Files", "*.txt")])
        if file_path:
            self.clear_outputs()  # Clear outputs before loading new program
            self.simulator.load_program_from_file(file_path)
            self.diagnostic_output_text.insert(
                tk.END, f"Program loaded from {file_path}\n")
        else:
            self.diagnostic_output_text.insert(tk.END, "No file selected\n")

    def run_program(self):
        self.clear_outputs()  # Clear outputs before running the program
        self.diagnostic_output_text.insert(tk.END, "Running program...\n")
        self.simulator.run()
        self.diagnostic_output_text.insert(tk.END, "Program executed.\n")

    def output_function(self, message, is_user_output=False):
        if message.startswith("Enter a number"):
            return simpledialog.askstring("Input", message)
        elif is_user_output:
            self.user_output_text.insert(tk.END, message + "\n")
        else:
            self.diagnostic_output_text.insert(tk.END, message + "\n")
        self.root.update()

    def start(self):
        self.root.mainloop()
