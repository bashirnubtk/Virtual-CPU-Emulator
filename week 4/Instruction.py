# Memory for instructions and data
memory = [
    {"op": "LOAD", "reg": 0, "val": 10},   # LOAD 10 into R0
    {"op": "LOAD", "reg": 1, "val": 5},    # LOAD 5 into R1
    {"op": "ADD", "reg": 0, "val": 5},     # R0 = R0 + R1 (using constant for simplicity)
    {"op": "LOAD", "reg": 1, "val": 2},    # LOAD 2 into R1
    {"op": "MUL", "reg": 0, "val": 2},     # R0 = R0 * R1 (using constant for simplicity)
    {"op": "STORE", "reg": 0, "addr": 0}   # STORE R0 in memory[0]
]

# Registers and RAM
registers = [0] * 4  # Four general-purpose registers
ram = [0] * 16       # Simulated RAM with 16 addresses


def fetch_instruction(memory, pc):
    """Fetches the next instruction from memory based on the program counter."""
    if pc < len(memory):
        return memory[pc]
    return None  # No instruction to fetch


def alu(op, reg_val, operand):
    """Performs basic ALU operations."""
    if op == "ADD":
        return reg_val + operand
    elif op == "SUB":
        return reg_val - operand
    elif op == "MUL":
        return reg_val * operand
    elif op == "DIV":
        return reg_val // operand if operand != 0 else 0
    else:
        raise ValueError(f"Unsupported ALU operation: {op}")


def execute_program(memory):
    """Executes instructions from memory in the fetch-decode-execute cycle."""
    pc = 0  # Program counter
    while pc < len(memory):
        instruction = fetch_instruction(memory, pc)
        if not instruction:
            break

        op = instruction["op"]
        reg = instruction.get("reg", None)
        val = instruction.get("val", None)
        addr = instruction.get("addr", None)

        if op == "LOAD":
            registers[reg] = val
        elif op in {"ADD", "SUB", "MUL", "DIV"}:
            registers[reg] = alu(op, registers[reg], val)
        elif op == "STORE":
            ram[addr] = registers[reg]
        else:
            raise ValueError(f"Unknown instruction: {op}")

        pc += 1


if __name__ == "__main__":
    # Execute the program
    execute_program(memory)

    # Display the final state of RAM and registers
    print("Final Registers:", registers)
    print("RAM:", ram)

