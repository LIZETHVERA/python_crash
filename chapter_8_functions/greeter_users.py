def greet_users (names):
    """print a simple greeting o each user in the list"""
    for name in names:
        msg = "Hello, " + name.title() + "!"
        print (msg)
usernames = ["hannah","ty","margot"]
greet_users (usernames)

