alien_0 ={"color":"green","points":"5"}
print (alien_0["color"])
print (alien_0["points"])


alien_0 ={"color":"green","points":"5"}

new_points = alien_0["points"]
print ("You just earned " + str(new_points) + " points!")


alien_0 ={"color":"green","points":"5"}
print (alien_0)
alien_0["x_position"] = 0
alien_0["y_position"] = 25
print (alien_0)

alien_0 = {}
alien_0 ["color"] = "green"
alien_0 ["points"] = 5
print (alien_0)

alien_0 = {"color" : "green"}
print ("the alien is " + alien_0["color"] + ".")
alien_0 = {"color" : "yellow"}
print ("The alien color now is " + alien_0 ["color"] + ".")

print ("\n")

alien_0 = {"x_position" : 0, "y_position" : 25, "speed" : "medium"}
print ("Original x-position: " + str (alien_0["x_position"]))

#Move the alien to the right
#determine how far to move the alien bases on its current speed.
if alien_0 ["speed"] == "slow":
    x_increment = 1
elif alien_0 ["speed"] == "medium":
    x_increment = 2
else: #this must be a fast alien
    x_increment = 3
#the new position is the old position plus the increment.
alien_0["x_position"] = alien_0 ["x_position"] + x_increment
print ("New x-position: " + str (alien_0["x_position"]))

print ("\n")
alien_0 ={"color":"green","points":"5"}
print (alien_0)

del alien_0["points"]
print (alien_0)
