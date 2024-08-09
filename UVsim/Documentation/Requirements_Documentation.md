### UVSim Requirements:

#### Project Overview

An important and influential educational client has hired your company to develop a software simulator called UVSim for computer science students to learn machine language and computer architecture. Students can execute their machine language programs on the simulator.

#### BasicML Overview

The UVSim is a simple virtual machine that interprets a machine language called BasicML. It includes a CPU, register, and main memory. An accumulator is used for calculations. The UVSim handles words as signed four-digit decimal numbers (+1234, -5678). The UVSim is equipped with a 100-word memory, referenced by location numbers 00 to 99.

##### BasicML Vocabulary

- **I/O Operations:**
  - READ (10): Read a word from the keyboard into memory.
  - WRITE (11): Write a word from memory to the screen.
- **Load/Store Operations:**
  - LOAD (20): Load a word from memory into the accumulator.
  - STORE (21): Store a word from the accumulator into memory.
- **Arithmetic Operations:**
  - ADD (30): Add a word from memory to the accumulator.
  - SUBTRACT (31): Subtract a word from memory from the accumulator.
  - DIVIDE (32): Divide the accumulator by a word from memory.
  - MULTIPLY (33): Multiply a word from memory by the accumulator.
- **Control Operations:**
  - BRANCH (40): Branch to a specific location in memory.
  - BRANCHNEG (41): Branch if the accumulator is negative.
  - BRANCHZERO (42): Branch if the accumulator is zero.
  - HALT (43): Stop the program.

##### Instruction Format

Each instruction is a signed four-digit or 6-digit decimal number. The first two/three digits are the operation code, and the last two/three digits are the operand (memory address).

#### Milestone 1-2 Deliverables

1. **Design Document (20 pts)**

   - Two User Stories
   - 10-15 Use Cases
2. **Working Prototype (40 pts)**

   - Command-line application
   - Input file processing
3. **Unit Tests (30 pts)**

   - Two unit tests per use case (20-30 total)
   - Spreadsheet listing all unit tests
4. **Other Documents (10 pts)**

   - README.txt with usage instructions
   - Meeting reports

#### Milestone 3 Deliverables

1. **Modifications from Previous Milestone (10 pts)**

   - Address feedback and TODO items.
2. **GUI Design Document (10 pts)**

   - Wireframe diagram of the GUI
   - Label and explain all controls
3. **Code Changes (35 pts)**

   - Implement the GUI
   - Ensure functionality matches the command-line version
4. **Class Definition Document (15 pts)**

   - Describe all classes, interfaces, and functions
   - Include input parameters, return values, pre- and post-conditions
5. **Software Requirement Specification (SRS) Documents (20 pts)**

   - Each team member creates an individual SRS document
   - Merge documents into a final team SRS document
6. **Other Documents (10 pts)**

   - Revised README.txt
   - Meeting reports

#### Milestone 4 Deliverables

1. **Revisions To Previous Milestone (10 pts)**

   - Address feedback and TODO items.
2. **New Design Modifications (50 pts)**

   - Branding with configurable color schemes
   - Support for loading, viewing, and editing files in the GUI
   - Save files to user-chosen directories
   - Allow multiple files to be open simultaneously
3. **Design Document Updates (30 pts)**

   - Update all design documents to reflect new features
4. **Other Documents (10 pts)**

   - Meeting reports

### Milestone 5 Functional Changes for Six-Digit Commands

1. **Expand Memory and Word Size**

   - Increase memory to 250 words (addresses 000 to 249)
   - Change word size to six digits
2. **Support Six-Digit Operations**

   - Prepend zero to function codes (e.g., 010 for READ)
3. **Support Both 4-Digit and 6-Digit Files**

   - Convert 4-digit files to 6-digit format
   - Differentiate between file formats
4. **Multiple File Support**

   - Open multiple files simultaneously within the GUI
