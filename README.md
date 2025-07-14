# Mini C++ Syntax Validator

This is a simple **syntax validator** for a subset of C++ written in **Python** using **PLY** (Python Lex-Yacc).  
It demonstrates core compiler theory concepts like tokenization, context-free grammars (CFG), and parsing.
> 🏫 **Note:** This project was developed as part of the *Automata Formal Languages and Logic(UE23CS242A)* course at **PES University**.
---

## 📌 What it Does

- Defines a **Context-Free Grammar (CFG)** covering:
  - Basic declarations (`int`, `float`, `char`)
  - Assignments and expressions
  - `if`, `while`, and `for` control structures
- Uses **PLY** to build a lexer and parser for this mini language.
- Provides a **CLI** to input C++-like code and check if the syntax is valid.
- Handles syntax errors with custom messages.

---

## 🛠️ Tech Stack

- **Language:** Python 3
- **Libraries:** PLY (`lex` and `yacc`)

---

## ⚙️ How to Run
```bash
1️⃣ Clone the repo

git clone https://github.com/YourUsername/mini-cpp-syntax-validator.git
cd mini-cpp-syntax-validator

2️⃣ Install dependencies
pip install ply

3️⃣ Run the parser
python main.py

4️⃣ Input your C++-like code
Type your code line by line.
Type END on a new line to run the syntax check.
Type exit to quit the program.

