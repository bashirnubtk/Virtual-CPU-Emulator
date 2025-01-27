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


## Week 8 Features Were Integrated

###  Week 6

- **Memory Management:** The IVT was integrated into the memory structure. Reserved memory addresses were allocated for storing interrupt routines.
- **Instruction Execution:** Extended the `decode_execute` function to handle new instructions like `INT`, `READ_PORT`, and `WRITE_PORT`.

###  Week 7

- **Stack Management:** Enhanced stack handling for interrupt routines, ensuring the CPU state is saved and restored properly.
- **Branching and Subroutine Calls:** Incorporated priority switching logic to allow task preemption using the `INT` instruction.


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

