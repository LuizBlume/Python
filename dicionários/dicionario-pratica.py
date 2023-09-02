# -*- coding: utf-8 -*-
# O dicionário sempre é usado com chaves.
meu_dicionario = {"A":"AMEIXA", "B":"BOLA", "C":"CACHORRO"}
print(meu_dicionario["A"]);

#Navegação entre os itens da lista.

for chave in meu_dicionario:
    print(meu_dicionario[chave]);

for chave in meu_dicionario:
    print(chave + ":" + meu_dicionario[chave])