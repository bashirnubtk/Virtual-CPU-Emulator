class CPURegisters:
    def __init__(self, memory_size=256):
       
        self.program_counter = 0  # Start at address 0
        self.instruction_register = None  # Holds the current instruction
        self.memory_size = memory_size  # Simulate memory size

    def fetch_instruction(self, memory):
       
        if not (0 <= self.program_counter < self.memory_size):
            raise IndexError("Program Counter out of memory bounds.")
        
        instruction = memory[self.program_counter]
        self.instruction_register = instruction
        self.program_counter += 1  # Increment PC for the next instruction
        return instruction

    def display_registers(self):
        """
        Display the 
        """
        print(f"Program Counter (PC): {self.program_counter}")
        print(f"Instruction Register (IR): {self.instruction_register}")

if __name__ == "__main__":
   
    memory = [
        "00010001",  
        "00100010",  
        "00110100",  
        "11110000",  
    ]
    
    cpu = CPURegisters(memory_size=len(memory))

    # Simulate fetching instructions
    try:
        while cpu.program_counter < len(memory):
            print(f"Fetched Instruction: {cpu.fetch_instruction(memory)}")
            cpu.display_registers()
    except IndexError as e:
        print(f"Error: {e}")
