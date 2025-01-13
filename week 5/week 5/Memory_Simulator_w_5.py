# Instruction Fetch-Decode-Execute with Memory Management

# Week 5: Memory Management
# Simulated Memory Management
class Memory:
    def __init__(self, size):
        self.size = size  # Total memory size
        self.memory = [0] * size  # Initialize memory with zeroes

    def read(self, address):
        if address < 0 or address >= self.size:
            raise ValueError(f"Invalid memory address: {address}")
        return self.memory[address]

    def write(self, address, value):
        if address < 0 or address >= self.size:
            raise ValueError(f"Invalid memory address: {address}")
        if value < 0 or value > 255:  # Assuming 8-bit memory cells
            raise ValueError(f"Invalid value: {value}. Must be between 0 and 255.")
        self.memory[address] = value

    def display(self, start=0, end=16):
        if end > self.size:
            end = self.size
        for i in range(start, end):
            print(f"Address {i:03}: {self.memory[i]:08b}")


# Week 4: Register Definitions
class Registers:
    def __init__(self):
        self.general_purpose = [0] * 4  # 4 general-purpose registers (R0-R3)
        self.pc = 0  # Program Counter
        self.ir = None  # Instruction Register

    def __repr__(self):
        return f"Registers(R0={self.general_purpose[0]}, R1={self.general_purpose[1]}, R2={self.general_purpose[2]}, R3={self.general_purpose[3]}, PC={self.pc})"


# Week 4: Instruction Execution
class CPU:
    def __init__(self, memory_size):
        # Week 5: Adding Memory Management
        self.memory = Memory(memory_size)
        self.registers = Registers()
        self.instruction_set = {
            'LOAD': self.instruction_load,
            'STORE': self.instruction_store,
            'ADD': self.instruction_add,
            'SUB': self.instruction_sub,
            'HALT': self.instruction_halt,
        }
        self.halted = False

    # Week 4: Instruction Fetch
    def fetch(self):
        # Fetch the instruction from memory
        address = self.registers.pc
        instruction = self.memory.read(address)
        self.registers.ir = instruction
        self.registers.pc += 1  # Increment PC for next instruction
        return instruction

    # Week 4: Decode and Execute Instructions
    def decode_and_execute(self, instruction):
        # Decode and execute the instruction
        opcode = instruction >> 12  # Extract the first 4 bits (opcode)
        reg1 = (instruction >> 8) & 0xF  # Next 4 bits (register 1)
        reg2 = (instruction >> 4) & 0xF  # Next 4 bits (register 2)
        operand = instruction & 0xFF  # Last 8 bits (operand)

        # Map opcode to instruction
        for key, func in self.instruction_set.items():
            if opcode == self.instruction_to_opcode(key):
                func(reg1, reg2, operand)
                return
        raise ValueError(f"Invalid opcode: {opcode}")

    # Week 4: Instruction to Opcode Mapping
    def instruction_to_opcode(self, name):
        mapping = {'LOAD': 1, 'STORE': 2, 'ADD': 3, 'SUB': 4, 'HALT': 15}
        return mapping.get(name, None)

    # Week 4: Define Instruction Implementations
    def instruction_load(self, reg1, _, address):
        value = self.memory.read(address)
        self.registers.general_purpose[reg1] = value

    def instruction_store(self, reg1, _, address):
        value = self.registers.general_purpose[reg1]
        self.memory.write(address, value)

    def instruction_add(self, reg1, reg2, _):
        self.registers.general_purpose[reg1] += self.registers.general_purpose[reg2]

    def instruction_sub(self, reg1, reg2, _):
        self.registers.general_purpose[reg1] -= self.registers.general_purpose[reg2]

    def instruction_halt(self, *args):
        self.halted = True

    # Week 4: Run Instructions
    def run(self):
        while not self.halted:
            instruction = self.fetch()
            self.decode_and_execute(instruction)

    # Week 5: Load Program into Memory
    def load_program(self, program):
        for i, instruction in enumerate(program):
            self.memory.write(i, instruction)


# Example Usage
if __name__ == "__main__":
    # Week 5: Initialize CPU with Memory
    cpu = CPU(memory_size=256)

    # Example program (binary representation of instructions)
    program = [
        0x110A,  # LOAD R1, 10
        0x3201,  # ADD R2, R1
        0x210A,  # STORE R1, 10
        0xF000   # HALT
    ]

    # Week 5: Load program into memory
    cpu.load_program(program)

    # Week 4: Run the CPU
    print("Initial State:", cpu.registers)
    cpu.run()
    print("Final State:", cpu.registers)
    print("\nMemory Snapshot:")
    cpu.memory.display(0, 16)
