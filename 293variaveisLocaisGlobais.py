#!/usr/bin/python3

a = 5


def muda_e_imprime():
    a = 7
    print('a dentro da funcao: %d' % a)


print('a antes de mudar: %d' % a)
muda_e_imprime()
print('a depois de mudar: %d' % a)

#>>>>
#a antes de muda: 5
#a dentro da função: 7
#a depois de mudar: 5
