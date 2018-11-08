pizzas = ["cheese","pepperoni","vegetables"]

friend_pizzas = pizzas [:]
pizzas. append ('broccoli')

friend_pizzas.append ('chicken')

print ("My favorite pizzas are: ")
for pizza in pizzas [:]:
	print (pizza.title())

print ("My friends favorites pizzas are: ")
for pizza in friend_pizzas [:]:
	print (pizza.title())

my_foods = ['pizza','falafel','carrot cake']

friends_foods = my_foods [:]
my_foods.append ("cannoli")
friends_foods.append ("ice cream")

print ('My favorite foods are: ')
for food in my_foods [:]:
	print(food.title()) 

print ("\nMy friend's favorite foods are:")
for food in friends_foods [:]:
