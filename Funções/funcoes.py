# -*- coding: utf-8 -*-
def soma(x, y):
    print(x + y)

soma(5, 10);

#Acima foi usado para chamar uma função e substituir o valor de uma variável.

#Abaixo, o return serve para retornar um valor. E o valor irá funcionar apartir de um print.

def soma(x, y):
    return x+y

s = soma(5, 10)
print(s)

#Abaixo também pode fazer uma conta usando duas strings.

def soma(x, y):
    return x+y

def mult(x, y):
    return x*y

m = mult(5, 3)
s = soma(5, 10)
print(soma(s, m));