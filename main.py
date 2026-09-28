import tkinter as tk
from gui import MIPS_GUI  # Buradaki sınıf adı, gui.py'ye uygun olarak MIPS_GUI olmalı
from instruction_memory import InstructionMemory
from data_memory import DataMemory

def main():
    root = tk.Tk()

    # Sample program (assembly instructions)
    instructions = [
        "addi $t0, $zero, 5",  # $t0 = 5
        "addi $t1, $zero, 5",  # $t1 = 5
        "add $t2, $t0, $t1"    # $t2 = $t0 + $t1
    ]

    # Load instructions into instruction memory
    instruction_memory = InstructionMemory()
    instruction_memory.load_instructions(instructions)

    # Create the GUI and pass the instruction memory, data memory, and CPU simulator
    simulator_gui = MIPS_GUI(root)

    # Set instruction and data memories
    simulator_gui.instruction_memory = instruction_memory
    simulator_gui.data_memory = DataMemory()

    # Start the main loop
    root.mainloop()

if __name__ == "__main__":
    main()


