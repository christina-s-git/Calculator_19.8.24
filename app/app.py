#this file starts the flask app

from flask import Flask, render_template, request 
from main import calculate

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])

def index():
    result = None 

    if request.method == "POST":
        #print(request.form)  # <-- Debugging step
        num1 = float(request.form["num1"]) #
        num2 = float(request.form["num2"])
        operation = request.form["operation"]

        result = calculate(num1, num2, operation)
        #print(f"Result from calculate(): {result}")

    return render_template("index.html", result = result)



if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)




#  
#num1 in square brackets refers to the user input from html form ...
#<form method="POST">
#    <input type="text" name="num1">  <!-- The name here is "num1" -->
#    <button type="submit">Calculate</button>
#</form>
