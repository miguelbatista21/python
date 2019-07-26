#!/usr/bin/python3
"""
primeiro = int(input('Primeiro numero: '))
segundo = int(input('Segundo numero : '))
terceiro = int(input('Terceiro numero: '))

maior = primeiro

if (segundo > maior):
    maior = segundo
if (terceiro > maior):
    maior = terceiro

print('Maior: ', maior)
"""
#-------------------------------------------------------
#MOSTRA O MAIOR E O MENOR.
a = int(input("primeiro valor: "))
b = int(input("Segundo valor: "))
c = int(input("Terceiro: "))

menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
#verifiando quem é o maior
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c

print(' o menor valor digitado foi {}'.format(menor))
print(' o maior valor digitado foi {}'.format(maior))