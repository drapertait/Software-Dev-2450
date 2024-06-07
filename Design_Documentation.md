# Design Document for Python Application

## High-Level Functionality
This Python application reads content from two text files (Test1.txt and Test2.txt), processes the data, and outputs the results in a user-friendly format. The application includes functionalities such as data validation, merging of data from both files, and displaying or storing the processed information.

## User Stories

User Stories

1) As a Computer Science Student, I want to load a BasicML program into the UVSim so that I can execute machine language instructions and observe their results.
 
2) As an Instructor, I want to provide students with a reliable and easy-to-use simulator so they can learn about machine language and computer architecture effectively.

## Use Cases

### 1. Read Data from Test1.txt
- **Description**: The system reads numeric data from Test1.txt.
- **Preconditions**: Test1.txt exists and is accessible.
- **Postconditions**: Data from Test1.txt is loaded into memory.
- **Actors**: System
- **Trigger**: User initiates the data reading process.
- **Flow**:
  1. User runs the application.
  2. The system checks for the existence of Test1.txt.
  3. The system reads the data from Test1.txt and loads it into memory.

### 2. Read Data from Test2.txt
- **Description**: The system reads numeric data from Test2.txt.
- **Preconditions**: Test2.txt exists and is accessible.
- **Postconditions**: Data from Test2.txt is loaded into memory.
- **Actors**: System
- **Trigger**: User initiates the data reading process.
- **Flow**:
  1. User runs the application.
  2. The system checks for the existence of Test2.txt.
  3. The system reads the data from Test2.txt and loads it into memory.

### 3. Validate Data Format
- **Description**: The system checks that all data entries are in the correct numeric format.
- **Preconditions**: Data has been read from Test1.txt and Test2.txt.
- **Postconditions**: Data entries are verified; invalid entries are flagged or removed.
- **Actors**: System
- **Trigger**: Data reading is complete.
- **Flow**:
  1. The system iterates through the data entries.
  2. The system checks each entry for numeric format.
  3. The system flags or removes invalid entries.

### 4. Merge Data from Both Files
- **Description**: The system combines data from Test1.txt and Test2.txt.
- **Preconditions**: Data from both files is loaded and validated.
- **Postconditions**: A merged dataset is created in memory.
- **Actors**: System
- **Trigger**: Data validation is complete.
- **Flow**:
  1. The system combines the validated data from Test1.txt and Test2.txt.
  2. The merged dataset is stored in memory.

### 5. Filter Duplicate Entries
- **Description**: The system removes duplicate entries from the merged dataset.
- **Preconditions**: Data is merged.
- **Postconditions**: The merged dataset contains only unique entries.
- **Actors**: System
- **Trigger**: Data merging is complete.
- **Flow**:
  1. The system identifies duplicate entries in the merged dataset.
  2. The system removes duplicate entries.

### 6. Sort Data
- **Description**: The system sorts the merged dataset in ascending order.
- **Preconditions**: Duplicate entries are removed.
- **Postconditions**: The dataset is sorted.
- **Actors**: System
- **Trigger**: Duplicate filtering is complete.
- **Flow**:
  1. The system sorts the dataset in ascending order.
  2. The sorted dataset is stored in memory.

### 7. Display Processed Data
- **Description**: The system displays the processed data in a user-friendly format.
- **Preconditions**: Data is sorted.
- **Postconditions**: Data is displayed to the user.
- **Actors**: System, User
- **Trigger**: Data sorting is complete.
- **Flow**:
  1. The system formats the sorted data.
  2. The system displays the formatted data to the user.



### 8. Log Errors and Warnings
- **Description**: The system logs any errors or warnings encountered during data processing.
- **Preconditions**: The application is running.
- **Postconditions**: Errors and warnings are logged.
- **Actors**: System
- **Trigger**: An error or warning occurs.
- **Flow**:
  1. The system detects an error or warning.
  2. The system logs the error or warning with details.


### 9. Provide Help and Documentation
- **Description**: The system provides help and documentation for using the application.
- **Preconditions**: The application is running.
- **Postconditions**: Readme.md and design_documentation.md are accessible to the user.
- **Actors**: User, System
- **Trigger**: User requests help or documentation.
- **Flow**:
  1. The user requests help or documentation.
  2. The system displays the relevant information.

### 10. Handle Missing Files Gracefully
- **Description**: The system handles cases where the input files are missing or inaccessible.
- **Preconditions**: The application is running.
- **Postconditions**: Appropriate error messages are displayed, and the system does not crash.
- **Actors**: System
- **Trigger**: A file is missing or inaccessible.
- **Flow**:
  1. The system checks for the existence of the input files.
  2. If a file is missing or inaccessible, the system displays an error message.
  3. The system continues running without crashing.

### 11. Multiply Accumulator

Description: Multiply the word in the accumulator by a word from a specific memory location.
Actors: User
Preconditions: UVSim is running a BasicML program.
Postconditions: Accumulator holds the result of the multiplication.
Inputs: None.
Outputs: Accumulator updated.

## 12. Branch

Description: Branch to a specific memory location.
Actors: User
Preconditions: UVSim is running a BasicML program.
Postconditions: Program counter is set to the specified memory location.
Inputs: None.
Outputs: Program counter updated.

### 13. Branch if Negative

Description: Branch to a specific memory location if the accumulator is negative.
Actors: User
Preconditions: UVSim is running a BasicML program.
Postconditions: If the accumulator is negative, the program counter is set to the specified memory location.
Inputs: None.
Outputs: Program counter updated if condition met.

### 14. Branch if Zero

Description: Branch to a specific memory location if the accumulator is zero.
Actors: User
Preconditions: UVSim is running a BasicML program.
Postconditions: If the accumulator is zero, the program counter is set to the specified memory location.
Inputs: None.
Outputs: Program counter updated if condition met.

### 15. Halt Program

Description: Stop the execution of the BasicML program.
Actors: User
Preconditions: UVSim is running a BasicML program.
Postconditions: Program execution is halted.
Inputs: None.
Outputs: Program stopped.




