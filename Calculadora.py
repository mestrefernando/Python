# -*- coding: utf-8 -*-
"""
Em Português
Calculadora
Autor: Fernando Mestre
Soma, Subtracção, Divisão, Multiplicação e Expoente
"""
print("-----Calculadora básica-----")

sair = False
while sair == False:
    num1 = float(input("Digite o primeiro número: "))
    operador = (input("Digite o operador: "))
    num2 = float(input("Digite o segundo número: "))
    if operador == "+":
        print(num1 + num2)
    elif operador == "-":
        print(num1 - num2)
    elif operador == "/":
        print(num1 / num2)
    elif operador == "*":
        print(num1 * num2)
    elif operador == "**":
        print(num1 ** num2)
    else:
        print("Operador inválido")
    teste = input("Deseja sair (Sim/Não?): ")
    if teste == "s":
        sair = True

"""In english""" 

Calculator
Author: Fernando Mestre
Sum, Subtraction, Division, Multiplication and Exponent
"""
print("-----Basic Calculator-----")

exit = False
while out == False:
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
    else:
        print("Invalid operator")
    test = input("Do you want to leave (Yes/No?): ")
    if test == "s":
        exit = True
