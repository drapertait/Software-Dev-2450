from cpu_class import CPU
from memory_class import Memory


class Simulator:
    def __init__(self, output_function, loader):
        self.memory = Memory()
        self.cpu = CPU(self.memory, output_function)
        self.loader = loader

    def load_program_from_file(self, file_path):
        self.reset()  # Reset the simulator state before loading a new program
        program = self.loader.load_program_from_file(file_path)
        self.load_program(program)

    def load_program(self, program):
        if len(program) > 250:
            raise ValueError("Program exceeds the maximum allowed size of 250 commands ")
        for i, instruction in enumerate(program):
            self.memory.write(i, instruction)

    def run(self,converted_content):
        while self.cpu.instruction_counter < len(self.memory.memory):
            instruction = self.memory.read(self.cpu.instruction_counter)
            if converted_content:
                instructions = converted_content.splitlines()
                instruction = instructions[self.cpu.instruction_counter]
            self.cpu.instruction_counter += 1
            if self.cpu.execute_instruction(instruction):
                break

        self.cpu.output_function(f"Final accumulator value: {self.cpu.accumulator}")
        self.cpu.output_function(str(self.memory))

    def reset(self):
        self.memory.reset()
        self.cpu.reset()
