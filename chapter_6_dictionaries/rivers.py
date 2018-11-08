rivers= {
    "Nile River": "North-East Africa",
    "Amazon River" : "South America",
    "Yangtze River" : "China",
    "Yenisei River" : "flows mainly in Russia"
    }
for river, country in rivers.items():
    print ("The " + river.title() + " through " + country.title())
print ("\n")

for river in rivers.keys():
    print (river.title())
print ("\n")
    
for country in rivers.values():
    print (country.title())
    
