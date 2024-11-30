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

5.**Increment PC:**

- After fetching, add 1 to the PC (or more, depending on the instruction size). This prepares the PC to fetch the next instruction in the next cycle.
---

### Core Concepts

1. **Instruction Decoding**:
   - Decoding means interpreting the fetched instruction to determine what operation to perform and what data to operate on.
   - Each instruction has an **opcode** (defines the operation) and optionally operands (define the data).

2. **Execution**:
   - Execution involves using the ALU for operations like addition, subtraction, and logical operations.
   - Registers store the results or intermediate values during execution.

3. **ALU Role**:
   - The ALU handles arithmetic (`ADD`, `SUB`) and logical (`AND`, `OR`) operations.
   - Operands for the ALU come from the registers or memory.

---

### Components of the Process

#### 1. **Registers**
Registers store intermediate data and results of ALU operations.

- **General Registers** (`R1`, `R2`): Used for operands.
- **Accumulator (`ACC`)**: Stores ALU results.
- **Program Counter (`PC`)**: Points to the current instruction.
- **Flags (`FLAGS`)**: Indicates status (e.g., Zero result).

#### 2. **ALU**
The ALU performs operations based on the instruction's opcode.

---

### Steps to Decode and Execute Instructions

1. **Fetch the Instruction**:
   - The fetched instruction includes an opcode and optional operands.

2. **Decode the Opcode**:
   - Determine the operation type (e.g., `ADD`, `SUB`).

3. **Access Operands**:
   - Retrieve operands from registers or memory.

4. **Perform the Operation**:
   - Use the ALU to execute the operation.

5. **Update Registers**:
   - Store the result in the appropriate register (e.g., `ACC`).

---

### Example Instruction Execution Workflow

#### Instruction: `ADD R1, R2`  
**Meaning**: Add the values of registers `R1` and `R2` and store the result in the accumulator (`ACC`).

1. **Fetch**:
   - The PC points to the instruction in memory: `[ADD, R1, R2]`.

2. **Decode**:
   - Opcode is `ADD`.
   - Operands are `R1` and `R2`.

3. **Execute**:
   - Retrieve values of `R1` and `R2`.
   - Perform `R1 + R2` using the ALU.

4. **Update Registers**:
   - Store the result in `ACC`.
   - Update flags (e.g., set Zero flag if the result is 0).

