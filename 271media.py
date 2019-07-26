#!/usr/bin/python3

#(1):
#CALULE A MEDIA DE 5 NOTAS.

notas = [6, 7, 5, 8, 9]
soma = 0
x = 0
while x < 5:
    soma += notas[x]
    x += 1
print("media: %5.2f" % (soma / x))
