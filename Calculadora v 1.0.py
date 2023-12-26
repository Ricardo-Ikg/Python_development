# Projeto de calculadora simples utilizando condicionais
# Calculadora Versão 1.0
#Autor: Ricardo

flag = "nao"
while (flag == "nao"):

    x = float(input("Digite um número "))
    operador = input("Digite um operador + - / * ")
    y = float(input("Digite um número "))
    
    if operador == "+":
        operacao = x + y 

    if operador == "-":
        operacao = x - y

    if operador == "*":
        operacao = x * y

    if operador == "/":
        operacao = x / y

    print(x, operador, y, "=", operacao)
    
    flag = input("Deseja sair?")
