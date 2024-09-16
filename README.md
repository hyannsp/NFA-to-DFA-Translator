# NFA to DFA Translator

This project aims to convert a Non-deterministic Finite Automaton (NFA) with epsilon (empty) transitions into a Deterministic Finite Automaton (DFA). It also checks if a set of words is recognized by the generated DFA.

## Project Objectives

### Part 1: NFA to DFA Conversion

**Alphabet:** `{0, 1}`

- **Input:**  
  A file representing the NFA transition table.

- **Input File Format:**
  - **Line 0:** The sequence of states separated by spaces.  
    Example: `A B C D E F`
  - **Line 1:** The initial state.
  - **Line 2:** The final states, separated by spaces (if there is more than one final state).
  - **Line 3 onwards:** Current state, character read, next state.  
    Use `h` to represent an epsilon (empty) transition.
  
  **Example of input:**
  ```mathematica
  A B C D E F
  A
  F
  A 0 B
  A 1 C
  A h D
  B 1 D
  C 0 E
  D h F
  E 1 F
  ```


- **Output:**  
A file representing the DFA transition table in the same format as the input file.

- **Visualization:**  
- Use **GraphViz** to display the NFA and DFA as graphs.
- Use **JFLAP** to draw the input and output automata for visual comparison.


## How to Run the Project

### Prerequisites
- Python 3.x
- Install necessary Python libraries if any (list them if needed)
- GraphViz installed for graph generation (optional but recommended for visualization)

### Steps
1. Clone this repository:
 ```bash
 git clone https://github.com/hyannsp/NFA-to-DFA-Translator
 ```
2. Navigate to **src** folder
 ```bash
 cd src
 ```
3. Run the main script with an NFA input file:
 ```bash
 python main.py
 ```
4. Provide the path to your NFA text file when prompted.