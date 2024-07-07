import tkinter as tk
from tkinter import filedialog


class UVsim:
    def __init__(self, simulator):
        self.simulator = simulator
        self.root = tk.Tk()
        self.root.title("UVsim GUI")

        # Frame for controls
        self.control_frame = tk.Frame(self.root)
        self.control_frame.pack(pady=10)

        self.load_button = tk.Button(
            self.control_frame, text="Load Program", command=self.load_program, width=15)
        self.load_button.grid(row=0, column=0, padx=5)

        self.run_button = tk.Button(
            self.control_frame, text="Run", command=self.run_program, width=15)
        self.run_button.grid(row=0, column=1, padx=5)

        # Frame for user input
        self.input_frame = tk.Frame(self.root)
        self.input_frame.pack(pady=10)

        self.prompt_label = tk.Label(self.input_frame, text="Input:")
        self.prompt_label.pack(side=tk.LEFT, padx=5)

        self.input_entry = tk.Entry(self.input_frame, width=50)
        self.input_entry.pack(side=tk.LEFT, padx=5)

        self.submit_button = tk.Button(
            self.input_frame, text="Submit", command=self.submit_input, width=10)
        self.submit_button.pack(side=tk.LEFT, padx=5)

        # Frame for user outputs
        self.output_frame = tk.Frame(self.root)
        self.output_frame.pack(pady=10)

        self.user_output_label = tk.Label(
            self.output_frame, text="User Output:")
        self.user_output_label.pack()

        self.user_output_text = tk.Text(
            self.output_frame, wrap=tk.WORD, width=80, height=10)
        self.user_output_text.pack(pady=5)

        self.user_scrollbar = tk.Scrollbar(
            self.output_frame, command=self.user_output_text.yview)
        self.user_output_text.configure(yscrollcommand=self.user_scrollbar.set)
        self.user_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # Frame for diagnostic messages
        self.diagnostic_frame = tk.Frame(self.root)
        self.diagnostic_frame.pack(pady=10)

        self.diagnostic_output_label = tk.Label(
            self.diagnostic_frame, text="Diagnostic Output:")
        self.diagnostic_output_label.pack()

        self.diagnostic_output_text = tk.Text(
            self.diagnostic_frame, wrap=tk.WORD, width=80, height=10)
        self.diagnostic_output_text.pack(pady=5)

        self.diagnostic_scrollbar = tk.Scrollbar(
            self.diagnostic_frame, command=self.diagnostic_output_text.yview)
        self.diagnostic_output_text.configure(
            yscrollcommand=self.diagnostic_scrollbar.set)
        self.diagnostic_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # Variable to store the input value
        self.input_value = None

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

    def submit_input(self):
        self.input_value = self.input_entry.get()
        self.input_entry.delete(0, tk.END)
        self.prompt_label.config(text="Input:")  # Reset the prompt label
        self.root.quit()  # Quit the main loop to continue execution

    def output_function(self, message, is_user_output=False):
        if message.startswith("Enter a number"):
            # Set the prompt label to the message
            self.prompt_label.config(text=message)
            self.root.mainloop()  # Wait for user input
            return self.input_value  # Return the user input
        elif is_user_output:
            self.user_output_text.insert(tk.END, message + "\n")
        else:
            self.diagnostic_output_text.insert(tk.END, message + "\n")
        self.root.update()

    def start(self):
        self.root.mainloop()
