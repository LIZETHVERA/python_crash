guest_list = ["Ana","Pedro","Lucia"]
print (guest_list [0] +" " + "You are invited to join us for dinner.")
print (guest_list [1] +" " + "You are invited to join us for dinner.")
print (guest_list [2] +" " + "You are invited to join us for dinner.")

popped_cantmake = guest_list.pop(1) # pedro no podrá ir 
print (popped_cantmake)

guest_list.append ("Sofia")
print (guest_list)
print (guest_list [0] +" " + "You are invited to join us for dinner.")
print (guest_list [1] +" " + "You are invited to join us for dinner.")
print (guest_list [2] +" " + "You are invited to join us for dinner.")

guest_list.insert(0,"Paola")
guest_list.insert(2,"Juan")
guest_list.append ("María")
print (guest_list)

print (guest_list [0] +" " + "You are invited to join us for dinner.")
print (guest_list [1] +" " + "You are invited to join us for dinner.")
print (guest_list [2] +" " + "You are invited to join us for dinner.")
print (guest_list [3] +" " + "You are invited to join us for dinner.")
print (guest_list [4] +" " + "You are invited to join us for dinner.")
print (guest_list [5] +" " + "You are invited to join us for dinner.")

print ("Hello " + str (guest_list[0:]) + " I found a bigger dinner table, now we are six")

print (guest_list)

popped_guest1 = guest_list.pop(0) # Solo podré invitar a 2 personas 
print ("Hi " + popped_guest1 + " I am sorry i can´t invited you, the restaurant canceled my table for 6")
popped_guest2 = guest_list.pop(1)
print ("Hi " + popped_guest2 + " I am sorry i can´t invited you, the restaurant canceled my table for 6")
popped_guest3 = guest_list.pop(2)
print ("Hi " + popped_guest3 + " I am sorry i can´t invited you, the restaurant canceled my table for 6")
popped_guest4 = guest_list.pop(1)
print ("Hi " + popped_guest4 + " I am sorry i can´t invited you, the restaurant canceled my table for 6")
print (guest_list)

print ("Hi " + guest_list[0] + " You are still invited")
print ("Hi " + guest_list[1] + " You are still invited")

del guest_list[:]
print (guest_list)


