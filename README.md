
# Sripathirao Karri's Interactive Python Calculator

## 🧮 Overview

This is a command-line based interactive calculator developed using Python. It uses **OOP principles** with classes and **custom exception handling** to perform a variety of arithmetic operations. Users can select from a menu of operations and input values to get real-time results.

This calculator supports:

* Addition
* Subtraction
* Multiplication
* Division
* Modulo
* Exponentiation
* Floor Division

All interactions happen via the terminal, making it a great example for learning basic Python concepts such as:

* Classes and objects
* Exception handling
* User input and control flow

---

## 🚀 Features

* Intuitive user interface via terminal
* Graceful error handling (e.g., division by zero, invalid inputs)
* Re-prompts user for valid inputs in case of errors
* Modular and object-oriented design
* Easy to extend with new operations

---

## 📋 Requirements

* Python 3.x

No additional libraries or frameworks are required.

---

## 📂 File Structure

```
calculator.py        # Main interactive calculator script
README.md            # Documentation file
```

---

## 🛠️ How to Use

1. **Run the script**:

   ```bash
   python calculator.py
   ```

2. **Follow the menu** displayed in the terminal:

   ```
   -- Calculator Menu ---
   1 Addition
   2 Subtraction
   3 Product
   4 Division
   5 Modulo
   6 Power
   7 Floor Division
   8 Exit
   ```

3. **Input your choice** (1-8), then enter two numeric values when prompted.

4. **Get the result**, or error messages if the input is invalid (like dividing by zero or entering non-numeric values).

---

## ⚠️ Known Issues / Bugs

* The constructor in the class is defined as `_init_` instead of Python's standard `__init__`. This causes the object not to initialize variables `a` and `b` properly.

  ✅ **Fix**:
  Change:

  ```python
  def _init_(self):
  ```

  to:

  ```python
  def __init__(self):
  ```

* The `floor_division()` method currently uses regular division (`/`) instead of floor division (`//`).

  ✅ **Fix**:
  Change:

  ```python
  return self.a/self.b
  ```

  to:

  ```python
  return self.a // self.b
  ```

---

## 👨‍💻 Author

**Sripathirao Karri**

---


