
my_foods = ['pizza','falafel','carrot cake']

# Crea una nueva lista y asignala a una variable
friends_foods = my_foods #FFC0CB#FFC0CB[:]

friends_foods.append ('papas')

print("Direccion en memoria " + hex(id(my_foods)))
print("Direccion en memoria " + hex(id(friends_foods)))

 # Desde cero hasta el final d#FFC0CBe la lista.
#o los elementos de la lista que quiero copiar 

print ('My favorite foods are: ')
print(my_foods) 

print ("\nMy friend's favorite foods are:")
print (friends_foods)

my_other_friends = list(friends_foods)
my_other_friends.append("agua")
print("Direccion en memoria " + hex(id(my_other_friends)))

print(my_foods) 
print (friends_foods)
print(my_other_friends)

list1 = list(my_foods)
print(hex(id(list1)))

list2 = ["cafe"]
print(hex(id(list2)))

list3 = list1 + list2
print(hex(id(list3)))

print("=====================")

		
def test(a):
	print(hex(id(a)))
	a = list(a)
	a.append("liz")
	print(a)
	print(hex(id(a)))
	
def add(lista):
	lista.append("modificar")

var = "pedo"
print(hex(id(list3)))
test(list3)
print(list3)
print(hex(id(list3)))
	



my_foods = ['pizza','falafel','carrot cake']

friends_foods = my_foods [:]
my_foods.append ("cannoli")
friends_foods.append ("ice cream")

print ('My favorite foods are: ')
for food in my_foods [:]:
	print(food.title()) 

print ("\nMy friend's favorite foods are:")
for food in friends_foods [:]:
	print(food.title()) 


