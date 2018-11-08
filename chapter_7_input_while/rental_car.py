car = input ("What kind of car would you like rent?: ")
print ("Let me see if i can find you a " + car)

restaurant = input ("How many people are in your group: ")
restaurant = int(restaurant)

if restaurant > 8:
    print ("You have to wait for a table")
else:
    print ("Your table is ready ")
    
multiples = input ("Enter a number and see if it is multiple of 10 or not ")
multiples = int (multiples)

if multiples % 10 == 0:
    print ("is multiple of 10")
else:
    print ("is not a multiple of 10")
    
