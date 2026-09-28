class InstructionMemory:
    def __init__(self):
        self.memory = []

    def load_instructions(self, instructions):
        self.memory = instructions

    def __str__(self):
        return "\n".join(self.memory)
