def add(x, y):
    return x + y

def subtract(x,y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x/y

num1 = float(input("Enter number 1 : "))
operation = input("select operation (+, -, *, /): ")
num2 = float(input("Enter number 2 : "))

if operation == "+":
    result = add(num1,num2)

if operation == "-":
    result = subtract(num1,num2)

if operation == "*":
    result = multiply(num1,num2)

if operation == "/":
    result = divide(num1,num2)

print(result)


