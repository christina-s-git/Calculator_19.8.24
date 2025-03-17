# Flask Calculator: How It Works

## 📌 Overview
This Flask-based calculator application takes user input from an HTML form, processes the calculation using a separate Python module (`main.py`), and returns the result back to the user. This document explains how `app.py` and `main.py` work together.

---

## 🔗 How `app.py` and `main.py` Work Together
```
USER INPUT (HTML Form)
     ⬇
Flask receives form data (app.py)
     ⬇
num1 = float(request.form["num1"])  -->  x
num2 = float(request.form["num2"])  -->  y
operation = request.form["operation"]  -->  operation
     ⬇
Pass values to main.py's calculate function:
calculate(num1, num2, operation)
     ⬇
main.py processes the calculation:
def calculate(x, y, operation):
     ⬇
Returns result back to Flask (app.py)
     ⬇
Flask sends result to HTML page
```

---

## 🔗 Code Mapping Example
| `app.py` (Flask) | `main.py` (Logic) |
|------------------|------------------|
| `num1 = float(request.form["num1"])` | `def calculate(x, y, operation):` |
| `num2 = float(request.form["num2"])` | `return x + y  # (or other operations)` |
| `operation = request.form["operation"]` | (Operation stays the same) |
| `result = calculate(num1, num2, operation)` | `calculate(x, y, operation)` |

---

## 🚀 Summary
- **Flask (`app.py`)** handles user input, calls `calculate` from `main.py`, and displays the result.
- **`main.py`** contains the logic to perform calculations and returns the result to Flask.
- **HTML Form** collects input and sends it to Flask.

This shows how data flows from the user input → Flask → main.py → back to Flask → displayed to user.

This separation of concerns makes the app modular, allowing the core logic (`main.py`) to be reused in different applications.



