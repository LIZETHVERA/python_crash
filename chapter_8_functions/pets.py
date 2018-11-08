def describe_pet (animal_type, pet_name):
    """Display informaction about a pet"""
    print ("\nI have a " + animal_type + ".")
    print ("My " + animal_type + "'s name is " + pet_name.title() + ".")
describe_pet ("hamster","harry")

def describe_pet (animal_type, pet_name):
    """Display informaction about a pet"""
    print ("\nI have a " + animal_type + ".")
    print ("My " + animal_type + "'s name is " + pet_name.title() + ".")
describe_pet (animal_type ="hamster",pet_name="harry")


def describe_pet (pet_name,animal_type = "dog",):
    """Display informaction about a pet"""
    print ("\nI have a " + animal_type + ".")
    print ("My " + animal_type + "'s name is " + pet_name.title() + ".")
    
describe_pet (pet_name="willie")
#describe_pet (willie") --> Esta forma tambièn estarìa correcta.

