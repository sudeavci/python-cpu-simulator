# 💻 Python GUI CPU Simulator

[![Python Version](https://img.shields.io/badge/python-3.x-blue.svg)](https://www.python.org)
[![Interface](https://img.shields.io/badge/interface-GUI-brightgreen.svg)]()
[![Topic](https://img.shields.io/badge/concept-computer--architecture-orange.svg)]()

A lightweight, interactive CPU simulator written in Python that features a Graphical User Interface (GUI). This simulator visually models the execution of instructions, showing real-time state changes within instruction memory, data memory, registers, and control units.

---

### 🧠 Features & Simulation Architecture

The application visually breaks down the standard processor design components into distinct modules, simulating how binary configurations translate into register operations.

* **GUI Dashboard:** An interactive interface that visualizes register arrays, clock steps, and active execution pathways.
* **Instruction Memory Layout:** Simulates instruction caching and fetching mechanisms step-by-step.
* **Data Memory Management:** Models independent read/write cycles for dynamic memory simulation.

---

### 📁 Repository Structure

```text
ProjectSimulator/
│
├── cpu_simulator.json / .py # Core control logic and instruction parsing
├── data_memory.py           # Simulated RAM/Data storage mapping
├── instruction_memory.py    # Instruction fetch pipeline management
├── gui.py                   # Desktop visual layout and interactive panels
├── main.py                  # Simulator bootstrap entry point
└── .gitignore


🚀 Getting Started
Prerequisites
Python 3.8 or higher
Standard Python UI packages (Tkinter comes pre-installed with standard Python distributions)

How to Run
To boot up the graphical CPU dashboard, navigate to the project directory and run the master entry script:

Shell
python3 main.py
