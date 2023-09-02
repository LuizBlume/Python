# -*- coding: utf-8 -*-
num1 = float(input("Informe um número: "))
num2 = float(input("Informe outro número: "))
operacao = input("Informe uma operação (+, -, *, /): ")

if operacao == "+":
    adicao = num1 + num2
    print("Resultado:", adicao)
elif operacao == "-":
    sub = num1 - num2
    print("Resultado:", sub)
elif operacao == "*":
    mult = num1 * num2
    print("Resultado:", mult)
elif operacao == "/":
    if num2 != 0:
        div = num1 / num2
        print("Resultado:", div)
    else:
        print("Erro: Divisão por zero.")
else:
    print("Opção inválida")