# Flask Calculator App

## Overview
This project turns an existing Python calculator package into a Flask web application with a frontend. Flask acts as the middleman, allowing users to interact with the calculator via a web interface.

## Project Structure
```
FlaskCalculator/
│── app.py                # Main Flask application
│── templates/
│   └── index.html        # Webpage for user interaction
│── app/                  # Existing calculator package
│   ├── __init__.py       # Package initializer
│   ├── main.py           # Calculator logic (unchanged!)
└── requirements.txt      # Required dependencies
```

## Installation & Setup

### 1️⃣ Install Dependencies
Ensure you have Python installed. Then, install the required packages:
```sh
pip install -r requirements.txt
```

### 2️⃣ Run the Flask App
```sh
python app.py
```
By default, the app will be available at:
```
http://127.0.0.1:5000/
```

## How It Works

### **1️⃣ Flask Application Setup (`app.py`)**
```python
from flask import Flask, render_template, request
from app import main  # Importing the calculator package

app = Flask(__name__)
```
- **Flask initializes the web app.**
- **Imports your existing calculator logic (`main.py`).**

---

### **2️⃣ Homepage Route (`@app.route('/')`)**
```python
@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    
    if request.method == "POST":
        num1 = float(request.form["num1"])
        num2 = float(request.form["num2"])
        operation = request.form["operation"]
        
        result = main.calculate(num1, num2, operation)  # Uses existing logic

    return render_template("index.html", result=result)
```
- **Handles user input (numbers & operation).**
- **Calls your existing calculator logic.**
- **Passes the result to the webpage.**

---

### **3️⃣ Rendering the Webpage**
```python
return render_template("index.html", result=result)
```
- Loads `index.html` and displays the calculated result.

---

### **4️⃣ Running the Flask App**
```python
if __name__ == "__main__":
    app.run(debug=True)
```
- Runs the app when `app.py` is executed.
- `debug=True` enables automatic reloading and error messages.

## How the Pieces Fit Together
| **Component**   | **Purpose**  |
|---------------|------------|
| `app.py`  | Handles web requests & calls the calculator package. |
| `main.py`  | Contains the actual calculator logic (unchanged). |
| `index.html`  | Displays the input form & result to the user. |

## Next Steps
- Customize the frontend (`index.html`).
- Add more operations to `main.py` if needed.
- Deploy the app to a cloud platform like AWS or Heroku.



