requested_toppings = ["mushrooms","extra cheese"]
if "mushrooms" in requested_toppings:
    print ("Adding mushrooms.")
if "pepperoni" in requested_toppings:
    print ("Adding Pepperoni.")
if "extra cheese" in requested_toppings:
    print ("Adding extra cheese")
print ("\nFinished making your pizza")

print ("\n")
requested_toppings = ["mushrooms","extra cheese","green peppers"]
for requested_topping in requested_toppings:
    print ("adding "+ requested_topping + ".")
print ("\nFinished making your pizza")

print ("\n")
requested_toppings = ["mushrooms","extra cheese","green peppers"]
for requested_topping in requested_toppings:
    if requested_topping == "green peppers":
        print ("Sorry, we are out of green peppers rigth now")
    else:
        print ("adding "+ requested_topping + ".")
print ("\nFinished making your pizza")
print ("\n")

requested_toppings = []
if requested_topping in requested_toppings:
    print ("Adding " + requested_topping + ".")
else:
    print ("Are you sure you want a plain pizza")

print ("\n")

available_toppings = ["mushrooms","olives","green peppers","pepperoni","pineapple","extra cheese",]
requested_toppings = ["mushrooms","french frieds","extra cheese"]
for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print ("Adding " + requested_topping + ".")
    else:
        print ("sorry, we don't have " + requested_topping + ".")
print ("\nFinished making your pizza")





