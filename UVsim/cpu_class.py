class CPU:
    def __init__(self, memory, output_function):
        self.accumulator = 0
        self.instruction_counter = 0
        self.memory = memory
        self.outputs = []
        self.output_function = output_function
        self.WORD_SIZE = 2**24  # 24-bit word size
        self.MAX_VALUE = 9999   # Maximum 4-digit value
        self.MIN_VALUE = -9999  # Minimum 4-digit value

    def check_overflow(self, value):
        if value > self.MAX_VALUE:
            return value - 2 * (self.MAX_VALUE + 1)
        elif value < self.MIN_VALUE:
            return value + 2 * (self.MAX_VALUE + 1)
        return value

    def execute_instruction(self, instruction):
        opcode = int(instruction) // 1000
        operand = int(instruction) % 1000

        if operand >= 250:
            self.output_function(f"Error: Invalid operand {operand}")
            return True
        
        if opcode == 10:
            self.read(operand)
        elif opcode == 11:
            self.write(operand)
        elif opcode == 20:
            self.load(operand)
        elif opcode == 21:
            self.store(operand)
        elif opcode == 30:
            self.add(operand)
        elif opcode == 31:
            self.subtract(operand)
        elif opcode == 32:
            self.divide(operand)
        elif opcode == 33:
            self.multiply(operand)
        elif opcode == 40:
            self.branch(operand)
        elif opcode == 41:
            self.branchneg(operand)
        elif opcode == 42:
            self.branchzero(operand)
        elif opcode == 43:
            return self.halt()

        return False

    def read(self, operand):
        value = int(self.output_function(
            f"Enter a number for memory location {operand}: "))
        self.memory.write(operand, value)
        output = f"Executed read (opcode 010) on memory location {operand:03d}: {value}"
        self.output_function(output, is_user_output=True)
        self.outputs.append(output)

    def write(self, operand):
        output = f"Executed write (opcode 011) on memory location {operand:03d}: {self.memory.read(operand)}"
        self.output_function(output, is_user_output=True)
        self.outputs.append(output)

    def load(self, operand):
        self.accumulator = self.memory.read(operand)
        self.output_function(
            f"Loaded value {self.accumulator} from memory location {operand:03d} into accumulator.")

    def store(self, operand):
        self.memory.write(operand, self.accumulator)
        self.output_function(
            f"Stored value {self.accumulator} from accumulator into memory location {operand:03d}.")

    def add(self, operand):
        self.accumulator += self.memory.read(operand)
        self.accumulator = self.check_overflow(self.accumulator)
        self.output_function(
            f"Added value from memory location {operand:03d}, new accumulator value: {self.accumulator}")

    def subtract(self, operand):
        self.accumulator -= self.memory.read(operand)
        self.accumulator = self.check_overflow(self.accumulator)
        self.output_function(
            f"Subtracted value from memory location {operand:03d}, new accumulator value: {self.accumulator}")

    def divide(self, operand):
        if self.memory.read(operand) == 0:
            self.output_function("Error: Division by zero")
            return
        self.accumulator //= self.memory.read(operand)
        self.output_function(
            f"Divided by value from memory location {operand:03d}, new accumulator value: {self.accumulator}")

    def multiply(self, operand):
        self.accumulator *= self.memory.read(operand)
        self.accumulator = self.check_overflow(self.accumulator)
        self.output_function(
            f"Multiplied by value from memory location {operand:03d}, new accumulator value: {self.accumulator}")

    def branch(self, operand):
        self.instruction_counter = operand

    def branchneg(self, operand):
        if self.accumulator < 0:
            self.instruction_counter = operand

    def branchzero(self, operand):
        if self.accumulator == 0:
            self.instruction_counter = operand

    def halt(self):
        self.output_function("Program encountered halt (043) opcode.")
        return True

    def reset(self):
        self.accumulator = 0
        self.instruction_counter = 0
        self.outputs = []
