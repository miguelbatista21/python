s = float(input('Salário: '))
p = float(input('Porcentagem de aumento: '))
aumento = s * p / 100
novo = s + aumento
print('Aumento: R$ %.2f' %aumento)
print('Novo salário: R$ %.2f' %novo)


>>>Salário: 10
>>>Porcentagem de aumento: 15
>>>Aumento: R$ 1.50
>>>Novo salário: R$ 11.50