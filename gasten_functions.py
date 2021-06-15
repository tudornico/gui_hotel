#function that adds guest to the guest list
def add_gast(gasten,gast):
    gasten.append(gast)
    return gasten
#we change the  last name of a guest
def lastname(person):
    x=name.split(person)
    return x

def change_lastname(person,new_name):
    x=[" "]
    x=name.split(person)
    x=new_name
    return person

#delete a guest from the hotel
def delete_guest(gasten,person):
    gasten.remove(person)
    return gasten