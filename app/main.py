import operations


def calculate(x, y, operation):

    #print(f"Received operation: {operation}")              Debugging   
    #print(f"x: {x}, y: {y}, operation: {operation}")       Debugging


    if operation == "+":
        result = operations.addition.add(x, y)
    elif operation == "-":
        result = operations.subtraction.subtract(x, y)
    elif operation == "*":
        result = operations.multiplication.multiply(x, y)
    elif operation == "/":
        result = operations.division.divide(x, y)
    else:
        result = "Invalid operation"

    return result