#!/usr/bin/python3

# Affichage sur une ligne 
print("Hello World !")

# Affichage sur plusieurs lignes
print("""
     Bonjour 

     Mr Mousssakat
     Bedril
""")

name = "Moussbed Bedril"

print(name.lower())  # lowercase

print(name.upper())  # uppercase

print(name.count("s"))  # The presence of Characters's number , in this case we have 2 occurences of s

print(name.replace("bed", "akat"))  # Replacement

print(name.find("M"))  # return of the index of the string found

print(dir(name))  # return the methodes and attributs of the variable

print(name.__eq__("Bedril"))  # check equality

print(name.__contains__("Bedril"))  # check

print(help(str.lower))  # Give the documentation of lower method

print(len(name))  # return number of characters

print(name[0])  # retrun M

print(name[0:5])  # substring exclude 5, return Mouss

print(name[0:])  # de 0 jusqu'a la fin , return Moussbed Bedril

print(name[9:])  # de 3 jusqu'a la fin , return Bedril

print(name[:])  # de 0 jusqu'a la fin , return Moussbed Bedril

print(name[::-1])  # de 0 jusqu'a la fin et de la fin jusqu'a -1 , return lirdeB debssuoM  : inversion de la chaine
