class Memory:
    def __init__(self, size=100):
        self.memory = [0] * size

    def read(self, address):
        return self.memory[address]

    def write(self, address, value):
        self.memory[address] = value

    def reset(self):
        self.memory = [0] * len(self.memory)

    def __str__(self):
        return "\n".join(f"{i}: {val}" for i, val in enumerate(self.memory))
