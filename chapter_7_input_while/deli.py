sandwich_orders = ["chicken","tuna","vegetables"]
finished_sandwiches = []

while sandwich_orders:
    finished_sandwich = sandwich_orders.pop()
    
    print ("Making " + finished_sandwich.title() + " sandwich")
    finished_sandwiches.append(finished_sandwich)
print ("\nThe folling sandwiches are ready")

for finish_sandwich in finished_sandwiches:
    print (finish_sandwich.title())
    
    
