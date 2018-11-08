dream_vacation = {}
polling_active = True


while polling_active:
    name = input ("What is your name: ")
    place = input ("What place would you love to go: ")
    
    dream_vacation [name] = place
    repeat = input ("Would you like to visit another place? (yes/no) ")
    if repeat == "no":
        polling_active = False
print ("\n---Dream vacations---")

for name, place in dream_vacation.items():
    print (name.title() + " you would love to go to " + place.title())    

