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

### Part 2: Veify that DFA accepts words

**Alphabet:** `{0, 1}`

- **Input:**  
  A file representing the DFA transition table.  

- **Input File Format for DFA:**
  - **Line 0:** The sequence of states separated by spaces.  
    Example: `A B C D E F`
  - **Line 1:** The initial state.  
  - **Line 2:** The final states, separated by spaces (if there is more than one final state).  
  - **Line 3 onwards:** Current state, character read, next state.  

  **Example of input:**
  ```mathematica
  a b c d e
  a
  a e
  a 0 b
  a 1 c
  b 0 d
  b 1 e
  c 1 e
  d 0 d
  e 1 e
  ```

- **Input File Format for Words:**
  - Each line contains one word composed of `{0,1}`'s.

  **Example of input:**
  ```mathematica
  0110010
  100110
  100110
  01011000
  0111111
  ```


## How to Run the Project

### Prerequisites
- Python 3.x
- Install necessary Python libraries if any (os, string)

### Steps
1. Clone this repository:
 ```bash
 git clone https://github.com/hyannsp/NFA-to-DFA-Translator
 ```
2. Navigate to the repository folder
 ```bash
 cd 'repository_name'
 ```
3. Run the main script with an NFA input file:
 ```bash
 python ./src/main.py
 ```
4. Select `1` to convert a nfa to dfa file, `2` to verify that words match or `0` to close application.
  - **Convert Files**
    1. When asked, provide the file path to a `.txt` format thats contain the *NFA* table
    2. When promped twice, specify the name for the new file (no need to add .txt).
    3. Your new file will be generated at `./output/dfa/your_file_name.txt`
  - **Words Verification**
    1. When asked, provide the file path to a `.txt` file that contains the *DFA* table.
    2. When prompted twice, provide the file path containing the *WORDS* in `.txt` format.
    3. Finally, provide the name for the output file containing the results (accepted/rejected words).
    4. It will be generated at `./output/words/yout_file_name.txt`