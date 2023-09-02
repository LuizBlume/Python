# list comprehension
# Aqui será visto como ter o valor ao quadrado da lista X.
x = [1, 2, 3, 4, 5];
y = [];
for i in x:
    y.append(i**2)
print(x)
print(y)

# Agora uma maneira mais simples de ter o valor ao quadrado.

x = [1, 2, 3, 4, 5];
y = [i**2 for i in x];
print(y)

# Agora um exemplo envolvendo uma condiçao.

x = [1, 2, 3, 4, 5];
y = [i**2 for i in x];
z = [i for i in x if i%2 == 1]
print(y)
print(z)
