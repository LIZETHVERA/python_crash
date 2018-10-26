cities = ["cartagena","medellin","bogota","santamarta","cali"]
print (cities)

lista =  []

for x in (cities):
	lista.append(x[0])
	
print(sorted(lista))

li = []
for x in sorted (cities):
	li.append(x[0])
	
print(li)

cities.reverse()
print (cities) 

print (dir (cities))
