#!/usr/bin/python3

#Estrutura de repetição while

r = 'S'
while r == 'S':
    n = int(input('Digite um valor: '))
    r = str(input('Quer continuar? [S/N ')).upper()
print('Fim')

#----------------------------------------------------------
n = 1
while n != 0:
    n = int(input('Digite: '))
print('Fim')

#-------------------------------------------------------

num = int(input("digite seu numero: "))  # -Pega o numero do usuario
x = 1  # aqui e aonde  o loop vai comecar # tbm eh chamado de contador
while x <= num:  # n e menor ou igual que x ? se for true ele fica ateh x ser maior
    print(x)
    x += 2  # e a mesma coisa que n = n + 2

#--------------------------------------------------------------------------------

x = int(input("Digite: "))
n = 0
while n <= x:
    print("lol", n)  # vai sair "lol" em todas linhas
    n += 2  # aqui pode usar tbm n = n + 2

# -------------------CONTADORES----------------------------------------------------
#--imprimi numeros pares entre 0 e um numero fornecido usando if
#
fim = int(input("Digite: "))
x = 0
while x <= fim:
    if x % 2 == 0:
        print(x)
    x = x + 1

#-------------------------------------------------------------
#----MOSTRA NUMEROS PARES
fim = int(input("Digite: "))
x = 0
while x <= fim:
    sobra = x % 2
    if sobra == 0:
        print(x)
    x = x + 1

#--------------------------------------------------------------
condicao = True
while (condicao):  #<1>
    print("BLOCO while() e condicao==True")  #<2>
    condicao = False  #<2>
else:
    print("BLOCO ELSE e condicao==False")
#--------------------------------------------------------------

x = int(input("Digite: "))
n = 0
while n <= x:
    print(n)
    n += 3
#--------------------------------------------------
conta = 0
while (conta <= 10):
    conta += 1
    print(x)
else:
    print("Valor da varievel conta e: ", conta)
#
#-------------------------------------------------------
n = int(input("Digite: "))
x = 1
print("while")
while (x < n):
    print(x)
    x = x + 2
else:
    print("else")
print("fim")
