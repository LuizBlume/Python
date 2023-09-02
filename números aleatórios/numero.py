import random
#Serve para importar o random
numero = random.randint(0, 10) #Serve para iniciar o intervalo de número aleatório e definir o final.
print(numero)

# O random.seed() serve para forçar o python é executar um número
random.seed(1)
numero = random.randint(0, 10)
print(numero)

# O método .choice() ele seleciona um número de uma lista.

lista = [6, 45, 9];
numero = random.choice(lista)
print(numero)