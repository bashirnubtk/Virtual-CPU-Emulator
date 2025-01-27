# Week 8: Advanced Virtual CPU Features

## Introduction

In Week 8, we focus on further extending the functionality of our virtual CPU simulator by integrating advanced features while ensuring compatibility with the work from previous weeks. This document outlines the tasks accomplished, the new features added, and how everything was merged seamlessly with the existing functionality from earlier weeks.

---

## Objectives

- Introduce **interrupt handling** and **priority-based task management**.
- Implement an **I/O simulation system** for handling basic input/output operations.
- Enhance **debugging support** with error reporting and program trace logging.
- Ensure backward compatibility with features developed in Weeks 6 and 7.

---

## Features Added

### 1. Interrupt Handling

Interrupts allow the CPU to temporarily halt the current task, execute a higher-priority task, and then resume. This feature introduces:

- **Interrupt Vector Table (IVT):** A reserved memory section for storing interrupt routines.
- **Interrupt Service Routines (ISR):** Functions that handle specific interrupts.
- **Software Interrupts:** Triggered by specific instructions (e.g., `INT`).

### 2. Priority-Based Task Management

We implemented a basic priority queue for managing tasks. Tasks are prioritized as:

- **High Priority**: Executed immediately, interrupting lower-priority tasks.
- **Normal Priority**: Executes in standard order.
- **Low Priority**: Deferred until no higher-priority tasks remain.

### 3. I/O Simulation System

To simulate real-world CPU I/O operations, we added:

- **I/O Ports:** Simulated ports for sending and receiving data.
- **READ\_PORT and WRITE\_PORT Instructions:** New instructions to interact with the ports.
- **Sample I/O Devices:** A virtual keyboard and display.

### 4. Debugging and Trace Logging

To assist with debugging and analysis, we added:

- **Error Detection and Reporting:** Detects and logs invalid memory access, stack overflows, etc.
- **Instruction Trace Logs:** Tracks all executed instructions for post-execution review.

---

## Instruction Set Updates

| Instruction  | Opcode | Description                             |
| ------------ | ------ | --------------------------------------- |
| `INT`        | `1001` | Triggers an interrupt routine from IVT. |
| `READ_PORT`  | `1010` | Reads data from an I/O port.            |
| `WRITE_PORT` | `1011` | Writes data to an I/O port.             |

---

## How Week 8 Features Were Integrated

### Merging with Week 6

- **Memory Management:** The IVT was integrated into the memory structure. Reserved memory addresses were allocated for storing interrupt routines.
- **Instruction Execution:** Extended the `decode_execute` function to handle new instructions like `INT`, `READ_PORT`, and `WRITE_PORT`.

### Merging with Week 7

- **Stack Management:** Enhanced stack handling for interrupt routines, ensuring the CPU state is saved and restored properly.
- **Branching and Subroutine Calls:** Incorporated priority switching logic to allow task preemption using the `INT` instruction.

---

## Example Program

The following program demonstrates the new features:

```plaintext
0001000100000010  # LOAD R1, 2
1011000000000001  # WRITE_PORT 1
1010000000000001  # READ_PORT 1
1001000000000001  # INT 1 (Interrupt Service Routine 1)
1111000000000000  # HALT
```

---

## Testing

- **Unit Testing:** All individual features were tested using predefined test cases.
- **Integration Testing:** Ensured compatibility between Weeks 6, 7, and 8 functionalities.
- **Debugging Tools:** Verified trace logs for correctness.

---

## Challenges

- **Backward Compatibility:** Adjusting existing code to accommodate new instructions while preserving old functionality.
- **Interrupt Priority:** Ensuring correct priority-based task switching without corrupting the program state.

---

## Conclusion

Week 8 significantly enhances the virtual CPU by introducing advanced features like interrupt handling, priority-based task management, and I/O simulation. These additions not only make the CPU more realistic but also prepare it for more complex operations in future iterations.

---

## Next Steps

- Implement multi-threading capabilities for concurrent task execution.
- Introduce advanced debugging tools like step-by-step execution.
- Optimize the CPU for better performance with larger programs.

