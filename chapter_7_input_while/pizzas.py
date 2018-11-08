prompts = "\nEnter a topping you want in your pizza"
prompts += "\nEnter 'quit' to end your order. "
message = ""

while message != "quit":
    message = input (prompts)
    if message == "quit":
        break 
    print ("You add " + message.title() + ".")
    

prompts = "\nEnter a topping you want in your pizza"
prompts += "\nEnter 'quit' to end your order. "
message = ""

active = True
while active: 
    message = input (prompts)
    if message == "quit":
        active = False 
        break 
    print ("You add " + message.title() + ".")
    
