#Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
# a) o produto do dobro do primeiro com metade do segundo .
# b) a soma do triplo do primeiro com o terceiro. 
# c) o terceiro elevado ao cubo.
a = int(input('insira o primeiro número: '))
b =  int(input('insira o segundo número: '))
c = float (input('insira o terceiro número: '))

rsptA = (a *2) + (b/2)

rsptB = (a *3) + c

rsptC = c **3

print (f'resposta: a) ', rsptA, "\n b) ", rsptB, "\n c)", rsptC)