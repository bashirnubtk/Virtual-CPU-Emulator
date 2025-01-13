# Week 5: CPU and Memory Management Classes
class Memory:
    def __init__(self, size):
        self.data = [0] * size

    def read(self, address):
        return self.data[address]

    def write(self, address, value):
        self.data[address] = value

    def display(self, start, end):
        for i in range(start, end):
            print(f"Address {i:04X}: {self.data[i]:04X}")


class Registers:
    def __init__(self):
        self.general_purpose = [0] * 4  # Four general-purpose registers (R0-R3)
        self.pc = 0  # Program Counter
        self.ir = 0  # Instruction Register

    def __str__(self):
        gp_regs = ', '.join(f'R{i}: {val}' for i, val in enumerate(self.general_purpose))
        return f"{gp_regs}, PC: {self.pc}, IR: {self.ir}"


class CPU:
    def __init__(self, memory_size):
        self.memory = Memory(memory_size)
        self.registers = Registers()
        self.instruction_set = {
            0x1: self.instruction_load,
            0x2: self.instruction_store,
            0x3: self.instruction_add,
            0x4: self.instruction_sub,
            0xF: self.instruction_halt
        }
        self.halted = False

    def load_program(self, program):
        for address, instruction in enumerate(program):
            self.memory.write(address, instruction)

    def fetch(self):
        address = self.registers.pc
        self.registers.ir = self.memory.read(address)
        self.registers.pc += 1

    def decode_execute(self):
        instruction = self.registers.ir
        opcode = (instruction & 0xF000) >> 12
        reg1 = (instruction & 0x0F00) >> 8
        reg2 = (instruction & 0x00F0) >> 4
        addr = instruction & 0x00FF

        if opcode in self.instruction_set:
            self.instruction_set[opcode](reg1, reg2, addr)
        else:
            raise ValueError(f"Unknown opcode: {opcode:X}")

    def run(self):
        while not self.halted:
            self.fetch()
            self.decode_execute()

    # Week 5: Implement Core Instructions
    def instruction_load(self, reg1, _, addr):
        self.registers.general_purpose[reg1] = self.memory.read(addr)

    def instruction_store(self, reg1, _, addr):
        self.memory.write(addr, self.registers.general_purpose[reg1])

    def instruction_add(self, reg1, reg2, _):
        self.registers.general_purpose[reg1] += self.registers.general_purpose[reg2]

    def instruction_sub(self, reg1, reg2, _):
        self.registers.general_purpose[reg1] -= self.registers.general_purpose[reg2]

    def instruction_halt(self, *args):
        self.halted = True


# Week 6: Input/Output Operations
class IODevices:
    def __init__(self):
        self.keyboard_buffer = ""
        self.display_buffer = []

    def keyboard_input(self, input_string):
        self.keyboard_buffer = input_string

    def read_keyboard(self):
        if self.keyboard_buffer:
            char = self.keyboard_buffer[0]
            self.keyboard_buffer = self.keyboard_buffer[1:]
            return ord(char)
        return 0

    def write_display(self, value):
        self.display_buffer.append(chr(value))

    def show_display(self):
        print("Display Output:", ''.join(self.display_buffer))


class CPUWithIO(CPU):
    def __init__(self, memory_size):
        super().__init__(memory_size)
        self.io = IODevices()
        self.instruction_set.update({
            0x5: self.instruction_in,
            0x6: self.instruction_out
        })

    def instruction_in(self, reg1, *_):
        value = self.io.read_keyboard()
        self.registers.general_purpose[reg1] = value

    def instruction_out(self, reg1, *_):
        value = self.registers.general_purpose[reg1]
        self.io.write_display(value)


# Example Usage
if __name__ == "__main__":
    # Initialize CPU with Memory and I/O
    cpu = CPUWithIO(memory_size=256)

    # Example program
    program = [
        0x110A,  # LOAD R1, 10
        0x3201,  # ADD R2, R1
        0x210A,  # STORE R1, 10
        0x5000,  # IN R0
        0x6000,  # OUT R0
        0xF000   # HALT
    ]

    # Load program into memory
    cpu.load_program(program)

    # Simulate keyboard input
    cpu.io.keyboard_input("A")  # User types "A"

    # Run the CPU
    print("Initial State:", cpu.registers)
    cpu.run()
    print("Final State:", cpu.registers)

    # Show the display output
    cpu.io.show_display()
    print("\nMemory Snapshot:")
    cpu.memory.display(0, 16)
