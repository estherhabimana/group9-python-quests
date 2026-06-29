

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: cannot divide by zero"
    return a / b

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
operation = input("Enter operation (add, subtract, multiply, divide): ")

if operation == "add":
    print("Result:", add(num1, num2))
elif operation == "subtract":
    print("Result:", subtract(num1, num2))
elif operation == "multiply":
    print("Result:", multiply(num1, num2))
elif operation == "divide":
    print("Result:", divide(num1, num2))
else:
    print("Unknown operation. Please type add, subtract, multiply, or divide.")
