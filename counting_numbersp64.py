for value in range (1,21):
	print (value)

million = []
for value in range (1,1000001):
	million.append (value)
print (million)

million2 = []
for value in range (1,1000001):
	million2.append (value)
print(million2)

print(min (million2))
print (max (million2))
print (sum(million2))

odd = [] # Para que me imprima la lista con solo los impares.
for x in range (1,21,2):
	odd.append (x)
print (odd)

threes = [] # Para que me imprima la lista desde el 3 hasta el 30 de 3 en 3
for x in range (3,31,3):
	threes.append (x)
print (threes)

cubes = []
for x in range (1,11):
	cubes.append (x**3) 
print (cubes)

cubes =[x**3 for x in range(1,11)]
print (cubes)


