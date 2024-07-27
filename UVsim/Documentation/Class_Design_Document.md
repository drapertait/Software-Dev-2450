### Design Document for UVSim Project

---

#### Overview

The **UVSim** project is a simulation of a simplified computer, featuring a graphical user interface (GUI) for ease of interaction. It allows users to load, run, and interact with programs, providing insights into basic computer operations and instruction execution.

---
#### User Stories
## User Story 1
- **Title:** Load Program
- **Description:** As a computer science student, I want to load a BasicML program into the simulator so that I can test and debug my machine language programs.

## User Story 2
- **Title:** Run Program
- **Description:** As a computer science student, I want to run a loaded BasicML program so that I can see the results of my machine language instructions.

## User Story 3
- **Title:** Save Program
- **Description:** As a computer science student, I want to save my BasicML program to a file so that I can edit or run it later without losing my progress.

## User Story 4
- **Title:** Reset Simulator
- **Description:** As a computer science student, I want to reset the simulator so that I can start fresh with a new program or rerun the current program from the beginning.

## User Story 5
- **Title:** Edit Program
- **Description:** As a computer science student, I want to edit the loaded BasicML program within the simulator so that I can make changes and correct errors directly.

## User Story 6
- **Title:** View Output
- **Description:** As a computer science student, I want to view the output of my BasicML program on the simulator's interface so that I can analyze the results of my instructions.

## User Story 7
- **Title:** Configure Color Scheme
- **Description:** As a computer science student, I want to configure the color scheme of the simulator's interface so that I can personalize the look and feel of the application.

## User Story 8
- **Title:** Multiple Tabs
- **Description:** As a computer science student, I want to open multiple BasicML programs in different tabs within the simulator so that I can work on and compare multiple programs simultaneously.

## User Story 9
- **Title:** Cut, Copy, and Paste
- **Description:** As a computer science student, I want to cut, copy, and paste instructions within the BasicML program editor so that I can easily modify and organize my code.

## User Story 10
- **Title:** Error Handling
- **Description:** As a computer science student, I want the simulator to provide clear error messages when my BasicML program contains mistakes so that I can quickly identify and fix the issues.

## User Story 11
- **Title:** Branch Operations
- **Description:** As a computer science student, I want to use branch operations (BRANCH, BRANCHNEG, BRANCHZERO) in my BasicML program so that I can control the flow of execution based on specific conditions.

## User Story 12
- **Title:** Arithmetic Operations
- **Description:** As a computer science student, I want to perform arithmetic operations (ADD, SUBTRACT, MULTIPLY, DIVIDE) in my BasicML program so that I can implement complex calculations.

## User Story 13
- **Title:** Load Data
- **Description:** As a computer science student, I want to load data values into memory locations so that I can use them in my BasicML program for various calculations.

## User Story 14
- **Title:** Input from Keyboard
- **Description:** As a computer science student, I want to read input from the keyboard into memory locations so that my BasicML program can interact with the user.

## User Story 15
- **Title:** Output to Screen
- **Description:** As a computer science student, I want to write output from memory locations to the screen so that my BasicML program can display results to the user.

#### User Cases
# Use Cases for UVsim Project

## Use Case 1: Load Program
- **Actor:** Computer Science Student
- **Description:** Load a BasicML program into the simulator.
- **Steps:**
  1. The student selects "Load Program" from the GUI.
  2. The student browses and selects the BasicML file from the file dialog.
  3. The selected program is loaded into the simulator's memory.
  4. The program is displayed in the editor area for review and modification.

## Use Case 2: Run Program
- **Actor:** Computer Science Student
- **Description:** Run the loaded BasicML program.
- **Steps:**
  1. The student selects "Run" from the GUI.
  2. The simulator executes the loaded program.
  3. The output of the program is displayed in the "User Output" area.
  4. Any errors or diagnostic messages are displayed in the "Diagnostic Output" area.

## Use Case 3: Save Program
- **Actor:** Computer Science Student
- **Description:** Save the current BasicML program to a file.
- **Steps:**
  1. The student selects "Save Program" from the GUI.
  2. The student chooses a location and filename in the file dialog.
  3. The current program is saved to the specified file.

## Use Case 4: Reset Simulator
- **Actor:** Computer Science Student
- **Description:** Reset the simulator to its initial state.
- **Steps:**
  1. The student selects "Reset" from the GUI.
  2. The simulator clears the current program from memory.
  3. The simulator's registers and memory are reset to their default values.

## Use Case 5: Edit Program
- **Actor:** Computer Science Student
- **Description:** Edit the loaded BasicML program.
- **Steps:**
  1. The student selects and modifies instructions directly in the editor area.
  2. The student can cut, copy, and paste instructions using the GUI or keyboard shortcuts.
  3. The student saves the changes by selecting "Save Program" or "Save As".

## Use Case 6: View Output
- **Actor:** Computer Science Student
- **Description:** View the output and diagnostic messages of the program.
- **Steps:**
  1. The student runs the program by selecting "Run" from the GUI.
  2. The program's output is displayed in the "User Output" area.
  3. Any errors or diagnostic messages are displayed in the "Diagnostic Output" area.

## Use Case 7: Configure Color Scheme
- **Actor:** Computer Science Student
- **Description:** Configure the color scheme of the simulator's interface.
- **Steps:**
  1. The student selects "Settings" from the menu bar.
  2. The student chooses "Color Scheme" from the settings menu.
  3. The student selects the desired primary and off-colors.
  4. The simulator updates the color scheme accordingly.

## Use Case 8: Multiple Tabs
- **Actor:** Computer Science Student
- **Description:** Open multiple BasicML programs in different tabs.
- **Steps:**
  1. The student selects "New Main Tab" from the GUI.
  2. A new tab is created with a blank program editor.
  3. The student loads or writes a program in the new tab.
  4. The student can switch between tabs to work on different programs.

