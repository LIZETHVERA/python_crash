usernames = ["maria","pablo","juan","catalina","admin"]
if usernames:
    for username in usernames:
        if username == "admin":
            print ("Hello admin would you like to see a status report")
        else:
            print ("hello " + username.title() + " Thank you for logging again")
else: 
    print ("We need to find more users ")
