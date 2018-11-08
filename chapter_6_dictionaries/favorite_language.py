favorite_languages = {
    "jen" : "python",
    "sarah" : "c",
    "edward" : "rubi",
    "phil" : "python",
    }
for name, language in favorite_languages.items():
    print (name.title() + "'s favorite language is " + language.title() + ".")
    
for name in favorite_languages.keys():
    print (name.title())

for name in favorite_languages:
    print (name.title())

print ("\n")
favorite_languages = {
    "jen" : "python",
    "sarah" : "c",
    "edward" : "rubi",
    "phil" : "python",
    }
friends = ["phil" , "sarah"]
for name in favorite_languages.keys():
    print (name.title())
    
    if name in friends:
        print ("HI " + name.title() + ", I see your favorite language is " + favorite_languages [name].title() + "!")
    if "erin" not in favorite_languages.keys():
        print ("Erin, please take our poll!")
        

print ("\n")
favorite_languages = {
    "jen" : "python",
    "sarah" : "c",
    "edward" : "rubi",
    "phil" : "python",
    }
    
for name in sorted (favorite_languages.keys()):
    print (name.title() + ", thank you for taking the poll.")


print ("\n")

favorite_languages = {
    "jen" : "python",
    "sarah" : "c",
    "edward" : "rubi",
    "phil" : "python",
    }
print ("The following languages have been mentioned:")
for language in favorite_languages.values():
    print (language.title())
    

print ("\n")

favorite_languages = {
    "jen" : "python",
    "sarah" : "c",
    "edward" : "rubi",
    "phil" : "python",
    }
print ("The following languages have been mentioned:")
for language in set (favorite_languages.values()):
    print (language.title())
    
