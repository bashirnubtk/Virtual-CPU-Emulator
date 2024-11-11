# Week 2: Instruction Set Architecture (ISA)
## Assembler Program Description

The Assembler Program is a tool designed to convert assembly code into machine code. It allows users to write assembly instructions, which are then translated into the binary code that a CPU can execute.

### ADD(Addition)
**Operations** : Adds the values of two registers or a register and a memory location, storing the result in a target register.

**Format** : ADD R1, R2 (Adds the contents of R2 to R1 and stores the result in R1). 

### SUB (Subtraction)

**Operation**:Subtracts the value of one register or memory location from another, storing the result in a target register.

**Format** : SUB R1, R2 (Subtracts the contents of R2 from R1 and stores the result in R1). 

### LOAD (Load Data into Register)

**Operation** :Loads data from memory into a register.

**Format**: LOAD R1, [100] (Loads the value from memory address 100 into register R1).

### STORE (Store Data from Register to Memory)

**Operation** :Stores data from a register into a specified memory location.

**Format** :STORE R1, [200] (Stores the value of R1 into memory address 200).


### CMP (Compare)

**Operation** :Compares the values of two registers or a register and memory, setting status flags (e.g., zero, carry) based on the result.

**Format** :CMP R1, R2 (Compares R1 to R2 and sets flags accordingly).

### MOV (Move Data)

**Operation** :Copies data from one register to another or from memory to a register.

**Format** :MOV R1, R2 (Copies the value in R2 into R1).

### INC (Increment)

**Operation** :Increments the value in a register by 1.

**Format** :INC R1 (Increments the value in R1 by 1).

### DEC (Decrement)

**Operation** :Decrements the value in a register by 1.

**Format** :DEC R1 (Decrements the value in R1 by 1).

### NOP (No Operation)

**Operation** :Does nothing and simply advances the program counter by one. Useful for timing or alignment.

**Format** :NOP (No effect, moves to the next instruction).

### Create a Simple Assembler:
#### How to Use This Assembler:

1. Write  assembly code in the format above.
2. Run the assembler script to convert it into binary machine code.
3. Feed the binary output to the virtual CPU emulator for execution.


