responses = {}
#Set a fal to indicate that polling is active.

polling_active = True

while polling_active:
    #Promts for the person's name and response.
    name = input ("\nWhat is your name ")
    response = input ("\nWhich mountain would you want to climb someday? ")
    
    #Store the response in the dictionary.
    responses[name] = response
    
    #Find out in anyone els is going to take the poll.
    repeat = input ("Would you like to let another person respond? (yes / no) ")
    if repeat == "no":
        polling_active = False
#Polling is complete. Show the results
print ("\n--- Poll Results---")
for name, response in responses.items():
    print (name + " Would like to climb " + response + ".")
    
    
