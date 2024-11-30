# Week 4: Instruction Execution
## Implementing the instruction fetching mechanism
**Instruction fetching:** The process of retrieving the next instruction from memory, based on the current value of the Program Counter (PC).
### Steps to Implement Instruction Fetching
1.**Use the Program Counter (PC):**
- The PC holds the address of the next instruction to be fetched from memory.

2.**Memory Initialization:**

- Think of memory as a list of instructions and data. The memory is preloaded with a program, where each instruction is represented by an opcode (number or identifier).

3.**Program Counter:**

- Start with a PC initialized to 0. This means the first instruction will be fetched from memory[0].

4.**Fetching Mechanism:**

- Access the memory at the current value of the PC.
Retrieve the instruction at that address.

5**Increment PC:**

- After fetching, add 1 to the PC (or more, depending on the instruction size). This prepares the PC to fetch the next instruction in the next cycle.

