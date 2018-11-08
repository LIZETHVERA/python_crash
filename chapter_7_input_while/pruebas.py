prompt = "Tell me something, and i will repeat the message to you: "
prompt += "\nEnter 'quit' to end the program. ?"

active = True 
while active:
    message = input (prompt)
    
    if message == "quit":
        active = False 
    else:
        print (message)
        
