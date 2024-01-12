#Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
# Para mulheres: (62.1*h) - 44.7
# Para homens: (72.7*h) - 58

h = float(input('Qual sua Altura?: '))

sexo = int(input('Digite 1 para Homem ou 2 para Mulher: '))
pesoHomem = (72.7*h) - 58
pesoMulher = (62.1*h) - 44.7

if sexo == 1:
    print("O seu peso ideal é: ",pesoHomem)

if sexo == 2:
    print("O seu peso ideal é: ",pesoMulher)

else:
    print('insira o número correto')

