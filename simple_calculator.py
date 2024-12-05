"""
********************************************************************************
* Project Name:  Calculator
* Description:   A simple calculator program built in Python that supports basic arithmetic operations
* Author:        ziqkimi308
* Created:       2024-12-05
* Updated:       2024-12-05
* Version:       1.0
********************************************************************************
"""

from art import logo
from replit import clear

# Define functions
def add(n1, n2):
    return n1 + n2
def minus(n1, n2):
    return n1 - n2
def multiple(n1, n2):
    return n1 * n2
def divide(n1, n2):
    return n1 / n2

# Define dictionary
operations = {
    "+" : add,
    "-" : minus,
    "*" : multiple,
    "/" : divide,
}

# Define calculator
def calculator():
    # Opening logo
    print(logo)

    # Opening statement
    n1 = float(input("Enter first number: "))

    # Print operators
    for i in operations:
        print(i)

    should_continue = True
    while should_continue:
        symbol = input("Enter an operation: ")
        n2 = float(input("Enter next number: "))

        # Calculate using function
        cal_func = operations[symbol] # This will call either add, minus, multiple, or divide
        ans = cal_func(n1, n2)

        print(f"{n1} {symbol} {n2} = {ans}")

        next_n = input("Type 'y' to continue or 'n' for new calculation: ").lower()
        if next_n == 'y':
            n1 = ans
        else:
            clear()
            calculator()

# Out of defined function calculator, call calculator()
calculator()


