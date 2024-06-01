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
    memory[operand] = int(input("Enter a number: "))

def write(operand):
    global memory
    print(memory[operand])

def load(operand):
    global accumulator, memory
    accumulator = memory[operand]

def store(operand):
    global accumulator, memory
    memory[operand] = accumulator

def add(operand):
    global accumulator, memory
    accumulator += memory[operand]

def subtract(operand):
    global accumulator, memory
    accumulator -= memory[operand]

def divide(operand):
    global accumulator, memory
    if memory[operand] == 0:
        print("Error: Division by zero")
        return
    accumulator //= memory[operand]

def multiply(operand):
    global accumulator, memory
    accumulator *= memory[operand]

def branch(operand):
    global instruction_counter
    instruction_counter = operand
    return True

def branchneg(operand):
    global accumulator, instruction_counter
    if accumulator < 0:
        instruction_counter = operand
        return True
    return False

def branchzero(operand):
    global accumulator, instruction_counter
    if accumulator == 0:
        instruction_counter = operand
        return True
    return False

def halt():
    print("Program halted.")
    return True

def execute_instruction(instruction):
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
        return branch(operand)
    elif opcode == 41:
        return branchneg(operand)
    elif opcode == 42:
        return branchzero(operand)
    elif opcode == 43:
        return halt()

    return False

def run():
    global instruction_counter
    while True:
        instruction = memory[instruction_counter]
        instruction_counter += 1
        if execute_instruction(instruction):
            break

if __name__ == "__main__":
    program = [
        1007,  # READ into location 07
        2007,  # LOAD from location 07
        2108,  # STORE into location 08
        1108,  # WRITE from location 08
        4300,  # HALT
    ]
    load_program(program)
    run()
