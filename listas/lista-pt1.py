lista1 = ["Abacate", "Abacaxi", "Manga"];
lista2 = [1,2,3,4,5];
lista3 = ["Abacaxi", 2 , 9.89, True];
for item in lista1:
    print(item)

#A função len() de strings também podem ser usadas aqui.

#Para adicionarmos itens a nossa lista se usa append()

lista1.append("Limão")
print(lista1)

#Para saber se um elemento pertence a lista ou não, se usa in

if 2 in lista2:
    print("O 2 tem na lista")
else:
    print("Não tem na lista");

#Para remover itens de uma lista se usa del.

del lista1[3];
print(lista1)

#Para apagar a lista inteira se usa [:]