#Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
#salário bruto.
#quanto pagou ao INSS.
#quanto pagou ao sindicato.
#o salário líquido.
#calcule os descontos e o salário líquido, conforme a tabela abaixo:

salarioHora = float(input('insira valor p/ hora trabalhada: '))
quantHora = int(input('insira o número de horas trabalhadas no mês: '))

salarioBruto = salarioHora * quantHora

ir = (salarioBruto * 11)/100

inss = (salarioBruto * 8)/100

sindicato = (salarioBruto * 5)/100

salarioLiquido = salarioBruto - (ir + inss + sindicato)

print('Veja os valores:\nSalario Bruto:',salarioBruto, '\nDesconto IR: ', ir, '\nDesconto INSS: ', inss, '\nDesconto Sindicato:', sindicato)
print('Saldo Líquido: ', salarioLiquido)