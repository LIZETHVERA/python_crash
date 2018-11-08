favorite_languages = {
    "jen" : "python",
    "Sarah" : "c",
    "edward" : "rubi",
    "phil" : "python",
    }
    
languages_poll = ["lia","eamon","laura","SARAH","sofia","phil"]

new_fl = [((name.lower(),language.lower()) for name , language in favorite_languages.items()]

for people in languages_poll: 
    if people.lower() in new_fl.keys():
        print (people.title() + " thank you for taking the poll")
    else:
        print (people.title() + " Please take the poll")

