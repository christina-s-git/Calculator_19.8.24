# Evolution from CLI Calculator to Flask Web App

## Overview
This document explains the transformation of our **CLI-based calculator** into a **Flask web application**. The goal was to move from a simple command-line interface to a user-friendly web-based calculator while maintaining modularity and reusability.

---

## **1️⃣ Initial CLI-Based Calculator**

### **Structure of the CLI Project**
Originally, the calculator was a command-line application where users could manually input numbers and select an operation. It followed this structure:

```
calculator_19.08.24/
├── app/
│   ├── main.py            # Main script for the calculator
│   ├── ui.py              # Handles user input and output
│   └── operations/        # Contains arithmetic operation functions
│       ├── addition.py
│       ├── subtraction.py
│       ├── multiplication.py
│       └── division.py
├── requirements.txt       # Python dependencies
├── Dockerfile             # Docker configuration
└── README.md              # Project documentation
```

### **How it Worked**
- The `ui.py` file handled user input and displayed results.
- The `operations/` directory contained separate modules for each arithmetic function.
- The `main.py` file orchestrated the calculation by:
  1. Collecting user input (numbers and operation)
  2. Calling the relevant arithmetic function
  3. Printing the result

Example execution:
```bash
$ python main.py
Enter the first number: 10
Enter the second number: 5
Select operation (+, -, *, /): +
Result: 15.0
```

---

## **2️⃣ Transition to a Flask Web Application**

### **Why Move to Flask?**
- To provide a web-based user interface instead of a command-line interface.
- To separate logic from presentation using **Flask templates**.
- To prepare the project for deployment as a web service.

### **Key Changes in Structure**

```
FlaskCalculatorDocker_19.8.24/
├── app/
│   ├── app.py                # Flask application entry point
│   ├── templates/
│   │   ├── index.html        # Web UI
│   ├── static/               # CSS/JavaScript files (if needed)
│   ├── calculator/
│   │   ├── __init__.py
│   │   ├── main.py           # Core calculator logic
│   │   ├── operations/
│   │   │   ├── __init__.py
│   │   │   ├── addition.py
│   │   │   ├── subtraction.py
│   │   │   ├── multiplication.py
│   │   │   ├── division.py
├── Dockerfile                # Docker configuration
├── requirements.txt          # Dependencies
└── README.md                 # Documentation
```

---

## **3️⃣ Changes & Key Adjustments**

### **1. Replacing CLI Input with Web Forms**
Instead of `ui.get_input()`, the Flask app now:
- Uses an HTML form (`index.html`) to collect numbers and operations.
- Sends form data to the backend via a `POST` request.

```python
num1 = float(request.form["num1"])
num2 = float(request.form["num2"])
operation = request.form["operation"]
```

### **2. Flask Routing & Handling Requests**
We defined a route (`/calculate`) to handle form submissions.

```python
@app.route("/calculate", methods=["POST"])
def calculate():
    num1 = float(request.form["num1"])
    num2 = float(request.form["num2"])
    operation = request.form["operation"]
    result = main.calculate(num1, num2, operation)
    return render_template("index.html", result=result)
```

### **3. Adapting the Main Logic**
- `main.py` remains mostly unchanged except for the removal of CLI-specific code.
- The function `calculate(x, y, operation)` is reused.

```python
def calculate(x, y, operation):
    if operation == "+":
        return operations.addition.add(x, y)
    elif operation == "-":
        return operations.subtraction.subtract(x, y)
    elif operation == "*":
        return operations.multiplication.multiply(x, y)
    elif operation == "/":
        return operations.division.divide(x, y)
    return "Invalid operation"
```

### **4. Adding a Frontend (index.html)**
The new web UI replaces CLI prompts:

```html
<form action="/calculate" method="post">
    <input type="text" name="num1" required>
    <select name="operation">
        <option value="+">+</option>
        <option value="-">-</option>
        <option value="*">×</option>
        <option value="/">÷</option>
    </select>
    <input type="text" name="num2" required>
    <button type="submit">Calculate</button>
</form>
<p>Result: {{ result }}</p>
```

---

## **4️⃣ Adding Docker Support**

A `Dockerfile` was added to allow easy deployment:

```Dockerfile
FROM python:3.9-slim
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
CMD ["python", "app.py"]
```

### **Running with Docker**
```sh
docker build -t flask-calculator .
docker run -p 5000:5000 flask-calculator
```

Now, the app runs in a browser at `http://127.0.0.1:5000/` 🎉

---

## **Summary of the Transition**

| Feature              | CLI Version | Flask Version |
|----------------------|------------|--------------|
| Input Handling      | CLI prompts | Web form (HTML) |
| Processing Logic    | `main.py` calls `ui.py` | `app.py` calls `main.py` |
| Output Display      | Printed in terminal | Displayed in browser |
| Modularity         | Functions for each operation | Functions reused in Flask |
| Deployment Method  | Run with Python | Run with Docker |

By making these changes, we transformed the CLI calculator into a **scalable**, **user-friendly**, and **web-ready** application! 🚀

