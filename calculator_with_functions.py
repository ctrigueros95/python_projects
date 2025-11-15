# Make a calculator that can add, subtract, multiplnum2 and divide using functions

num1 = float(input("Give me the first value: "))

num2 = float(input("Give me the second value: "))

op = input ("Give me an operator: ")

def add(num1, num2):
    return num1 + num2    

def subtract(num1, num2):
    return num1 - num2   

def multiply(num1,num2):
    return num1 * num2

def divide(num1,num2):
    return num1 / num2

def modulo(num1,num2):
    return num1 % num2

if op == "+":

    print(add(num1,num2))
        
if op == "-":

    print(subtract(num1,num2))
        
if op == "*":

    print(multiply(num1,num2))
        
if op == "/":

    print(divide(num1,num2))
        
if op == "%":

    print(modulo(num1,num2))