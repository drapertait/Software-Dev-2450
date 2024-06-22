from cpu_class import CPU
from memory_class import Memory
from program_loader_class import ProgramLoader


class Simulator:
    def __init__(self, output_function):
        self.memory = Memory()
        self.cpu = CPU(self.memory, output_function)
        self.loader = ProgramLoader()

    def load_program_from_file(self, file_path):
        program = self.loader.load_program_from_file(file_path)
        self.load_program(program)

    def load_program(self, program):
        for i, instruction in enumerate(program):
            self.memory.write(i, instruction)

    def run(self):
        while self.cpu.instruction_counter < len(self.memory.memory):
            instruction = self.memory.read(self.cpu.instruction_counter)
            self.cpu.instruction_counter += 1
            if self.cpu.execute_instruction(instruction):
                break

        self.cpu.output_function(
            f"Final accumulator value: {self.cpu.accumulator}")
        self.cpu.output_function(str(self.memory))

    def reset(self):
        self.memory.reset()
        self.cpu.reset()
