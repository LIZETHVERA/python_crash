message = input ("Tell me something, and i will repetar it back to you: ")
print (message)

name  = input ("please enter your name: ")
print ("hello, "+  name + "!")

prompt = "If you tell us who you are, we can personalize the messages you see"
prompt += "\nWhat is your first name?"

name = input (prompt)
print ("\nHello," + name + "!")

prompt = "Tell me something, and i will repeat the message to you: "
prompt += "\nEnter 'quit' to end the program. ?"

message = ""
while message != "quit":
    message = input (prompt)
    print (message)
 

prompt = "Tell me something, and i will repeat the message to you: "
prompt += "\nEnter 'quit' to end the program. ?"

message = ""
while message != "quit":
    message = input (prompt)
    if message != "quit":
        print (message)
 
