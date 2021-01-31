#!/usr/bin/python3


def mafunction():
    print("Hello moussbed")

mafunction()


def mafunction2():
    return "moussbed"


m = mafunction2()
phrase = "Hello  {} ".format(m)
print()    


def mafunction(action,nom):
     return "{} {} !!! ".format(action,nom)
 
print(mafunction("briller", "moussbed"))


def mafunction(*args):
      liste = []
      for arg in args: 
          liste.append(arg)
      return liste

print(mafunction("Amina", "Tamo", "Rita"))


def function(*args, **kwargs):
       liste = []
       for key, value in kwargs.items():
           liste.append( "{} => {} ".format(key,value) )
       return liste

   
print(function("Moussakat", "Bedril" , country="Cameroon", town="Douala", district="PK10")) # ['country => Cameroon ', 'town => Douala ', 'district => PK10 ']