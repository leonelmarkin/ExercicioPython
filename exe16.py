#Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.

metrosQuadrados = int(input('insira a quantidade de metros por quadrado:'))

litrosNecessários = metrosQuadrados / 3

quantLatas = litrosNecessários / 18

valor = quantLatas * 80

print(f"a quantidade de latas de tinta a serem compradas são:\n{quantLatas:.2f}")
print(f'O valor total fica de: R$ {valor:.2f}')



