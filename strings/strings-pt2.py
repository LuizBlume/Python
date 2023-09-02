# -*- coding: utf-8 -*-
a = "Luiz";
b = "Fernando";
concat = a +  " " + b
print(concat.lower())
print(concat.upper())

#Para remover espaços em branco se usa ".strip()"

print(concat.strip());

#Para converter a string em uma lista se usa ".split()"

print(concat.split());

#Método ".find()" busca na string o valor que você definir, aparece a posição.

string = "O rato roeu a roupa do rei de Roma"
busca = string.find("rei")
print(busca)

#Para buscar o restante da frase da string, se usa:

busca = string.find("rei")
print(string[busca:])

#A função replace é usada para substítuir uma parte de uma string.