#João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho. Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente. João precisa que você faça um programa que leia a variável peso (peso de peixes) e calcule o excesso. Gravar na variável excesso a quantidade de quilos além do limite e na variável multa o valor da multa que João deverá pagar. Imprima os dados do programa com as mensagens adequadas.

pesoPeixe = int(input('insira o peso: '))

excesso = pesoPeixe - 50

valorMulta = excesso * 4.00

if pesoPeixe > 50:
    print(f'O Você terá que pagar uma multa de {valorMulta:.2f}')

else:
    print('Você está livre de multas, com o peso de até 50kgs.')
