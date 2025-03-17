# Flask Calculator with Docker

## Overview

This is a simple **Flask-based calculator** application that provides a web interface for basic arithmetic operations. It is designed as a modular Python package and is containerized using Docker.

## Features

- Addition, subtraction, multiplication, and division
- Flask-based web frontend
- Modular Python structure
- Dockerized for easy deployment

## Project Structure

```
FlaskCalculatorDocker_19.8.24/
│-- app/
│   │-- app.py                 # Flask application entry point
│   │-- Dockerfile            # Docker configuration file
│   │-- requirements.txt      # List of dependencies
│   │-- templates/
│   │   ├── index.html       # HTML template for the calculator UI
│   │-- main.py                # Core calculator logic
│   ├── operations/
│   │   ├── __init__.py      # Package initializer
│   │   ├── addition.py
│   │   ├── subtraction.py
│   │   ├── multiplication.py
│   │   ├── division.py
```

## Installation & Usage

### 1️⃣ Running the App Locally (Without Docker)

#### Prerequisites:

- Python 3.8+
- `pip` installed

#### Steps:

1. Clone the repository:
   ```sh
   git clone <repo_url>
   cd FlaskCalculatorDocker_19.8.24/app
   ```
2. Create a virtual environment (recommended):
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```
3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
4. Run the Flask app:
   ```sh
   python app.py
   ```
5. Open **`http://127.0.0.1:5000/`** in your browser.

---

### 2️⃣ Running the App with Docker

#### Prerequisites:

- Docker installed

#### Steps:

1. Build the Docker image:
   ```sh
   docker build -t flask-calculator .
   ```
2. Run the container:
   ```sh
   docker run -p 5000:5000 flask-calculator
   ```
3. Open **`http://127.0.0.1:5000/`** in your browser.

---

## API Routes

- \*\*GET \*\***`/`** → Renders the calculator UI
- \*\*POST \*\***`/calculate`** → Performs the selected arithmetic operation

---

## Notes

- If the app is not accessible in Docker, ensure `app.run(host="0.0.0.0", debug=True)` is set in `app.py`.
- If modifying the app, rebuild the Docker image before running again.

Enjoy calculating! 🧮🎉

