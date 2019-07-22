#!/usr/bin/python3

#fatorial de 10
i = 1
fat = 1
while i <= 10:
    fat = fat * i
    i = i + 1
print("Fat(10) = %d" % fat)
#
#>>>Fat(10) = 3628800
#
#
#
#
i = 1
fat = 1
n = int(input("Digite n: "))
while i <= n:
    fat = fat * i
    i = i + 1
print("Fat(%d) = %d" % (n, fat))
#
#>>>>Digite n: 10
#Fat(10) = 3628800
