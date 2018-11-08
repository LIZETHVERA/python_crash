sandwich_orders = ["chicken","pastrami","tuna","pastrami","vegetables","pastrami"]
finished_sandwiches = []

while "pastrami" in sandwich_orders:
    sandwich_orders.remove("pastrami")
print ("Deli has run out of pastrami")
    
print ("\n")

while sandwich_orders:
    finished_sandwich = sandwich_orders.pop()
    
    print ("Making " + finished_sandwich.title() + " sandwich")
    finished_sandwiches.append(finished_sandwich)
print ("\nThe folling sandwiches are ready")

for finish_sandwich in finished_sandwiches:
    print (finish_sandwich.title())    
