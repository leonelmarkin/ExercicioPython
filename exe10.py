#Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.

salarioHora = float(input('insira valor p/ hora trabalhada: '))
quantHora = int(input('insira o número de horas trabalhadas no mês: '))

total = salarioHora * quantHora

print(f'O valor da sua hora trabalhada é de {total:.2f}')