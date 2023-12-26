num_1 = float(input("Digite um número: "))
num_2 = float(input("Digite um número: "))
operador = input("Digite o operador: ")

if operador == '+':
    operacao = num_1 + num_2

if operador == '-':
    operacao = num_1 - num_2

if operador == "/":
    if num_2 == 0:
        print("Não é possível dividir por zero!")

    else:
        operacao = num_1 / num_2

if operador == '*':
    operacao = num_1 * num_2

else: 
    print("Sinal não reconhecido")

print(operacao)