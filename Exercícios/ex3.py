import math

a = float(input("Digite o coeficiente 'a': "))
b = float(input("Digite o coeficiente 'b': "))
c = float(input("Digite o coeficiente 'c': "))
delta = b**2 - 4*a*c
if delta > 0:
    x1 = (-b + math.sqrt(delta)) / (2*a)
    x2 = (-b - math.sqrt(delta)) / (2*a)
    print(f"As raízes são: x1 = {x1} e x2 = {x2}")
elif delta == 0:
    x1 = -b / (2*a)
    print(f"A raiz dupla é: x1 = {x1}")
else:
    realPart = -b / (2*a)
    imaginaryPart = math.sqrt(-delta) / (2*a)
    print(f"As raízes complexas são: x1 = {realPart} + {imaginaryPart}i e x2 = {realPart} - {imaginaryPart}i")