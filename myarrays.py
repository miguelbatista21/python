myArray = [7, "24", "Fish", "hat stand"]

print(myArray[0])
print(myArray[1])
print(myArray[2])
print(myArray[3])
#-------------------------------------------------------------------------------
edificio = ["Familia Sousa", " Familia Brito", "Sr Jorge", "Familia Tanaka"]

print(edificio[1])
#--------------------------------------------------------------------------------
myWords = ["dudes", "and"]
myWords.append("Bettys")

print(myWords[0])
print(myWords[2])

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


#append()	Adds an element at the end of the list
#clear()	Removes all the elements from the list
#copy()	    Returns a copy of the list
#count()	Returns the number of elements with the specified value
#extend()	Add the elements of a list (or any iterable), to the end of the current list
#index()	Returns the index of the first element with the specified value
#insert()	Adds an element at the specified position
#pop()	    Removes the element at the specified position
#remove()	Removes the first item with the specified value
#reverse()	Reverses the order of the list
#sort()	    Sorts the list