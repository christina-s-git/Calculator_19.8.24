# Step 1: Use an official lightweight Python image
FROM python:3.9-slim

# Step 2: Set the working directory inside the container
WORKDIR /app

# Step 3: Copy project files into the container
COPY . /app

# Step 4: Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Step 5: Expose the Flask port
EXPOSE 5000

# Step 6: Run the application
CMD ["python", "app.py"]
