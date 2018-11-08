age = 12

if age <4: 
    print ("Your admission cost is $o.")
elif age < 18:
    print ("Your admission cost is $5.")
else:
    print ("Your admission cost is $10.")

print ("\n")
age = 63
if age < 4 : 
    price = 0
elif age < 18:
    price = 5
elif age <65: 
    price =10
else:
    price = 5

print ("Your admission cost is $" + str(price)+ ".")

print ("\n")
age = 61
if age < 4 : 
    price = 0
elif age < 18:
    price = 5
elif age < 65: 
    price = 10
elif age >= 65:
    price = 5
print ("Your admission cost is $" + str(price)+ ".")
