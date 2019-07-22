#!/usr/bin/python3
#-------ACUMULADORES
#
#
#
#------------MEDIA----------
n = 1
soma = 0
while n <= 10:
    x = int(input("Digite o %d numero: " % n))
    soma = soma + x
    n = n + 1
print("Soma: %d" % soma)
#
#
#
#
#----------CALCULANDO A MEDIA-FORMA MAIS SIMPLES

numeros = range(1, 100)
media = sum(numeros) / len(numeros)
print(media)

#
#
#
#
#
#-----------OUTRAS FORMAS: COM RANGE
soma = 0
quantidade = 0
for i in range(15, 101):
    soma += i
    quantidade += 1

media = soma / quantidade
print(media)
#
#
#
#
#
#-----------OUTRAS FORMAS: SEM RANGE
soma = 0
quantidade = 0
i = 15
while i <= 100:
    soma += i
    quantidade += 1
    i += 1

media = soma / quantidade
print(media)