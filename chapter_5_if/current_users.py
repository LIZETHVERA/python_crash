  

current_users = ["MARIA","pablo","juan","Catalina","admin"]
new_users = ["maria","juana,","gabriel","CATALINA","ana"]

current_users = [current_user.lower() for current_user in current_users]
for new_user in new_users:
    if new_user.lower() in current_users:
        print ("Sorry " + new_user + " you will be enter a new username")
    else:
        print (new_user + " The username is available")

