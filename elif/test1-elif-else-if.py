num = int(input("Coloque um numero: "))
if num < 200:
    preco = 0.20
elif num <= 400:
    preco = 0.18
elif num <= 800:
    preco = 0.15
else:
    preco = 0.08

print("Resultado:", (num * preco))
print(preco)

#if soma > 0:
#     print "Maior que Zero."
#elif soma = 0:
#     print "Igual a Zero."
#else:
#     print "Menor que Zero."

#num = int(input("Coloque um numero: "))

#if num < 200:
#    preco = 0.20
#else:
#    if num <= 400:
#        preco = 0.18
#    else:
#        if num >= 800:
#            preco = 0.08
#        else:
#            preco = 0.15

#print("Resultado :", (num * preco))
#print(preco)
#
#
#
#        < 200?                PREÇO = 0.20
#       /----------------------------------------------
#      /TRUE
#-----/                          < 400?     PREÇO = 0.18
#     \                          /-----------------------
#      \FALSE                   /TRUE
#       \----------------------
#                               \FALSE      PREÇO = 0.15
#                                \-----------------------
