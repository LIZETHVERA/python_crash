favorite_places = {
    "Sofia": ["cali","bogota", "barranquilla"],
    "Toya" : ["LA","san diego"],
    "juan" : ["london"],
    }

for name, places in favorite_places.items():
    if len (places)== 1:
        print ("\n" + name.title() + "'s favorite place is: ")
        for place in places:
            print ("\t" + place.title())
        
for name, places in favorite_places.items():
    print ("\n" + name.title() + "'s favorite places are: ")
    for place in places:
        print ("\t" + place.title())
        
        
print ("\n")
favorite_numbers = {
    "lucia": [5,6,7],
    "maria": [3,4,5],
    "sofia": [10,11,12],
    "carlos": [15,16,17],
    }

for name, numbers in favorite_numbers.items():
    print ("\n" + name.title() +"'s favorite numbers are" )
    for number in numbers:
        print ("\t" + str (number)) 
