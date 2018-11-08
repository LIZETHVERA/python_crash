movie_age = input ("\nEnter your age ")
movie_age = int (movie_age)

while True:
    if movie_age < 3:
        print ("The ticket is free")
    elif movie_age <= 12:
        print ("the ticket cost is $10")
    else:
        print ("The ticket cost is $15")
    break 
    
