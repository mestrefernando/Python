# -*- coding: utf-8 -*-
"""
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
