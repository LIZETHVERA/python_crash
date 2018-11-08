glossary2 = {
    "list" : "a data structure that is a mutable",
    "tuple" : "is a sequence of immutable objects",
    "dictionary": "maps a set of objects (keys) to another set of objects (values)",
    "loop": "is a sequence of instruction s that is continually repeated until a certain condition is reached",
    }
for glossary, meaning in glossary2.items():
    print (glossary.title() + " : " + meaning + ".")

