num = int(input("Coloque um numero: "))

if num < 200:
    preco = 0.20
else:
    if num <= 400:
        preco = 0.18
    else:
        if num >= 800:
            preco = 0.08
        else:
            preco = 0.15

print("Resultado : ", (num * preco))
print(preco)

#ELSE
#   O que fazer quando a condiçao do if é falsa??
#   Os dois códigos abaxo fazem a mesma coisa:

idade = int(input("Digite a idade de seu carro: "))
if idade <= 3:
    print("Seu carro é novo")
if idade > 3:
    print("Seu carro é velho")
# ------------------------------------------------------------------

idade = int(input("Digite a idade de seu carro:"))
if idade <= 3:
    print("Seu carro é novo")
    #else:
    print("Seu carro é velho")

#------------------------------------------------------------------

v = int(
    input("Velocidade: "))  #ISSO É OQUE VAI APARECER QUANDO RODAR O PROGRAMA
if v > 110:
    multa = (v - 110) * 5  #
    print("Você foi multado!")
    print("Valor d multa: R$ %5.2f" % multa)
