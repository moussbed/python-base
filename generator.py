#!/usr/bin/python3

maliste = [i for i in range(10)]

def mafunction(liste):
    maliste = [] # Creation d'une autre liste 
    for item in liste:
        maliste.append(" Hello number {}".format(item))
    return maliste

print(mafunction(maliste)) # [' Hello 0', ' Hello 1', ' Hello 2', ' Hello 3', ' Hello 4', ' Hello 5', ' Hello 6', ' Hello 7', ' Hello 8', ' Hello 9']

# Utilisation d'un generator
def mafunction2(liste):
    for item in liste:
        yield " Hello number {}".format(item)
       
print(mafunction2(maliste)) # <generator object mafunction2 at 0x10b3d9190>

# Parcours d'un generator
result_generator=mafunction2(maliste)
print(next(result_generator)) # Hello number 0
print(next(result_generator)) # Hello number 1
print(next(result_generator)) # Hello number 3


# recuperer l'integralite sans next ?
liste= [i for i in mafunction2(maliste)] # liste = list(mafunction2(maliste))

print(liste) # [' Hello number 0', ' Hello number 1', ' Hello number 2', ' Hello number 3', ' Hello number 4', ' Hello number 5', ' Hello number 6', ' Hello number 7', ' Hello number 8', ' Hello number 9']


# on peut creer un generator 

generator_created = (i for i in range(10)) # utilisation des parentheses et non des crochets
print(generator_created) # <generator object <genexpr> at 0x10e338200>

listeFormGenerator = list(generator_created)
print(listeFormGenerator) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


# Empreinte memoire
import sys

liste = [ "Hello double {} ".format(i**2) for i in range(10000)]
print(sys.getsizeof(liste)) # 87616
      
generator = ("Hello double {} ".format(i**2) for i in range(10000))
print(sys.getsizeof(generator)) # 112

# Si je reconverti ce generator en liste je perds l'interet du generator 
generatorTolist= list(generator)
print(sys.getsizeof(generatorTolist)) # 83104