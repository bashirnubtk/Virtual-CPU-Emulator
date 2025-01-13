# Instruction Set
INSTRUCTION_SET = {
    'LOAD': '0001',
    'STORE': '0010',
    'ADD': '0011',
    'SUB': '0100',
    'JMP': '0101',
    'HALT': '1111'
}

# Register Set (4 registers, R0-R3)
REGISTER_SET = {
    'R0': '00',
    'R1': '01',
    'R2': '10',
    'R3': '11'
}

# CPU Components
class VirtualCPU:
    def __init__(self):
        self.registers = {'R0': 0, 'R1': 0, 'R2': 0, 'R3': 0}  # General-purpose registers
        self.program_counter = 0  # Program Counter
        self.instruction_register = None  # Instruction Register
        self.memory = [0] * 256  # Simulated memory (256 bytes)

    # Arithmetic Logic Unit (ALU)
    def alu(self, operation, operand1, operand2):
        if operation == 'ADD':
            return operand1 + operand2
        elif operation == 'SUB':
            return operand1 - operand2
        else:
            raise ValueError(f"Unsupported ALU operation: {operation}")

    # Execute a single instruction
    def execute_instruction(self, binary_instruction):
        opcode = binary_instruction[:4]
        if opcode == INSTRUCTION_SET['LOAD']:
            reg = list(REGISTER_SET.keys())[int(binary_instruction[4:6], 2)]
            addr = int(binary_instruction[6:], 2)
            self.registers[reg] = self.memory[addr]
        elif opcode == INSTRUCTION_SET['STORE']:
            reg = list(REGISTER_SET.keys())[int(binary_instruction[4:6], 2)]
            addr = int(binary_instruction[6:], 2)
            self.memory[addr] = self.registers[reg]
        elif opcode == INSTRUCTION_SET['ADD']:
            reg1 = list(REGISTER_SET.keys())[int(binary_instruction[4:6], 2)]
            reg2 = list(REGISTER_SET.keys())[int(binary_instruction[6:8], 2)]
            self.registers[reg1] = self.alu('ADD', self.registers[reg1], self.registers[reg2])
        elif opcode == INSTRUCTION_SET['SUB']:
            reg1 = list(REGISTER_SET.keys())[int(binary_instruction[4:6], 2)]
            reg2 = list(REGISTER_SET.keys())[int(binary_instruction[6:8], 2)]
            self.registers[reg1] = self.alu('SUB', self.registers[reg1], self.registers[reg2])
        elif opcode == INSTRUCTION_SET['JMP']:
            addr = int(binary_instruction[4:], 2)
            self.program_counter = addr
        elif opcode == INSTRUCTION_SET['HALT']:
            return False
        return True

    # Run a program
    def run_program(self, program):
        self.program_counter = 0
        while self.program_counter < len(program):
            self.instruction_register = program[self.program_counter]
            if not self.execute_instruction(self.instruction_register):
                break
            self.program_counter += 1

# Assembler functions remain unchanged
def assemble_instruction(line):
    parts = line.strip().replace(",", "").split()
    opcode = parts[0].upper()
    if opcode not in INSTRUCTION_SET:
        raise ValueError(f"Invalid instruction: {opcode}")

    binary_code = INSTRUCTION_SET[opcode]
    if opcode in ['LOAD', 'STORE']:
        reg = REGISTER_SET[parts[1]]
        addr = format(int(parts[2]), '08b')
        binary_code += reg + addr
    elif opcode in ['ADD', 'SUB']:
        reg1 = REGISTER_SET[parts[1]]
        reg2 = REGISTER_SET[parts[2]]
        binary_code += reg1 + reg2 + '0000'
    elif opcode == 'JMP':
        addr = format(int(parts[1]), '08b')
        binary_code += addr
    elif opcode == 'HALT':
        binary_code += '00000000'
    return binary_code

def assemble_program(assembly_code):
    machine_code = []
    for line in assembly_code:
        if line.strip() and not line.startswith(';'):
            machine_code.append(assemble_instruction(line))
    return machine_code

# Example usage
assembly_code = [
    "LOAD R1, 10",
    "ADD R1, R2",
    "STORE R1, 100",
    "JMP 200",
    "HALT"
]

cpu = VirtualCPU()
machine_code = assemble_program(assembly_code)
cpu.run_program(machine_code)
