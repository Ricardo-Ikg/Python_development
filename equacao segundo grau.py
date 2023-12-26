from math import sqrt

a = float(input("Digite o valor de A:"))
b = float(input("Digite o valor de B:"))
c = float(input("Digite o valor de C:"))

delta = (b**2 - 4*a*c)

if delta < 0:
    print("Não existem raízes reais")

else: 
    print((-b + sqrt(delta)) / 2*a) 
    print((-b - sqrt(delta)) / 2*a)
