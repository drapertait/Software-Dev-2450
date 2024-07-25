### Design Document for UVSim Project

---

#### Overview

The **UVSim** project is a simulation of a simplified computer, featuring a graphical user interface (GUI) for ease of interaction. It allows users to load, run, and interact with programs, providing insights into basic computer operations and instruction execution.

---

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
