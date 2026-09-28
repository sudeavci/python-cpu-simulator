import tkinter as tk
from tkinter import filedialog, messagebox
from cpu_simulator import CPUSimulator
from instruction_memory import InstructionMemory
from data_memory import DataMemory

class MIPS_GUI:
    def __init__(self, master):
        self.master = master
        self.master.title("MIPS Simulator")

        # Initialize simulator
        self.simulator = CPUSimulator(InstructionMemory(), DataMemory())

        self.setup_ui()

    def setup_ui(self):
        button_frame = tk.Frame(self.master)
        button_frame.grid(row=0, column=0, padx=5, pady=5)

        self.step_button = tk.Button(button_frame, text="Step", command=self.step)
        self.step_button.grid(row=0, column=0, padx=5)

        self.run_button = tk.Button(button_frame, text="Run", command=self.run)
        self.run_button.grid(row=0, column=1, padx=5)

        self.asm_frame = tk.Frame(self.master)
        self.asm_frame.grid(row=1, column=0, padx=5, pady=5)

        self.asm_label = tk.Label(self.asm_frame, text="Assembly Code:")
        self.asm_label.grid(row=0, column=0)

        self.asm_text = tk.Text(self.asm_frame, height=10, width=20)
        self.asm_text.grid(row=1, column=0)

        self.machine_code_frame = tk.Frame(self.master)
        self.machine_code_frame.grid(row=1, column=1, padx=5, pady=5)

        self.machine_code_label = tk.Label(self.machine_code_frame, text="Machine Code:")
        self.machine_code_label.grid(row=0, column=0)

        self.machine_code_text = tk.Text(self.machine_code_frame, height=10, width=20)
        self.machine_code_text.grid(row=1, column=0)

        self.register_frame = tk.Frame(self.master)
        self.register_frame.grid(row=1, column=2, padx=5, pady=5)

        self.registers_label = tk.Label(self.register_frame, text="Registers:")
        self.registers_label.grid(row=0, column=0)

        self.registers_text = tk.Text(self.register_frame, height=10, width=20)
        self.registers_text.grid(row=1, column=0)

        self.imem_label = tk.Label(self.master, text="Instruction Memory:")
        self.imem_label.grid(row=2, column=0, columnspan=3)

        self.imem_text = tk.Text(self.master, height=5, width=60)
        self.imem_text.grid(row=3, column=0, columnspan=3)

        self.dmem_label = tk.Label(self.master, text="Data Memory:")
        self.dmem_label.grid(row=4, column=0, columnspan=3)

        self.dmem_text = tk.Text(self.master, height=5, width=60)
        self.dmem_text.grid(row=5, column=0, columnspan=3)

        self.load_button = tk.Button(self.master, text="Load Program", command=self.load_program)
        self.load_button.grid(row=6, column=0, columnspan=3, pady=5)

        self.write_code_button = tk.Button(self.master, text="Write Code", command=self.write_code)
        self.write_code_button.grid(row=7, column=0, columnspan=3, pady=5)

    def load_program(self):
        """Open a file dialog for the user to select a file containing assembly code"""
        file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
        if file_path:
            with open(file_path, 'r') as file:
                program = file.readlines()
                program = [line.strip() for line in program]
                self.simulator.load_program(program)
                self.update_display()
        else:
            messagebox.showwarning("No File Selected", "Please select a file to load the program.")

    def write_code(self):
        """Allow the user to write code directly in a text field and load it into the simulator"""
        code = self.asm_text.get(1.0, tk.END).strip()
        if code:
            program = code.splitlines()
            self.simulator.load_program(program)
            self.update_display()
        else:
            messagebox.showwarning("No Code Entered", "Please enter some assembly code.")

    def step(self):
        try:
            self.simulator.step()
            self.update_display()
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def run(self):
        try:
            self.simulator.run()
            self.update_display()
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def update_display(self):
        self.registers_text.delete(1.0, tk.END)
        self.machine_code_text.delete(1.0, tk.END)
        self.asm_text.delete(1.0, tk.END)
        self.imem_text.delete(1.0, tk.END)
        self.dmem_text.delete(1.0, tk.END)

        registers = self.simulator.display_registers()
        for i, reg in enumerate(registers):
            self.registers_text.insert(tk.END, f"$r{i}: {reg}\n")

        memory = self.simulator.display_memory()
        for i, mem in enumerate(memory[:10]):
            self.dmem_text.insert(tk.END, f"Address {i}: {mem}\n")

        program, machine_code = self.simulator.display_program()
        for line in program:
            self.asm_text.insert(tk.END, f"{line}\n")
        for code in machine_code:
            self.machine_code_text.insert(tk.END, f"{hex(code)}\n")

        imem = self.simulator.instruction_memory.memory
        for i in range(min(10, len(imem))):
            try:
                instruction = int(imem[i], 16) if isinstance(imem[i], str) else imem[i]
                self.imem_text.insert(tk.END, f"Address {i}: {hex(instruction)}\n")
            except ValueError:
                self.imem_text.insert(tk.END, f"Address {i}: Invalid instruction\n")
