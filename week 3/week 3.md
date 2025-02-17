# Week 3: Basic CPU Components

## Concept of ALU (Arithmetic Logic Unit)
The ALU (Arithmetic Logic Unit) is a critical component of a CPU, responsible for performing arithmetic and logical operations. Typically, it handles the following:

 1. **Arithmetic Operations:**  Such as addition (ADD), subtraction (SUB), multiplication (MUL), and division (DIV).
 2. **Logical Operations:** Such as AND, OR, NOT, and XOR.
 3. **Comparison:** Determines whether one number is equal to, less than, or greater than another.

## Implementing General-Purpose Registers (GPRs)
In a CPU, General-Purpose Registers (GPRs) are small, fast storage locations used to temporarily hold data during processing. These registers are crucial for efficient computation and serve as operands for the ALU.

#### **Design Goals for General-Purpose Registers:**
 - Store intermediate results and data.
 - Allow data to be read and written quickly.
 - Integrate with the ALU for operations.

### Explanation
3. **Arithmetic Operations:**
   - **ADD:** Adds two operands.
   - **SUB:** Subtracts the second operand from the first.
   - **MUL:** Multiplies two operands.
   - **DIV:** Divides the first operand by the second (integer division).
4. **Logical Operations:**
AND: Bitwise AND between operands.
OR: Bitwise OR between operands.
XOR: Bitwise XOR between operands.
NOT: Bitwise NOT of the operand.
5. **Comparison (CMP):**
For comparing two operands:

EQUAL: Returns if the two operands are equal.
LESS: Returns if the first operand is less than the second.
GREATER: Returns if the first operand is greater than the second.

6. **Error Handling:**
Raises an error if an invalid operation is passed or if division by zero occurs.


