# Faça um Programa que peça as 4 notas bimestrais e mostre a média.

print('insira as notas !')

n1 = int (input('insira a nota 1:'))
n2 = int (input('insira a nota 2:'))
n3 = int (input('insira a nota 3:'))
n4 = int (input('insira a nota 4:'))

soma = n1 + n2 + n3 + n4

media = soma/4

print('A Média é: ', media)

if media <6 :
    print("Reprovado")

else :
    print('Aprovado')