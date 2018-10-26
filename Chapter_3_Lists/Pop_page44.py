motorcycles = ["honda","yamaha","suzuki"]
print (motorcycles)

popped_motorcycle = motorcycles.pop() # Este remueve el último de la lista
print (motorcycles) # Se imprime la lista sin el último elemento
print (popped_motorcycle) # Este muestra es el elemento eliminado


motorcycles = ["honda","yamaha","suzuki"]
last_owned = motorcycles.pop()
print ("The last motocycle I owned was a " + last_owned.title()+".")

motorcycles = ["honda","yamaha","suzuki"]
firts_owned = motorcycles.pop(0)
print ("The firts motocycle I owned was a " + firts_owned.title()+".")

motorcycles = ["honda","yamaha","suzuki","ducati"]
print (motorcycles)
motorcycles.remove("ducati") # Cuando no sabemos la posición en la que está, pero conocemos su valor. 
print (motorcycles)

motorcycles = ["honda","yamaha","suzuki","ducati"]
print (motorcycles)
too_expensive = "ducati"
motorcycles.remove(too_expensive)
print (motorcycles)
print ("\nA " + too_expensive.title() + " is too expensive for me.")
