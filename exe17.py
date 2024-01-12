#Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
#Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
#comprar apenas latas de 18 litros;
#comprar apenas galões de 3,6 litros;
#misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.

import math

valortotal = int

metrosQuadrados = int(input('insira a quantidade de metros por quadrado:'))

litrosNecessários = metrosQuadrados / 6

quantGalao = math.ceil (litrosNecessários / 3.6)

quantLatas = math.ceil(litrosNecessários / 18)

valorLata =  quantLatas * 80.00
valorGalao = quantGalao * 25.00

valorAcrescimo = (valorGalao+valorLata * 10) /100

mistGalaoeLata = valorAcrescimo + valorLata + valorGalao

print(f"\nSituação 1: Comprar apenas latas de 18 litros")
print(f"Quantidade de latas: {quantLatas}")
print(f"Preço total: R$ {valorLata:.2f}")

print("\nSituação 2: Comprar apenas galões de 3,6 litros")
print(f"Quantidade de galões: {quantGalao}")
print(f"Preço total: R$ {valorGalao:.2f}")

restante = litrosNecessários % 18
if restante != 0:
    restante = restante / 3.6


valortotal = math.ceil (valorLata + restante + valorAcrescimo)

print("\nSituação 3: Misturar latas e galões para minimizar o desperdício")
print(f"Quantidade de latas: {quantLatas}")
print(f"Quantidade de Galões: {restante}")
print(f"Preço total: R$ {valortotal:.1f}")




    





