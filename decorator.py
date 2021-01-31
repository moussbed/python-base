#!/usr/bin/python3


def mafunction():
    
    return " Hello moussbed"

# Nous voulons ajouter un mesage a cette fonction avant le retour 
# Solution 1 : ajouter le message a l'interieur de la function

def mafunction2():
    print("Message :")
    return "Hello moussbed"

# Solution 2 : solution 1 n'est pas une bonne pratique selon le Open/Close de SOLID, utilisons donc le Decorator pour resoudre

def dec(fonction):
    print("Message :")
    return fonction

@dec
def onefunction():
    return "Hello moussbed"

print(onefunction())    