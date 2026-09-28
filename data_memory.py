class DataMemory:
    def __init__(self, size=512):
        self.memory = [0] * (size // 4)  # 512 bytes, 4 bytes per word

    def read(self, address):
        return self.memory[address // 4]  # Read word

    def write(self, address, value):
        self.memory[address // 4] = value  # Write word

    def __str__(self):
        return "\n".join([f"Addr {i * 4}: {val}" for i, val in enumerate(self.memory)])