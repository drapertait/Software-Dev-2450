This program simulates a simple machine language computer/UVSim. It reads instructions/BasicML from a file, loads the instructions into memory, and executes them. Instructions are fed via a text file where each line contains one instruction. The program is read into memory starting at address 0.

The first two digits of each BasicML instruction are the operation code specifying the operation to be performed, and the last two digits of the BasicML instruction are the operand – the address of the memory location containing the word to which the operation applies.

Table of Contents
1. Installation
2. Running the Application
3. Using the GUI
    - Main Window
    - File Menu
    - Control Panel
    - Output Display

Installation

Prerequisites
- Python 3.x

Running the Application

To run the application with the GUI, use the following command:
    python main.py

Using the GUI

Main Window
The main window of the GUI consists of three primary sections:
1. Load Program: For opening files.
2. Run: Executing the program.
3. Quit: Quits the program. 

Load program:
- After pressing load program you need find the document you would like to use on your computer.

Run:
- After pressing run, the file you selected will begin executing. Any needed information from the user will be prompted. 

Workflow
1. Open a File: Click on the "File" menu and select "Open" to load a UVSim file.
2. Run the Simulation: Use the "Run" button to execute the entire UVSim file or the "Step" button to execute it instruction by instruction.
3. View Output: Monitor the Output Display to see the results of the simulation.
5. Exit: Click on "Quit" to close the application when done.

Below is an example of what an instruction file should look like:

```
+1007
+1008
+2007
+2008
+2109
+1109
+4300
+0000
+0000
+0000
```


The available operations are as follows:

- **10xx**: Read (Input a number into memory location `xx`)
- **11xx**: Write (Output the number from memory location `xx`)
- **20xx**: Load (Load the number from memory location `xx` into the accumulator)
- **21xx**: Store (Store the number from the accumulator into memory location `xx`)
- **30xx**: Add (Add the number from memory location `xx` to the accumulator)
- **31xx**: Subtract (Subtract the number from memory location `xx` from the accumulator)
- **32xx**: Divide (Divide the accumulator by the number from memory location `xx`)
- **33xx**: Multiply (Multiply the accumulator by the number from memory location `xx`)
- **40xx**: Branch (Set the instruction counter to `xx`)
- **41xx**: Branch if negative (Set the instruction counter to `xx` if the accumulator is negative)
- **42xx**: Branch if zero (Set the instruction counter to `xx` if the accumulator is zero)
- **43xx**: Halt (Stop the program)


Troubleshooting

- Issue: The application does not start.
  - Solution: Ensure all prerequisites are installed and you are using the correct command to start the application.
  
- Issue: File does not load.
  - Solution: Verify that the file format is correct and the file is not corrupted.

- Issue: Buttons are unresponsive.
  - Solution: Ensure the application is not in the middle of executing a command and try again. Check the console for any error messages.

Contact
For further assistance, please contact the development team.
