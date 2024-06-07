# Software-Dev-2450

This program simulates a simple machine language computer/UVSim. It reads instructions/BasicML from a file, loads the instructions into memory, and executes them. Instructions are fed via a text file where each line contains one instruction. The program is read into memory starting at address 0.

The first two digits of each BasicML instruction are the operation code specifying the operation to be performed, and the last two digits of the BasicML instruction are the operand – the address of the memory location containing the word to which the operation applies. Below is an example of what an instruction file should look like:

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

## TO RUN THE PROGRAM

1. Open a terminal and navigate to the project folder (project 2450).
2. Ensure that the desired instruction file is in the project folder.
3. Run the following command:
   ```sh
   python3 program1.py
   ```

While running, the program will continuously prompt the user for instruction files until the user presses "q" to quit. Some operations may require user input; follow the prompts to complete each operation.
