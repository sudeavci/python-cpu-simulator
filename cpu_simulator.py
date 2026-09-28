class CPUSimulator:
    def __init__(self, instruction_memory, data_memory):
        self.pc = 0  # Program counter
        self.registers = [0] * 32  # 32 general-purpose registers
        self.instruction_memory = instruction_memory
        self.data_memory = data_memory

    def load_program(self, program):
        """Assembly programını yükler."""
        self.instruction_memory.load_instructions(program)

    def execute_instruction(self):
        if self.pc >= len(self.instruction_memory.memory):
            print("End of program.")
            return

        instruction = self.instruction_memory.memory[self.pc]
        self.pc += 1

        print(f"Executing instruction: {instruction}")

        # R-Format Instructions (example for add and sub)
        if instruction.startswith("add"):
            _, rd, rs, rt = instruction.split()
            rd, rs, rt = int(rd[1:]), int(rs[1:]), int(rt[1:])
            self.registers[rd] = self.registers[rs] + self.registers[rt]
        elif instruction.startswith("sub"):
            _, rd, rs, rt = instruction.split()
            rd, rs, rt = int(rd[1:]), int(rs[1:]), int(rt[1:])
            self.registers[rd] = self.registers[rs] - self.registers[rt]

        # I-Format Instructions (example for addi, lw, sw)
        elif instruction.startswith("addi"):
            _, rt, rs, imm = instruction.split()
            rt, rs, imm = int(rt[1:]), int(rs[1:]), int(imm)
            self.registers[rt] = self.registers[rs] + imm
        elif instruction.startswith("lw"):
            _, rt, address = instruction.split()
            rt, address = int(rt[1:]), int(address[:-1])
            self.registers[rt] = self.data_memory.read(address)
        elif instruction.startswith("sw"):
            _, rt, address = instruction.split()
            rt, address = int(rt[1:]), int(address[:-1])
            self.data_memory.write(address, self.registers[rt])

        # J-Format Instructions (example for j, jal, jr)
        elif instruction.startswith("j"):
            pass
        elif instruction.startswith("jal"):
            pass
        elif instruction.startswith("jr"):
            pass

    def __str__(self):
        return f"PC: {self.pc}\nRegisters: {self.registers}"

    def step(self):
        """Step-by-step execution."""
        self.execute_instruction()

    def run(self):
        """Run the program until the end."""
        while self.pc < len(self.instruction_memory.memory):
            self.execute_instruction()

    def display_registers(self):
        """Return the state of all registers."""
        return self.registers

    def display_memory(self):
        """Return the current state of data memory."""
        return self.data_memory.memory

    def display_program(self):
        """Return the assembly program and its machine code."""
        program = self.instruction_memory.memory
        machine_code = [self.convert_to_machine_code(instr) for instr in program]
        return program, machine_code

    def convert_to_machine_code(self, instruction):
        """Convert an instruction to machine code."""
        return hash(instruction) % 0xFFFFFFFF
