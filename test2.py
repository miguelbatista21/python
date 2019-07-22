#!/usr/bin/python3

#---------------FATORIAL DE 12
i = 1
fat = 1
while i <= 12:
    x = int(input("Digite: "))

    fat = fat * i
    i = i + 1
print("Fat(12) = %d" % fat)

#imprima os numeros pares entre 0 e um numero fornecido usando if

n = 1
soma = 0
while n <= 10:
    x = int(input("Digite o %d numero: " % n))
    soma = soma + x
    n = n + 1
print("Soma: %d" % soma)
#-----------------------------------------------------------------

n = int(input("Digite"))
x = 1
while x <= n:x
    print(x)
    x = x + 2
#---------------------------------------------------------------------

soma = 0
while True:
   x = int(input("Digite o numero (0 sai): "))
   if x == 0:
       break
    soma = soma + x
print("Soma: %d" % soma)


#TABUADA

tabuada = 1
while tabuada <= 10:
    n = 1
    print('Tabuada %d' % tabuada)
    while n <= 10:
        print('%d x %d = %d' % (tabuada, n, tabuada * n))
        n = n + 1
    tabuada = tabuada + 1

