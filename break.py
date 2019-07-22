#!/usr/bin/python3

soma = 0
while True:
    x = int(input("Digite o numero (0 sai): "))
    if x == 0:
        break
    soma = soma + x
print("soma: %d" % soma)

#Digite o numero (0 sai): 10
#Digite o numero (0 sai): 10
#Digite o numero (0 sai): 50
#Digite o numero (0 sai): 0
#soma: 70
