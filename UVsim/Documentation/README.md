
# UVsim User Manual

## Project Setup Initial Setup

1. **Clone the Repository**
   ```sh
   git clone https://github.com/your-username/UVsim.git
   cd UVsim
   ```

2. **Set Up Virtual Environment**
   ```sh
   python -m venv UVsimVenv
   ```

3. **Activate the Virtual Environment**
   ```sh
   UVsimVenv\Scripts\activate  # On Windows
   # For MacOS/Linux use:
   # source UVsimVenv/bin/activate
   ```

4. **Install Requirements**
   ```sh
   pip install -r requirements.txt
   ```

### Running the Application

To start the UVsim GUI, simply run:
```sh
python uvsim_gui.py
```

## Menu Options and Their Functions

### 1. **Load Program**
- **Description**: Opens a file dialog to load a program into the simulator.
- **Steps**:
  1. Click the **Load Program** button.
  2. Select the program file you want to load from your file system.
  3. The program will be loaded into the simulator's memory.

### 2. **Save Program**
- **Description**: Opens a file dialog to save the current program from the text area.
- **Steps**:
  1. Click the **Save Program** button.
  2. Choose the location and name for the file to save the current program.
  3. The program will be saved to the specified location.

### 3. **Save Program As**
- **Description**: Similar to Save Program, but allows you to specify a new file name or location.
- **Steps**:
  1. Click the **Save Program As** button.
  2. Select the location and enter the name for the new file.
  3. The program will be saved to the new location with the specified name.

### 4. **Run Program**
- **Description**: Runs the loaded program in the simulator.
- **Steps**:
  1. Click the **Run Program** button.
  2. The simulator will execute the loaded program, displaying outputs as defined by the program logic.

### 5. **Reset Simulator**
- **Description**: Resets the simulator, clearing memory and resetting the state.
- **Steps**:
  1. Click the **Reset Simulator** button.
  2. The simulator will be reset to its initial state, clearing any loaded program and outputs.

### 6. **Apply Color Scheme**
- **Description**: Opens a dialog to apply a color scheme to the GUI.
- **Steps**:
  1. Click the **Apply Color Scheme** button.
  2. Select the desired color scheme from the options provided.
  3. The GUI will update to reflect the selected color scheme.

### To edit files:

- Load a program, makes changes in user output field, hit "save program", then reload that program again. 