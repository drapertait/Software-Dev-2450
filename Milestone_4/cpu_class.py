class CPU:
    def __init__(self, memory, output_function):
        self.accumulator = 0
        self.instruction_counter = 0
        self.memory = memory
        self.outputs = []
        self.output_function = output_function
        self.WORD_SIZE = 2**15  # 16-bit word size

    def check_overflow(self, value):
        if value >= self.WORD_SIZE:
            return value - 2 * self.WORD_SIZE
        elif value < -self.WORD_SIZE:
            return value + 2 * self.WORD_SIZE
        return value

    def execute_instruction(self, instruction):
        opcode = instruction // 100
        operand = instruction % 100

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
        output = f"Executed read (opcode 10) on memory location {operand}: {value}"
        self.output_function(output, is_user_output=True)
        self.outputs.append(output)

    def write(self, operand):
        output = f"Executed write (opcode 11) on memory location {operand}: {self.memory.read(operand)}"
        self.output_function(output, is_user_output=True)
        self.outputs.append(output)

    def load(self, operand):
        self.accumulator = self.memory.read(operand)
        self.output_function(
            f"Loaded value {self.accumulator} from memory location {operand} into accumulator.")

    def store(self, operand):
        self.memory.write(operand, self.accumulator)
        self.output_function(
            f"Stored value {self.accumulator} from accumulator into memory location {operand}.")

    def add(self, operand):
        self.accumulator += self.memory.read(operand)
        self.accumulator = self.check_overflow(self.accumulator)
        self.output_function(
            f"Added value from memory location {operand}, new accumulator value: {self.accumulator}")

    def subtract(self, operand):
        self.accumulator -= self.memory.read(operand)
        self.accumulator = self.check_overflow(self.accumulator)
        self.output_function(
            f"Subtracted value from memory location {operand}, new accumulator value: {self.accumulator}")

    def divide(self, operand):
        if self.memory.read(operand) == 0:
            self.output_function("Error: Division by zero")
            return
        self.accumulator //= self.memory.read(operand)
        self.output_function(
            f"Divided by value from memory location {operand}, new accumulator value: {self.accumulator}")

    def multiply(self, operand):
        self.accumulator *= self.memory.read(operand)
        self.accumulator = self.check_overflow(self.accumulator)
        self.output_function(
            f"Multiplied by value from memory location {operand}, new accumulator value: {self.accumulator}")

    def branch(self, operand):
        self.instruction_counter = operand

    def branchneg(self, operand):
        if self.accumulator < 0:
            self.instruction_counter = operand

    def branchzero(self, operand):
        if self.accumulator == 0:
            self.instruction_counter = operand

    def halt(self):
        self.output_function("Program encountered halt (43) opcode.")
        self.output_function(
            "Outputs from read and write operations (opcode 10 and 11) up to this point:", is_user_output=True)
        for output in self.outputs:
            self.output_function(output, is_user_output=True)
        return True

    def reset(self):
        self.accumulator = 0
        self.instruction_counter = 0
        self.outputs = []
