import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import ttk
from simulator_class import Simulator
from program_loader_class import ProgramLoader
from color_scheme import load_color_scheme, apply_color_scheme, set_color_scheme, get_contrasting_color
from file_operations import open_file, save_file, save_file_as

class UVsim:
    def __init__(self, simulator):
        self.simulator = simulator
        self.root = tk.Tk()
        self.root.title("UVsim GUI")

        # Load color scheme from configuration file
        self.primary_color, self.off_color = load_color_scheme()

        self.root.configure(bg=self.primary_color)

        # Branding
        self.branding_label = tk.Label(self.root, text="UVsim", font=("Helvetica", 24, "bold"), bg=self.primary_color, fg=get_contrasting_color(self.primary_color))
        self.branding_label.pack(pady=10)

        # Create main tab control
        self.main_tab_control = ttk.Notebook(self.root)
        self.main_tab_control.pack(expand=1, fill='both')

        # Frame for controls
        self.control_frame = tk.Frame(self.root, bg=self.primary_color)
        self.control_frame.pack(pady=10)

        self.new_tab_button = tk.Button(self.control_frame, text="New Main Tab", command=self.create_new_main_tab, width=15, bg=self.off_color, fg=get_contrasting_color(self.off_color))
        self.new_tab_button.grid(row=0, column=0, padx=5)

        self.load_button = tk.Button(self.control_frame, text="Load Program", command=self.load_program, width=15, bg=self.off_color, fg=get_contrasting_color(self.off_color))
        self.load_button.grid(row=0, column=1, padx=5)

        self.run_button = tk.Button(self.control_frame, text="Run", command=self.run_program, width=15, bg=self.off_color, fg=get_contrasting_color(self.off_color))
        self.run_button.grid(row=0, column=2, padx=5)

        self.reset_button = tk.Button(self.control_frame, text="Reset", command=self.reset_simulator, width=15, bg=self.off_color, fg=get_contrasting_color(self.off_color))
        self.reset_button.grid(row=0, column=3, padx=5)

        self.rerun_button = tk.Button(self.control_frame, text="Re-run", command=self.rerun_program, width=15, bg=self.off_color, fg=get_contrasting_color(self.off_color))
        self.rerun_button.grid(row=0, column=4, padx=5)

        self.save_button = tk.Button(self.control_frame, text="Save Program", command=self.save_program, width=15, bg=self.off_color, fg=get_contrasting_color(self.off_color))
        self.save_button.grid(row=0, column=5, padx=5)

        self.save_as_button = tk.Button(self.control_frame, text="Save As", command=self.save_program_as, width=15, bg=self.off_color, fg=get_contrasting_color(self.off_color))
        self.save_as_button.grid(row=0, column=6, padx=5)

        # Variable to store the input value and prompt status
        self.input_value = None
        self.prompt_active = False
        self.tab_files = {}  # Dictionary to store file paths for each tab
        self.tab_controls = {}  # Dictionary to store controls for each sub-tab

        # Add file, edit, and settings menus
        self.create_menus()

        # Apply the color scheme after creating widgets
        self.apply_color_scheme()

        # Create initial main tab
        self.create_new_main_tab()

    def create_menus(self):
        menubar = tk.Menu(self.root)

        # File menu
        file_menu = tk.Menu(menubar, tearoff=0)
        file_menu.add_command(label="New Main Tab", command=self.create_new_main_tab)
        file_menu.add_command(label="Open", command=self.load_program)
        file_menu.add_command(label="Save", command=self.save_program)
        file_menu.add_command(label="Save As", command=self.save_program_as)
        file_menu.add_separator()
        file_menu.add_command(label="Quit", command=self.root.quit)
        menubar.add_cascade(label="File", menu=file_menu)

        # Edit menu
        edit_menu = tk.Menu(menubar, tearoff=0)
        edit_menu.add_command(label="Cut", command=lambda: self.get_current_text_area().event_generate("<<Cut>>"))
        edit_menu.add_command(label="Copy", command=lambda: self.get_current_text_area().event_generate("<<Copy>>"))
        edit_menu.add_command(label="Paste", command=self.paste_text)
        menubar.add_cascade(label="Edit", menu=edit_menu)

        # Settings menu
        settings_menu = tk.Menu(menubar, tearoff=0)
        settings_menu.add_command(label="Color Scheme", command=lambda: set_color_scheme(self.root, self.get_current_text_area()))
        menubar.add_cascade(label="Settings", menu=settings_menu)

        self.root.config(menu=menubar)

    def create_new_main_tab(self):
        main_frame = tk.Frame(self.main_tab_control, bg=self.primary_color)
        self.main_tab_control.add(main_frame, text="Main Tab")

        sub_tab_control = ttk.Notebook(main_frame)
        sub_tab_control.pack(expand=1, fill='both')

        self.create_new_sub_tab(sub_tab_control)

        self.main_tab_control.select(len(self.main_tab_control.tabs()) - 1)

    def create_new_sub_tab(self, sub_tab_control):
        sub_frame = tk.Frame(sub_tab_control, bg=self.primary_color)
        sub_tab_control.add(sub_frame, text="Untitled")

        # Frame for user input
        input_frame = tk.Frame(sub_frame, bg=self.primary_color)
        input_frame.pack(pady=10)

        prompt_label = tk.Label(input_frame, text="Input:", bg=self.primary_color, fg=get_contrasting_color(self.primary_color))
        prompt_label.pack(side=tk.LEFT, padx=5)

        input_entry = tk.Entry(input_frame, width=50)
        input_entry.pack(side=tk.LEFT, padx=5)
        input_entry.bind("<Return>", self.submit_input)

        submit_button = tk.Button(input_frame, text="Submit", command=self.submit_input, width=10, bg=self.off_color, fg=get_contrasting_color(self.off_color))
        submit_button.pack(side=tk.LEFT, padx=5)

        # Frame for user outputs
        output_frame = tk.Frame(sub_frame, bg=self.primary_color)
        output_frame.pack(pady=10)

        user_output_label = tk.Label(output_frame, text="User Output:", bg=self.primary_color, fg=get_contrasting_color(self.primary_color))
        user_output_label.pack()

        user_output_text = tk.Text(output_frame, wrap=tk.WORD, width=80, height=10, bg=self.off_color, fg=get_contrasting_color(self.off_color))
        user_output_text.pack(pady=5)

        user_scrollbar = tk.Scrollbar(output_frame, command=user_output_text.yview)
        user_output_text.configure(yscrollcommand=user_scrollbar.set)
        user_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # Frame for diagnostic messages
        diagnostic_frame = tk.Frame(sub_frame, bg=self.primary_color)
        diagnostic_frame.pack(pady=10)

        diagnostic_output_label = tk.Label(diagnostic_frame, text="Diagnostic Output:", bg=self.primary_color, fg=get_contrasting_color(self.primary_color))
        diagnostic_output_label.pack()

        diagnostic_output_text = tk.Text(diagnostic_frame, wrap=tk.WORD, width=80, height=10, bg=self.off_color, fg=get_contrasting_color(self.off_color))
        diagnostic_output_text.pack(pady=5)

        diagnostic_scrollbar = tk.Scrollbar(diagnostic_frame, command=diagnostic_output_text.yview)
        diagnostic_output_text.configure(yscrollcommand=diagnostic_scrollbar.set)
        diagnostic_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        sub_frame.pack(fill='both', expand=1)

        # Ensure a new sub-tab is selected after creation
        if len(sub_tab_control.tabs()) > 0:
            sub_tab_control.select(len(sub_tab_control.tabs()) - 1)

        # Initialize entry in tab_files dictionary
        current_tab = sub_tab_control.select()
        self.tab_files[current_tab] = {'file_path': None}
        self.tab_controls[current_tab] = {
            'input_entry': input_entry,
            'user_output_text': user_output_text,
            'diagnostic_output_text': diagnostic_output_text,
            'prompt_label': prompt_label
        }

    def get_current_sub_tab_control(self):
        return self.main_tab_control.nametowidget(self.main_tab_control.select()).winfo_children()[0]

    def get_current_text_area(self):
        current_tab = self.get_current_sub_tab_control().select()
        return self.tab_controls[current_tab]['user_output_text']

    def get_current_diagnostic_area(self):
        current_tab = self.get_current_sub_tab_control().select()
        return self.tab_controls[current_tab]['diagnostic_output_text']

    def clear_outputs(self):
        self.get_current_text_area().delete(1.0, tk.END)
        self.get_current_diagnostic_area().delete(1.0, tk.END)

    def load_program(self):
        current_tab = self.get_current_sub_tab_control().select()
        file_path,converted_content = open_file(self.get_current_text_area())
        self.convert_content = converted_content
        self.get_current_diagnostic_area().insert(tk.END, f"Loading program from {file_path}\n")
        if file_path:
            # with open(file_path, 'r') as file:
            #     content = file.read()
            if len(converted_content.splitlines()) > 250:
                self.get_current_diagnostic_area().insert(tk.END, "Error: File exceeds the maximum allowed size of 250 lines.\n")
                return
            self.get_current_text_area().delete(1.0, tk.END)
            self.get_current_text_area().insert(tk.END, converted_content)
            self.simulator.load_program_from_file(file_path)
            self.get_current_diagnostic_area().insert(tk.END, f"Program loaded from {file_path}\n")
            self.tab_files[current_tab] = {'file_path': file_path}
            self.get_current_diagnostic_area().insert(tk.END, f"Stored file path for tab: {file_path}\n")
            # Ensure tab title is updated correctly
            sub_tab_control = self.get_current_sub_tab_control()
            if len(sub_tab_control.tabs()) > 0:
                sub_tab_control.tab(current_tab, text=file_path.split('/')[-1])
        else:
            self.get_current_diagnostic_area().insert(tk.END, "No file selected\n")

    def save_program(self):
        current_tab = self.get_current_sub_tab_control().select()
        file_path = self.tab_files[current_tab]['file_path']
        if file_path:
            with open(file_path, 'w') as file:
                content = self.get_current_text_area().get(1.0, tk.END).strip()
                if len(content.splitlines()) > 250:
                    self.get_current_diagnostic_area().insert(tk.END, "Error: Content exceeds the maximum allowed size of 250 lines.\n")
                    return
                file.write(content)
            self.get_current_diagnostic_area().insert(tk.END, "Program saved\n")
        else:
            self.save_program_as()

    def save_program_as(self):
        current_tab = self.get_current_sub_tab_control().select()
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
        if file_path:
            with open(file_path, 'w') as file:
                content = self.get_current_text_area().get(1.0, tk.END).strip()
                if len(content.splitlines()) > 250:
                    self.get_current_diagnostic_area().insert(tk.END, "Error: Content exceeds the maximum allowed size of 250 lines.\n")
                    return
                file.write(content)
            self.tab_files[current_tab]['file_path'] = file_path
            self.get_current_diagnostic_area().insert(tk.END, f"Program saved to {file_path}\n")
            self.get_current_sub_tab_control().tab(current_tab, text=file_path.split('/')[-1])
        else:
            self.get_current_diagnostic_area().insert(tk.END, "Save cancelled\n")

    def run_program(self):
        self.clear_outputs()  # Clear outputs before running the program
        program_code = self.get_current_text_area().get("1.0", tk.END).strip().splitlines()
        if len(program_code) > 250:
            messagebox.showerror("Error", "Program exceeds the maximum allowed size of 250 commands.")
            return
        program_code = [int(line) for line in program_code if line.strip().isdigit()]
        self.simulator.load_program(program_code)
        print(self.convert_content)
        self.simulator.run(self.convert_content)
        self.get_current_diagnostic_area().insert(tk.END, "Program executed.\n")

    def rerun_program(self):
        current_tab = self.get_current_sub_tab_control().select()
        file_path = self.tab_files[current_tab]['file_path']
        self.get_current_diagnostic_area().insert(tk.END, f"Attempting to rerun program from {file_path}\n")
        if file_path:
            self.clear_outputs()  # Clear outputs before running the program
            self.simulator.load_program_from_file(file_path)
            self.simulator.run()
            self.get_current_diagnostic_area().insert(tk.END, "Program rerun.\n")
        else:
            self.get_current_diagnostic_area().insert(tk.END, "No program loaded to rerun.\n")

    def reset_simulator(self):
        self.simulator.reset()
        self.get_current_diagnostic_area().insert(tk.END, "Simulator reset.\n")

    def paste_text(self):
        clipboard_content = self.root.clipboard_get()
        current_content = self.get_current_text_area().get("1.0", tk.END).strip().splitlines()
        new_content = clipboard_content.splitlines()
        if len(current_content) + len(new_content) > 250:
            messagebox.showerror("Error", "Pasting exceeds the maximum allowed size of 250 commands.")
            return
        self.get_current_text_area().insert(tk.INSERT, clipboard_content)

    def submit_input(self, event=None):
        if self.prompt_active:
            current_tab = self.get_current_sub_tab_control().select()
            self.input_value = self.tab_controls[current_tab]['input_entry'].get()
            self.tab_controls[current_tab]['input_entry'].delete(0, tk.END)
            self.tab_controls[current_tab]['prompt_label'].config(text="Input:")  # Reset the prompt label
            self.prompt_active = False
            self.root.quit()  # Quit the main loop to continue execution

    def output_function(self, message, is_user_output=False):
        current_tab = self.get_current_sub_tab_control().select()
        if message.startswith("Enter a number"):
            self.tab_controls[current_tab]['prompt_label'].config(text=message)
            self.prompt_active = True
            self.root.mainloop()  # Wait for user input
            return self.input_value  # Return the user input
        elif is_user_output:
            self.get_current_text_area().insert(tk.END, message + "\n")
        else:
            self.get_current_diagnostic_area().insert(tk.END, message + "\n")
        self.root.update()

    def apply_color_scheme(self):
        apply_color_scheme(self.root, self.primary_color, self.off_color)

    def start(self):
        self.root.mainloop()


if __name__ == "__main__":
    loader = ProgramLoader()
    gui = UVsim(None)
    simulator = Simulator(gui.output_function, loader)
    gui.simulator = simulator
    gui.start()

