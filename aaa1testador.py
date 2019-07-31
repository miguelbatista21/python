#!/usr/bin/python3

#a = int(input("1Digite: "))
#b = int(input("2Digite: "))
#c = int(input("3Digite: "))

#if a >= b and a >= c:
#    print('primeiro: %d' % a)
#elif b >= c:
#    print('Segundo: %d' % b)
#else:
#    print('Terceiro: %d' % c)

#-------------------------------------------------
#uma lista com 3 notas
#notas = [7.5, 9, 8.3]
#acessando uma nota
#print (notas[0])
#>>>7.5
#mudando a primeira nota
#notas [0] = 8.7
#print (notas[0])
#>>>8.7
#print(200 / 6)
#print(205 // 6)
#
#
#
#
# Python code to demonstrate the working of
# sum()

#numbers = [1, 2, 3, 4, 5, 1, 4, 5]

# start parameter is not provided
#Sum = sum(numbers)
#print(Sum)

# start = 10
#Sum = sum(numbers, 10)
#print(Sum)

numeros = input().split(" ")
numeros.sort()

for num in numeros:
    print(num)

print('\n')

for num in numeros:
    print(num)
