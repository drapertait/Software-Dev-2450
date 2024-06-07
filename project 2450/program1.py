# Math: logan
# read write load store: Tait
# branches and halt, read me : andrew
# input output: Vip
# team unit tests: Tait and logan 
# design document: Vip


memory = [0] * 100
accumulator = 0
instruction_counter = 0

def load_program(program):
    global memory
    for i, instruction in enumerate(program):
        memory[i] = instruction

def read(operand):
    global memory
    memory[operand] = int(input(f"Enter a number for memory location {operand}: "))

def write(operand):
    global memory
    print(f"Output from memory location {operand}: {memory[operand]}")

def load(operand):
    global accumulator, memory
    accumulator = memory[operand]
    print(f"Loaded value {accumulator} from memory location {operand} into accumulator.")

def store(operand):
    global accumulator, memory
    memory[operand] = accumulator
    print(f"Stored value {accumulator} from accumulator into memory location {operand}.")

def add(operand):
    global accumulator, memory
    accumulator += memory[operand]
    print(f"Added value from memory location {operand}, new accumulator value: {accumulator}")
    return accumulator

def subtract(operand,test=None):
    global accumulator, memory
    if test:
        memory[operand]=test
    accumulator -= memory[operand]
    print(f"Subtracted value from memory location {operand}, new accumulator value: {accumulator}")

def divide(operand,test=None):
    global accumulator, memory
    if test:
        memory[operand]=test
    if memory[operand] == 0:
        print("Error: Division by zero")
        return
    accumulator //= memory[operand]
    print(f"Divided by value from memory location {operand}, new accumulator value: {accumulator}")

def multiply(operand,test=None):
    global accumulator, memory
    if test:
        memory[operand]=test
    accumulator *= memory[operand]
    print(f"Multiplied by value from memory location {operand}, new accumulator value: {accumulator}")

def branch(operand):
    global instruction_counter
    instruction_counter = operand
    print(f"Branched to instruction at memory location {operand}.")
    return True

def branchneg(operand):
    global accumulator, instruction_counter
    if accumulator < 0:
        instruction_counter = operand
        print(f"Branched to instruction at memory location {operand} because accumulator is negative.")
        return True
    return False

def branchzero(operand):
    global accumulator, instruction_counter
    if accumulator == 0:
        instruction_counter = operand
        print(f"Branched to instruction at memory location {operand} because accumulator is zero.")
        return True
    return False

def halt():
    print("Program halted.")
    return True

def execute_instruction(instruction):
    global accumulator
    opcode = instruction // 100
    operand = instruction % 100

    if opcode == 10:
        read(operand)
    elif opcode == 11:
        write(operand)
    elif opcode == 20:
        load(operand)
    elif opcode == 21:
        store(operand)
    elif opcode == 30:
        add(operand)
    elif opcode == 31:
        subtract(operand)
    elif opcode == 32:
        divide(operand)
    elif opcode == 33:
        multiply(operand)
    elif opcode == 40:
        if branch(operand):
            return True
    elif opcode == 41:
        if branchneg(operand):
            return True
    elif opcode == 42:
        if branchzero(operand):
            return True
    elif opcode == 43:
        if halt():
            return True
    
    print(f"Accumulator after executing instruction {instruction}: {accumulator}")
    print_memory()
    return False

def print_memory():
    print("Memory content:")
    print("     " + " ".join(f"{i:4}" for i in range(10)))
    for i in range(0, len(memory), 10):
        print(f"{i:2} | " + " ".join(f"{memory[i+j]:4}" for j in range(10)))
    print()

def run():
    global instruction_counter
    while True:
        instruction = memory[instruction_counter]
        instruction_counter += 1
        if execute_instruction(instruction):
            break
    print_memory()
    print(f"Final accumulator value: {accumulator}")


def read_program_from_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    program = [int(line.strip()) for line in lines if line.strip()]
    return program

if __name__ == "__main__":
    
    while True:
        try:
            file = input("Please enter a file name (or press 'q' to quit): ")
            if file.lower() == 'q':
                print("Exiting program.")
                break
            if not file.endswith(".txt"):
                file += ".txt"
            program = read_program_from_file(file)
            load_program(program)
            run()
        except FileNotFoundError:
            print(f"Error: File '{file}' not found. Please try again.")
        except ValueError:
            print(f"Error: File '{file}' contains invalid data. Please check the file and try again.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}. Please try again.")
        finally:
            # Reset memory and registers for the next program
            memory = [0] * 100
            accumulator = 0
            instruction_counter = 0
    print("\n" + "-"*30 + "\n")

