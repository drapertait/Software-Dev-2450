import tkinter as tk
from tkinter import filedialog, messagebox
import configparser
from simulator_class import Simulator


class UVsim:
    def __init__(self, simulator):
        self.simulator = simulator
        self.root = tk.Tk()
        self.root.title("UVsim GUI")

        # Load color scheme from configuration file
        self.config = configparser.ConfigParser()
        self.config.read('config.txt')
        self.primary_color = self.config.get(
            'DEFAULT', 'primary_color', fallback='#4C721D')
        self.off_color = self.config.get(
            'DEFAULT', 'off_color', fallback='#FFFFFF')

        self.root.configure(bg=self.primary_color)

        # Branding
        self.branding_label = tk.Label(self.root, text="UVsim", font=(
            "Helvetica", 24, "bold"), bg=self.primary_color, fg=self.off_color)
        self.branding_label.pack(pady=10)

        # Frame for controls
        self.control_frame = tk.Frame(self.root, bg=self.primary_color)
        self.control_frame.pack(pady=10)

        self.load_button = tk.Button(
            self.control_frame, text="Load Program", command=self.load_program, width=15, bg=self.off_color)
        self.load_button.grid(row=0, column=0, padx=5)

        self.run_button = tk.Button(
            self.control_frame, text="Run", command=self.run_program, width=15, bg=self.off_color)
        self.run_button.grid(row=0, column=1, padx=5)

        self.save_button = tk.Button(
            self.control_frame, text="Save Program", command=self.save_program, width=15, bg=self.off_color)
        self.save_button.grid(row=0, column=2, padx=5)

        self.add_button = tk.Button(
            self.control_frame, text="Add Command", command=self.add_command, width=15, bg=self.off_color)
        self.add_button.grid(row=0, column=3, padx=5)

        self.delete_button = tk.Button(
            self.control_frame, text="Delete Command", command=self.delete_command, width=15, bg=self.off_color)
        self.delete_button.grid(row=0, column=4, padx=5)

        # Frame for user input
        self.input_frame = tk.Frame(self.root, bg=self.primary_color)
        self.input_frame.pack(pady=10)

        self.prompt_label = tk.Label(
            self.input_frame, text="Input:", bg=self.primary_color, fg=self.off_color)
        self.prompt_label.pack(side=tk.LEFT, padx=5)

        self.input_entry = tk.Entry(self.input_frame, width=50)
        self.input_entry.pack(side=tk.LEFT, padx=5)
        self.input_entry.bind("<Return>", self.submit_input)

        self.submit_button = tk.Button(
            self.input_frame, text="Submit", command=self.submit_input, width=10, bg=self.off_color)
        self.submit_button.pack(side=tk.LEFT, padx=5)

        # Frame for user outputs
        self.output_frame = tk.Frame(self.root, bg=self.primary_color)
        self.output_frame.pack(pady=10)

        self.user_output_label = tk.Label(
            self.output_frame, text="User Output:", bg=self.primary_color, fg=self.off_color)
        self.user_output_label.pack()

        self.user_output_text = tk.Text(
            self.output_frame, wrap=tk.WORD, width=80, height=10, bg=self.off_color)
        self.user_output_text.pack(pady=5)

        self.user_scrollbar = tk.Scrollbar(
            self.output_frame, command=self.user_output_text.yview)
        self.user_output_text.configure(yscrollcommand=self.user_scrollbar.set)
        self.user_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # Frame for diagnostic messages
        self.diagnostic_frame = tk.Frame(self.root, bg=self.primary_color)
        self.diagnostic_frame.pack(pady=10)

        self.diagnostic_output_label = tk.Label(
            self.diagnostic_frame, text="Diagnostic Output:", bg=self.primary_color, fg=self.off_color)
        self.diagnostic_output_label.pack()

        self.diagnostic_output_text = tk.Text(
            self.diagnostic_frame, wrap=tk.WORD, width=80, height=10, bg=self.off_color)
        self.diagnostic_output_text.pack(pady=5)

        self.diagnostic_scrollbar = tk.Scrollbar(
            self.diagnostic_frame, command=self.diagnostic_output_text.yview)
        self.diagnostic_output_text.configure(
            yscrollcommand=self.diagnostic_scrollbar.set)
        self.diagnostic_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # Variable to store the input value and prompt status
        self.input_value = None
        self.prompt_active = False
        self.current_file = None  # Store the path of the current file

        # Add file and edit menus
        self.create_menus()

        # Apply the color scheme after creating widgets
        self.apply_color_scheme()

    def create_menus(self):
        menubar = tk.Menu(self.root)

        # File menu
        file_menu = tk.Menu(menubar, tearoff=0)
        file_menu.add_command(label="Open", command=self.load_program)
        file_menu.add_command(label="Save", command=self.save_program)
        file_menu.add_command(label="Save As", command=self.save_program_as)
        file_menu.add_separator()
        file_menu.add_command(label="Quit", command=self.root.quit)
        menubar.add_cascade(label="File", menu=file_menu)

        # Edit menu
        edit_menu = tk.Menu(menubar, tearoff=0)
        edit_menu.add_command(
            label="Cut", command=lambda: self.user_output_text.event_generate("<<Cut>>"))
        edit_menu.add_command(
            label="Copy", command=lambda: self.user_output_text.event_generate("<<Copy>>"))
        edit_menu.add_command(label="Paste", command=self.paste_text)
        menubar.add_cascade(label="Edit", menu=edit_menu)

        self.root.config(menu=menubar)

    def clear_outputs(self):
        self.user_output_text.delete(1.0, tk.END)
        self.diagnostic_output_text.delete(1.0, tk.END)

    def load_program(self):
        self.current_file = filedialog.askopenfilename()
        if self.current_file:
            with open(self.current_file, 'r') as file:
                content = file.read()
            self.user_output_text.delete(1.0, tk.END)
            self.user_output_text.insert(tk.END, content)
            self.simulator.load_program_from_file(self.current_file)
            self.diagnostic_output_text.insert(
                tk.END, f"Program loaded from {self.current_file}\n")
        else:
            self.diagnostic_output_text.insert(tk.END, "No file selected\n")

    def save_program(self):
        if self.current_file:
            with open(self.current_file, 'w') as file:
                file.write(self.user_output_text.get(1.0, tk.END))
            self.diagnostic_output_text.insert(tk.END, "Program saved\n")
        else:
            self.save_program_as()

    def save_program_as(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[
                                                 ("Text files", "*.txt"), ("All files", "*.*")])
        if file_path:
            with open(file_path, 'w') as file:
                file.write(self.user_output_text.get(1.0, tk.END))
            self.current_file = file_path
            self.diagnostic_output_text.insert(
                tk.END, f"Program saved to {file_path}\n")
        else:
            self.diagnostic_output_text.insert(tk.END, "Save cancelled\n")

    def run_program(self):
        self.clear_outputs()  # Clear outputs before running the program
        program_code = self.user_output_text.get(
            "1.0", tk.END).strip().splitlines()
        if len(program_code) > 100:
            messagebox.showerror(
                "Error", "Program exceeds the maximum allowed size of 100 commands.")
            return
        program_code = [int(line)
                        for line in program_code if line.strip().isdigit()]
        self.simulator.load_program(program_code)
        self.simulator.run()
        self.diagnostic_output_text.insert(tk.END, "Program executed.\n")

    def add_command(self):
        if len(self.user_output_text.get("1.0", tk.END).strip().splitlines()) >= 100:
            messagebox.showerror(
                "Error", "Cannot add more commands. Maximum limit of 100 reached.")
            return
        self.user_output_text.insert(tk.END, "0000\n")

    def delete_command(self):
        try:
            start, end = self.user_output_text.index(
                "sel.first"), self.user_output_text.index("sel.last")
            self.user_output_text.delete(start, end)
        except tk.TclError:
            messagebox.showwarning("Warning", "No text selected")

    def paste_text(self):
        clipboard_content = self.root.clipboard_get()
        current_content = self.user_output_text.get(
            "1.0", tk.END).strip().splitlines()
        new_content = clipboard_content.splitlines()
        if len(current_content) + len(new_content) > 100:
            messagebox.showerror(
                "Error", "Pasting exceeds the maximum allowed size of 100 commands.")
            return
        self.user_output_text.insert(tk.INSERT, clipboard_content)

    def submit_input(self, event=None):
        if self.prompt_active:
            self.input_value = self.input_entry.get()
            self.input_entry.delete(0, tk.END)
            self.prompt_label.config(text="Input:")  # Reset the prompt label
            self.prompt_active = False
            self.root.quit()  # Quit the main loop to continue execution

    def output_function(self, message, is_user_output=False):
        if message.startswith("Enter a number"):
            # Set the prompt label to the message
            self.prompt_label.config(text=message)
            self.prompt_active = True
            self.root.mainloop()  # Wait for user input
            return self.input_value  # Return the user input
        elif is_user_output:
            self.user_output_text.insert(tk.END, message + "\n")
        else:
            self.diagnostic_output_text.insert(tk.END, message + "\n")
        self.root.update()

    def apply_color_scheme(self):
        self.root.configure(bg=self.primary_color)
        self.control_frame.configure(bg=self.primary_color)
        self.load_button.configure(bg=self.off_color)
        self.run_button.configure(bg=self.off_color)
        self.save_button.configure(bg=self.off_color)
        self.add_button.configure(bg=self.off_color)
        self.delete_button.configure(bg=self.off_color)
        self.input_frame.configure(bg=self.primary_color)
        self.prompt_label.configure(bg=self.primary_color, fg=self.off_color)
        self.submit_button.configure(bg=self.off_color)
        self.output_frame.configure(bg=self.primary_color)
        self.user_output_label.configure(
            bg=self.primary_color, fg=self.off_color)
        self.user_output_text.configure(bg=self.off_color)
        self.diagnostic_frame.configure(bg=self.primary_color)
        self.diagnostic_output_label.configure(
            bg=self.primary_color, fg=self.off_color)
        self.diagnostic_output_text.configure(bg=self.off_color)

    def start(self):
        self.root.mainloop()
