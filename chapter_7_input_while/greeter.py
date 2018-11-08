
def greet_user():
    """Display a simple greeting."""
    print ("Hello!")
greet_user()


def greet_user(username):
    """Display a simple greeting."""
    print ("Hello," + username.title() + "!")
    
greet_user("jesse")

def display_message():
    print ("I am learning about functions.")
display_message()

def favorite_book(title):
    print ("one of my favorite books is " + title.title())
favorite_book("Alice in wonderlad")
