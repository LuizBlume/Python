# -*- coding: utf-8 -*-
#Forma sem função enumerate
lista = ["abacate", "bola", "cachorro"];
for i in range(len(lista)):
    print(i, lista[i])

# Função enumarate

lista = ["abacate", "bola", "cachorro"];
for i, nome in enumerate(lista):
    print(i, nome)