import tkinter as tk
from tkinter import filedialog, messagebox

valid_function_codes = {"10", "11", "20", "21", "30", "31", "32", "33", "40", "41", "42", "43"}

def convert_4bit_to_6bit(operation):
    """Convert a 4-digit string to a 6-digit string by converting function codes and numbers appropriately."""
    print(f"Converting operation: {operation}")  # Debug print
    # Check if the operation is exactly 4 digits
    if len(operation) == 4 and operation.isdigit():
        function_code = operation[:2]
        if function_code in valid_function_codes:
            # Convert to 6-digit by inserting '00' in the middle for function codes
            result = '0' + function_code + '0' + operation[2:]
        else:
            # Convert to 6-digit by prepending '00' for numeric values
            result = '00' + operation
        print(f"Converted to 6-bit: {result}")  # Debug print
        return result
    print(f"No conversion needed for: {operation}")  # Debug print
    return operation

def open_file(text_area):
    """Open a file, detect 4-digit operations, convert them to 6-digit if needed, and display the content."""
    file_path = filedialog.askopenfilename()
    if file_path:
        try:
            with open(file_path, 'r') as file:
                content = file.read()

            if len(content.splitlines()) > 250:
                messagebox.showerror("Error", "File exceeds the maximum allowed size of 250 lines.")
                return None
            
            print(f"Original content from file:\n{content}")  # Debug print
            
            # Convert content if it contains 4-digit operations
            converted_content = ""
            for line in content.splitlines():
                print(f"Processing line: {line}")  # Debug print
                if line.startswith('+'):
                    # Extract the numeric part
                    core_op = line[1:]
                    converted_op = convert_4bit_to_6bit(core_op)
                    converted_content += f"+{converted_op}\n"
                else:
                    converted_content += line + '\n'
            
            print(f"Converted content to display:\n{converted_content}")  # Debug print
            
            text_area.delete(1.0, tk.END)
            text_area.insert(tk.END, converted_content)
            return file_path
        except IOError as e:
            messagebox.showerror("Error", f"Unable to open file: {e}")
    return None

def save_file(text_area, current_file):
    """Save the content of the text area to a file."""
    if current_file:
        try:
            with open(current_file, 'w') as file:
                content = text_area.get(1.0, tk.END).strip()
                if len(content.splitlines()) > 250:
                    messagebox.showerror("Error", "Content exceeds the maximum allowed size of 250 lines.")
                    return
                file.write(content)
        except IOError as e:
            messagebox.showerror("Error", f"Unable to save file: {e}")
    else:
        save_file_as(text_area)

def save_file_as(text_area):
    """Prompt the user to select a file path and save the content of the text area to the selected file."""
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
    if file_path:
        try:
            with open(file_path, 'w') as file:
                content = text_area.get(1.0, tk.END).strip()
                if len(content.splitlines()) > 250:
                    messagebox.showerror("Error", "Content exceeds the maximum allowed size of 250 lines.")
                    return
                file.write(content)
        except IOError as e:
            messagebox.showerror("Error", f"Unable to save file: {e}")
        return file_path
    return None




# This is a tester gui just for the open and convert to 6 bit operations

# def create_gui():
#     """Create and display the Tkinter GUI."""
#     root = tk.Tk()
#     root.title("4-bit to 6-bit Converter")
    
#     text_area = tk.Text(root, wrap='word')
#     text_area.pack(expand=1, fill='both')
    
#     menu_bar = tk.Menu(root)
#     root.config(menu=menu_bar)
    
#     file_menu = tk.Menu(menu_bar, tearoff=0)
#     menu_bar.add_cascade(label="File", menu=file_menu)
#     file_menu.add_command(label="Open", command=lambda: open_file(text_area))
#     file_menu.add_command(label="Save", command=lambda: save_file(text_area, current_file))
#     file_menu.add_command(label="Save As", command=lambda: save_file_as(text_area))
#     file_menu.add_command(label="Exit", command=root.quit)
    
#     global current_file
#     current_file = None
    
#     root.mainloop()

# if __name__ == "__main__":
#     create_gui()
