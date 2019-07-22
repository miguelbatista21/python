#!/usr/bin/python3

#n = 1
#soma = 0
#while n <= 11:
#    x = int(input("Digite o %d numero: " % n))
#    soma = soma + x
#    n = n + 1
#print("Soma: %d" % soma)
#
#
#
#

#myArray = [7, "24", "Fish", "hat stand"]

#print(myArray[0])
#print(myArray[1])
#print(myArray[2])
#print(myArray[3])
#-------------------------------------------------------------------------------
#edificio = ["Familia Sousa", " Familia Brito", "Sr Jorge", "Familia Tanaka"]

#print(edificio[1])

#myWords = ["dudes", "and"]
#myWords.append("Bettys")

#print(myWords[0])
#print(myWords[2])

notas = [
    6,
    7,
    5,
    8,
    9,
]
soma = 0
x = 4
while x < 5:
    soma = soma + notas[x]  #OBS.: É O MESMO QUE soma += notas[x]
    x += 1  #    OBS.: É O MESMO QUE X=X+1
print("Média: %5.2f" % (soma / x))
