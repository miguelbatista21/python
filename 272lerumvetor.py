#!/usr/bin/python3

#tipos de VETORES
vetor = []
i = 1
while i <= 5:
    n = int(input("Digite um numero: "))
    vetor.append(n)
    i = i + 1
print("Vetor lido:", vetor)
#
#
#

meuVetor = [10] * 5
print(meuVetor)
#
#-------------------------------------------------------
#
print(dir(meuVetor))
[
    ..., 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert',
    'pop', 'remove', 'reverse', 'sort'
]
#------------------------------------------------------
#

#
#----------------------------------------------------
#

vetor = []
i = 1
while i <= 10:
    n = float(input("Digite um numero: "))
    vetor.append(n)
    i += 1
i = 9
while i >= 0:
    print(vetor[i])
    i -= 1
#
#>>>Digite um numero: 10
#>>>Digite um numero: 20
#>>>Digite um numero: 30
#>>>Digite um numero: 40
#>>>Digite um numero: 50
#>>>Digite um numero: 60
#>>>Digite um numero: 70
#>>>Digite um numero: 80
#>>>Digite um numero: 90
#>>>Digite um numero: 100
#100.0
#90.0
#80.0
#70.0
#60.0
#50.0
#40.0
#30.0
#20.0
#10.0

#
#----------------------------------------------------
#
