#Faça um programa que receba duas notas digitadas pelo usuário. Se a nota for maior ou igual a 6, escreva aprovado, senão escreva reprovado

grade = float(input("Digite o valor da primeira nota:"))
grade2 = float(input("Digite o valor da segunda nota:"))

mean = (grade + grade2) / 2

if grade < 0 or grade2 < 0:
    print("Valores de notas inválidos")

elif mean < 6:
    print("Aluno Reprovado")

else:
    print("Aluno Aprovado!!!")
