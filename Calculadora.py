# -*- coding: utf-8 -*-
"""
Calculator
Author: Fernando Mestre
Sum, Subtraction, Division, Multiplication, Exponent, Modulo and Integer Division
"""
print ("-----Basic Calculator-----")
exit = False
while exit == False:
    num1 = float(input("Type first number: "))
    operator = (input("Type operator: "))
    num2 = float(input("Type second number: "))
    if operator == "+":
        print(num1 + num2)
    elif operator == "-":
        print(num1 - num2)
    elif operator == "/":
        print(num1 / num2)
    elif operator == "*":
        print(num1 * num2)
    elif operator == "**":
        print(num1 ** num2)
    elif operator == "//":
        print(num1 // num2)
    elif operator == "%":
        print(num1 % num2)
    else:
        print("Invalid operator")
    test = input("Do you want to leave (Yes/No?): ")
    if test == "Yes":
        exit = True