## Use Case 9: Cut, Copy, and Paste
- **Actor:** Computer Science Student
- **Description:** Cut, copy, and paste instructions within the BasicML program editor.
- **Steps:**
  1. The student selects instructions in the editor area.
  2. The student uses the GUI or keyboard shortcuts to cut, copy, or paste the selected instructions.
  3. The student saves the changes by selecting "Save Program" or "Save As".

## Use Case 10: Error Handling
- **Actor:** Computer Science Student
- **Description:** Provide clear error messages when the BasicML program contains mistakes.
- **Steps:**
  1. The student runs the program by selecting "Run" from the GUI.
  2. The simulator detects errors in the program.
  3. Clear error messages are displayed in the "Diagnostic Output" area, indicating the type and location of errors.

## Use Case 11: Branch Operations
- **Actor:** Computer Science Student
- **Description:** Use branch operations (BRANCH, BRANCHNEG, BRANCHZERO) in the BasicML program.
- **Steps:**
  1. The student writes branch instructions in the program editor.
  2. The student runs the program by selecting "Run" from the GUI.
  3. The simulator executes the branch operations based on the conditions specified.
  4. The program flow changes according to the branch instructions.

## Use Case 12: Arithmetic Operations
- **Actor:** Computer Science Student
- **Description:** Perform arithmetic operations (ADD, SUBTRACT, MULTIPLY, DIVIDE) in the BasicML program.
- **Steps:**
  1. The student writes arithmetic instructions in the program editor.
  2. The student runs the program by selecting "Run" from the GUI.
  3. The simulator performs the arithmetic operations and updates the accumulator with the results.
  4. The output and diagnostic messages are displayed in their respective areas.

## Use Case 13: Load Data
- **Actor:** Computer Science Student
- **Description:** Load data values into memory locations.
- **Steps:**
  1. The student writes data values into specific memory locations in the program editor.
  2. The student runs the program by selecting "Run" from the GUI.
  3. The simulator loads the data values into the specified memory locations.
  4. The program executes using the loaded data.

## Use Case 14: Input from Keyboard
- **Actor:** Computer Science Student
- **Description:** Read input from the keyboard into memory locations.
- **Steps:**
  1. The student writes READ instructions in the program editor.
  2. The student runs the program by selecting "Run" from the GUI.
  3. The simulator prompts the user to enter input values.
  4. The entered values are stored in the specified memory locations.

## Use Case 15: Output to Screen
- **Actor:** Computer Science Student
- **Description:** Write output from memory locations to the screen.
- **Steps:**
  1. The student writes WRITE instructions in the program editor.
  2. The student runs the program by selecting "Run" from the GUI.
  3. The simulator outputs the values from the specified memory locations to the screen.
  4. The output is displayed in the "User Output" area.

### Components

#### 1. color_scheme.py

- **Functionality**: Handles loading, applying, setting, and saving color schemes for the GUI.
- **Libraries Used**: Tkinter, configparser.

#### 2. cpu_class.py

- **Functionality**: Contains the `CPU` class, simulating a simple CPU.
- **Key Features**:
  - Supports instructions: read, write, load, store, add, subtract, divide, multiply, branch, branchneg, branchzero, and halt.
  - Includes overflow checking, an output function, and a reset method.

#### 3. file_operations.py

- **Functionality**: Provides functions for converting 4-digit operations to 6-digit operations, opening a file, converting its content, and saving the content of a text area to a file or as a new file.
- **Libraries Used**: Tkinter, filedialog, messagebox.

#### 4. main.py

- **Functionality**: Initializes and starts the UVSim program by creating instances of `ProgramLoader`, `Simulator`, and `UVsim`, and linking them together.

#### 5. memory_class.py

- **Functionality**: Includes a `Memory` class with methods for reading, writing, and resetting memory, as well as a string representation of the memory contents.

#### 6. program_loader_class.py

- **Functionality**: Contains the `ProgramLoader` class with a method to load a program from a file, converting each line to an integer.

#### 7. simulator_class.py

- **Functionality**: Implements a `Simulator` class.
- **Key Features**:
  - Loads programs into memory.
  - Runs the programs using the `CPU` class.
  - Resets the simulator state.

#### 8. uvsim_gui.py

- **Functionality**: Defines the `UVsim` class for creating a Tkinter-based GUI for the UVSim program.
- **Key Features**:
  - Methods for creating and managing tabs.
  - Loading and saving programs.
  - Running and resetting the simulator.
  - Handling user inputs.
  - Applying color schemes.

---

### Project Workflow

1. **Initialization**:

   - The `main.py` script initializes the program by creating instances of `ProgramLoader`, `Simulator`, and `UVsim` classes, linking the simulator to the GUI.
2. **Loading Programs**:

   - Users can load a program file through the GUI.
   - The program is read and loaded into memory.
3. **Running Programs**:

   - Users can run the loaded program.
   - The CPU executes instructions sequentially, updating the accumulator and memory as needed, while displaying outputs and diagnostics in the GUI.
4. **User Interaction**:

   - The GUI provides facilities for user input, file management, and viewing outputs and diagnostics.
   - Users can customize the color scheme via the settings.
5. **Simulator Functions**:

   - The simulator can reset its state, load programs, and rerun programs.
   - The CPU performs basic arithmetic and control operations, simulating the execution of a simple computer program.

---

### Libraries and Dependencies

- **Tkinter**: For GUI components and interaction.
- **Configparser**: For handling configuration files.
- **filedialog, messagebox**: For file operations and user notifications.

---
