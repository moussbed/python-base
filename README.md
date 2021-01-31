%title: Python Scripting
%author: moussbed
%date: 20-01-2020
#  Python : Introduction

+- Tout script python commence avec le sha-bang

```shell script
  #!/usr/bin/python 
```
    

+- Pour avoir l'emplacement de l'executable de python 
   
   $ which python 


+- Pour executer un script python, on le lance sur terminal
   
   $ ./script.py
     

---
# Python : String 

+- entre double cote et simple cote

```python
  print("Hello World !")

```


+- sur plusieurs lignes triple simple  quotes ou trimple double quotes

```python
 print("""
         Salut 
         Moussakat
         Bedril
  """) 
```

--- 
# Pyhton : Les variables 

+- Les variables 
   
   +- Simplifie la maintenance 
   
   +- Meilleur comprehension 

   +- Sans dollar 

```python
  name= "Bedril"
  print("Bonjour " + name + "!!! " )

```


+- Plus lisible encore 

```python
  firstname = "Bedril"
  lastname= "Moussakat"
  
  phrase ="{} {} !!!".format(firstname,lastname)
  print(phrase)

```

+- Le typage 

```python
  name = "Bedril"
  print(type(name))

```

---
# Python : string complements

+- methodes 

```python
  name = "Bedril"
  print(name.lower()) # minuscule
  print(name.upper()) # majuscule

```

```python
  name="Moussbed Bedril"
  print(name.count("s")) # nombre d'occurence de la chaine 

```

```python
  name="Moussbed"
  print(name.find('M')) # return the first index

```

```python
  name = "Moussbed"
  print(name.replace("bed","akat")) # replacement

```

```python
  name = "moussbed"
  print(dir(name)) # renvoie les methodes et les attributs de la variable

```

```python
  print( help(str.lower) ) # documentation de la methode lower()

```

+- fonctions

```python
  name="moussbed"
  print( len(name) )  # renvoie le nombre de caracteres

```

---
# Python : string complements (suite)


+- initiation aux tableaux

```python
  name="Moussbed Bedril"
  print(name[0]) # renvoie M
  
```

```python
 name="Moussbed Bedril"
 print(name[0:5]) # substring inclus 5

```

```python
  name= "Moussakat bedril"
  print(name[0:]) # de 0 jusqu'a la fin 

```

```python
 name="Moussakat Bedril"
 print(name[0:3]) # de 0 jusqu'a 2 

```

```python
  name = "Moussakat Bedril"
  print(name[3:]) # de 3 jusqu'a la fin

```


```python
  name = "Moussakat Bedril"
  print(name[::-1]) # De 0 jusqu'a la fin et la fin jusqu'a -1, resultat : inverse la chaine 

```


---
# Python : les nombres 

+- avanatge : typage minimaliste

+- int 

```python
  num = 345

```

+- float 

```python
  num= 23.45

```

+- Operations

```python
 print(2+2)
 print(3/2)
 print(3//2) # partie entier du resultat de la division
 print(3**2) # puissance
 print(3%2)
 print(3*2+1)
 print(3*(2+1)) 

```

+- incrementation 

```python
 num=2
 num += 1
 num *=4

```

+- les fonctions 

```python
  abs(-2)
  round(3.14)
  round(3.14,1) # arrondie d'1 chiffre apres la virgule

```

+- comparaison 

```python
  print(3!=3)
  print(3==2)
  print(3 > 5 )

```

---
# Python : les nombres (suite)

+- caster 

```python
  number1 = "100"
  number2 = "200"
  print( int(number1) + int(number2))

```

---
# Python : Listes

+- instancier une liste 

```python
  liste = []
  liste = list() 
  liste = ["A","B", "C"]

```

+- principe 

```python
  liste = ["A", "B" , "C"]
  print( len(liste) )  
  print( liste[0])
  print( liste[-1] )
  print( liste[0:2])
  print( liste[0:])
  print( liste[::-1] )  
  
```

+- ajout en fin dans une liste 

```python
  liste.append("D")

```

+- insertion

```python
  liste.insert(1,"Z")
  
```
 
---
# Python : Listes (suite)

+- suppression

```python
  liste.remove("Z")

```

+- etendre ou fusionner

```python
  liste2= ['E','F']
  liste.extend(liste2)

```

+- Suppresion du dernier element : LIFO

```python
 liste.pop()

```

+- Inverser 

```python
 liste.reverse()

```

+- trier

```python
 liste.sort() # par ordre croissant 
 liste.sort(reverse=True) # par ordre decroissant
 
 liste2 = sorted(liste) # la fonction sorted renvoie une nouvelle liste sans changer le contexte : Immuabilite

```

+- min max sum 

```python
 minimum = min(liste)
 maximum = max(liste)

 liste3= [2,45,6,3,0]
 somme=sum(liste3)

```

+- index 

```python
 index = liste.index("A")

```

+- la presence 

```python
 condition = "A" in liste
 print(condition) # true

```

---
# Python : liste complements 

+- Parcourir d'une liste 

```python
  lettres = ["A","B","C","D","E"]

  for lettre in lettres:
      print(lettre)
```

+- Plus de precision

```python
 for index, valeur in enumerate(letters):
     print(index,valeur)
  
 for index, valeur in enumerate(letters, start=1): # on reindexe, le premier element va commencer a l'index 1
     print(index,valeur)
```

+- Jointure

```python
jointure=  ",".join(letters)

```

---
# Python : Tuples

+- liste immutables

+- plus rapide qu'une liste 

+- securise le contenu


+- initialiser un tuple vide 

```python
 mon_tuple_vide = () # tuple vide 
 mon_tuple_full = ("A","B","C", "D", "E") 

```

+- immuabilite 

```python
 mon_tuple_full[0] = "Z" # TypeError: 'tuple' object does not support item assignment
 mon_tuple.remove("A") # AttributeError: 'tuple' object has no attribute 'remove'

```
+- count , index 

```python
 occurence = mon_tuple_full.count("A")
 index = mon_tuple_full.index("A")

```

+- conditions

```python
  condition = "A" in mon_tuple_full
  print(condition) # true
 
```

---
# Python : Set 

+- liste sans ordre 

+- sans doublons 


+- Initialisation 

```python
 set_vide = {}
 set_vide = set()

 set_full = {"A" , "B" , "D" , "K" , "E", "A", "D"}
 print(set_full) # {'B', 'D', 'A', 'K', 'E'}  : doublon retirer 

```


+- intersection, difference , union 

```python
  intersection =first_set.intersection(second_set)
  print(intersection) # {'A', 'C'}

  difference=first_set.difference(second_set)
  print(difference) # {'D', 'I', 'E', 'B'}

  union = first_set.union(second_set)
  print(union) # {'C', 'I', 'A', 'E', 'D', 'K', 'B', 'T'}

```

 
+- Convert a list to a set 

```python
 mon_set = set(liste)

```


---
# Python : dictionnaire 

+- definit comme les sets : {}

+- prinicpe de clef-valeur 


+- initialisation 

```python
 dictionnaire = { "clef1" : "valeur1" , "clef2" : "valeur2"} 
 dictionnaire = {"clef1" : "valeur1" , "maliste" : ["valeur1" , "valeur2" , "valeur3"]} 

```

+- interrogation

```python
 valeur = dictionnaire["clef1"]

```

+- interrogation avec des clefs inexistantes

```python
 valeur =  dictionnaire.get("clef1") # return valeur1
 valeur =  dictionnaire.get("clef13") # return None

```

+- modification

```python
  dictionnaire["clef1"]="valeurchanged"
  dictionnaire.update({ "clef1" : "nvllevaleur1" , "clef2" : "nvllevaleur2"})

```

---
# Python : dictionnaire (suite)

+- suppression 

```python
  del dictionnaire["clef3"]

```

+- suppression avec utilisation 

```python
  deleted = dictionnaire.pop("clef3")
 
```


+- autes 

```python
 len(dictionnaire)
 dictionnaire.keys()
 dictionnaire.values()
 dictionnaire.items()

```

+- parcours 

```python
  for key, value in dictionnaire.items():
      print(key,value)
```


---
# Python : If condition 


+- if = condition 

+- principe 

```python
  if True:
     print("True")
  else:
     print("False")
```

+- comparaison

   +- egalite : ==
   +- superieur ou egale : >=
   +- inferieur ou egale : <=
   +- different : !=
   +- comparateur d'objects memoire : is 
   
+- sinon

```python
 if channel == "moussbed":
    print("moussbed channel")
 elif channel == "youtube":
    print("youtube channel")
 else:
    print("No channel")

```   

+- operateurs and / or / not

```python
active= True
if channel == "moussbed" and active:
   print("moussbed channel is activated")
elif not active:
   print("channel doesn't activated")
else:
   print("No channel")
```

--- 
# Python : If condition (suite)


+- principe du is 

```python
l1 = ["A", "B", "C"]
l2 = ["A", "B", "D"]

if l1==l2: 
   print("egalite")

if l1 is l2: 
   print("meme object")

```

+- Booleens 
  +- les valeurs possibles de la condition sont : 
      +- 0
      +- []
      +- {}
      +- ()
      +- None
      +- ""

```python
  condition = False

  if condition:
    print("Ca marche")
  else:
    print("Ca ne marche pas") 
```

```python
  liste=["A","B","C"]
  if liste:
    print("Full list")
  else:
    print("Empty list") 
```

---
# Python : boucle For 

+- parcourir une liste (fonctionne avec les string)

```python
  letters = ["A", "B" , "C"]
  for letter in letters:
    print(letter)

```

+- break : sortir de la bouble

```python
  for letter in letters
     if letter == "C":
        print(" Tu sors ...")
        break
     print(letter)     
```

+- continue : sauter l'itération  

```python
  for letter in letters
     if letter == "C":
        print(" Tu saute ...")
        continue
     print(letter)     
```

+- double iteration 

```python
 letters = ["A", "B", "C", "D"]
 numbers = [1,2,3]
 for letter in letters:
     for number in numbers:
         print(number, letter) 
 
```

+- double iteration avec range

```python
  letters = ["A", "B", "C", "D"]
  numbers = [1,2,3]
  for letter in letters:
     for number in range(4):
         print(number, letter) 

```

---
# Phyton : La boucle while 

+- while = tant que

```python
  x=0
  while x < 7 :
      print("moussbed")
      x +=1
```

+- while with continue

```python
  x=0
  while x < 7 :
      if x == 5:
         x += 1
         continue
      print("moussbed")
      x +=1

```

---
# Python : les fonctions 

+- objectifs? factoriser 

+- Éviter de refaire deux fois la meme chose 

+- meilleure maintenance 

+- principe

```python

  def mafonction():
      action

  # appel de la function
  mafonction() 
```

+- return 

```python

  def mafunction():
      return "moussbed"
  
  m = mafunction()

```

+- passer les variables 

```

 def mafunction(action,nom):
     return "{} {} !!!".format(action,nom)
 
 mafunction("briller", "moussbed)

```
---
# Python : les fonctions (Complement)


+- le paramètre args 

```python

  def mafunction(*args):
      liste = []
      for arg in args: 
          liste.append(arg)
      return liste

  mafunction("Moussakat", "Bedril", "Kagrav")

```


+- le paramètre kwargs : recuperer un dictionnaire

```python

   def mafunction(*args, **kwargs):
       liste = []
       for key, value in kwargs.items():
           liste.append( "{} => {} ".format(key,value) )
       return liste

   mafunction("Moussakat", "Bedril" , country="Cameroon", town="Douala", district="PK10")

``` 

-----
# Python : Les modules 

+- modules = organisation du code / partage

+- partage de variables et de fonctions

+- organisation

  +- mon_module.py

```shell script
  #!/usr/bin/python

  mavariable= "la variable du module"
  
  def mafunction(default=mavariable):
      return "La function du module renvoie {}".format(default) 


```
  +- main.py

```shell script

  #!/usr/bin/python
  import mon_module as mm
  # from mon_module import mafunction
  
  mavariable = "la variable du main"   

  print(mm.mafunction()) # La function du module renvoie la variable du module
  print(mm.mafunction(mavariable)) # La function du module renvoie la variable du main

  #print(mafunction())

```

---
# Python : le Path

+- binaire python 

  $ which python 
  or 
  $ which python3 

+- les librairies 

```python
  
 import sys 
 
 print(sys.path) # affiche toutes les librairies locales de python
 
```

---
# Pyhton : PIP

+- gestionnaire librairie de librairie/paquets


--- 

# Python : virtualEnv

+- Isolation

+- Installation 

   $ pip install virtualenv
   or
   $ python -m pip install virtualenv 

+- mise en place d'un project

   $ virtualenv monprojet 
   
+- utiliser 
   
   $ source monprojet/bin/activate
   or
   $ deactivate   
   
+- version de python 
  
   $ virtualenv --python /usr/bin/python3 monproject
   $ soure monproject/bin/activate
   $ python 
   

+- list des paquests presentent dans la machine ou environnement
   
   $ pip list   
   
+- utilisation des requirements/ freeze

   $ pip freeze --local > requirements.txt (environment 1)
   $ pip install -r requirements.txt (environment 2)
   

---
# Python : Slicing

+- Manipulation des liste 

+- principe [START, END, EVOl]

+- END exclut 
  
  +- a partir des index 
 
  +- positifs : on part du debut 
    
  +- negatifs : on part de la 
  
  +- exemple

```python
  maliste = [1, 3, 5, 6, 7, 4,0,12,9,8]
  maliste[2] # 5
  maliste[-2] # 9
  print(maliste[1:8:2]) # [3,6,4,12]

```    
  + reverse 
  
```python
   maliste[::-1] # [8,9,12,0,4,7,6,5,3,1]
```
  
  +- exemple url 
  
```python
  url= "moussakatbedril@yahoo.com"
  url[:16] # moussakatbedril

```  

```python
 index = url.index("@")
 url[:index] # moussakatbedril
```

---
# Pyhton : List Comprehension

+- Realisation des liste en format oneliners

+- Simplifie la construction des liste 

+- N'existe pas dans d'autre langages 


```python
 maliste = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] # long
 maliste = [i for i in range(10)] # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

```

```python
   # Pair list 
   maliste = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
   pairs=[]
   for i in maliste:
       if i % 2 ==0 :
          pairs.append(i)
   
   # This code above is too long, we can use a faster way that way
   pairs = [i for i in maliste if i % 2 ==0]
   
```

```python

  # Multiply each element by ten 
  maliste = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
  doubleListe=[]
  for i in maliste:
      doubleListe.append(i*10)

  # This code above is too long, we can use a faster way that way
  doubleListe=[i*10 for i in maliste] # [0, 10, 20, 30, 40, 50, 60, 70, 80, 90]
  
```


```python

# double parcours 
 maliste=[0, 1, 2, 3, 4] 
 letters = ["A", "B",  "C"] 
 maliste_letters=[]
 for i in maliste:
     for j in letters:
         maliste_letters.append("{} {}".format(i,j))

# This code above is too long, we can use a faster way that way 

  maliste_letters= ["{} {}".format(i,j) for i in maliste for j in letters ] 
# result
# ['0 A', '0 B', '0 C', '1 A', '1 B', '1 C', '2 A', '2 B', '2 C', '3 A', '3 B', '3 C', '4 A', '4 B', '4 C']

```

---
# Pyhton : module OS

+- Utilisation des fonctions du systeme d'exploitation

+- chargement et informations

```python

import os 
print(dir(os))
print(help(os.chmod))

# Repertoire courant 
print(os.getcwd())  # /Users/bedrilmoussakat/development/projects/scripts/python

# Change directory 
os.chdir("/Users/bedrilmoussakat/development/projects/scripts/") 
print(os.getcwd()) # /Users/bedrilmoussakat/development/projects/scripts

# list files or folders 
print(os.listdir()) # ['.DS_Store', 'python', 'awk', 'bash']


# create toto's folder 
#os.rmdir('toto')  # Suppression
os.mkdir('toto')
print(os.listdir()) # ['.DS_Store', 'python', 'awk', 'toto', 'bash']

# creation recursive
os.makedirs('tata/guide/java',exist_ok=True)
print(os.listdir('tata/guide')) # ['java']

# Rename
os.rename('toto', 'titi')
print(os.listdir()) # ['.DS_Store', 'python', 'awk', 'tata', 'bash', 'titi']


# information
print(os.stat('tata'))     
print(os.stat('tata').st_size) # 96 taille du fichier iu du dossier 

```

---
# Pyhton : module OS (Path)

+- Parcourir un repertoire (fichiers et repertoire) et afficher le contenu

```python
import os

os.walk('/tmp')

for chemin,repertoires,fichiers in os.walk('/tmp'):
    print(chemin,repertoires,fichiers)

```

+- Variables d'environnements

```python
   import os

   print(os.environ)
   print(os.environ.get('M2_HOME'))
   print(os.environ.get('HOME'))
```

+- Jointure avec ou sans slash

```python
  import os
  os.path.join('/Users/bedrilmoussakat', 'teste.txt')
  os.path.join('/Users/bedrilmoussakat/', 'teste.txt')

```

+- dirname, basename, split, splitext

```python
import os

print(os.path.dirname('/Users/bedrilmoussakat/teste.txt')) # /Users/bedrilmoussakat
print(os.path.basename('/Users/bedrilmoussakat/teste.txt')) # teste.txt
print(os.path.split('/Users/bedrilmoussakat/teste.txt')) # ('/Users/bedrilmoussakat', 'teste.txt')
print(os.path.splitext('/Users/bedrilmoussakat/teste.txt')) # ('/Users/bedrilmoussakat/teste', '.txt')

```

+-  condition

```python
import os
os.path.exists('/Users/bedrilmoussakat/teste.txt')
os.path.isdir('/Users/bedrilmoussakat/teste.txt')
os.path.isfile('/Users/bedrilmoussakat/teste.txt')
```
   
---
# Pyhton : Generators

+- Dans les fonctions et les iterations de résultats

+- La ou ca coince 

```python
   def mafunction(liste):
       maliste = [] # Creation d'une autre liste 
       for item in liste:
           maliste.append(" Hello {}".format(item))
       return maliste

   maliste = [i for i in range(10)]
   mafunction(maliste)

   # Rq : Retour d'une nouvelle liste recomposee , append 
```

+- Solution : mot cle yield > generator 

```python

 def mafunction(liste):
       for item in liste:
          yield " Hello number {}".format(item)
       
  maliste = [i for i in range(10)]
  print(mafunction(maliste)) # <generator object mafunction2 at 0x10b3d9190>
  
# Rq: attention aux performances ( meilleure si on ne repasse par une liste)

```

+- yield : coroutine ( routine : ensemble d'instructions concues pour effectuer une tâche récurrente)


+- comment parcours un generator 

```python
   result_generator= mafunction(maliste)
   next(result_generator) # Hello number 0
   next(result_generator) # Hello number 1
   ...
   next(result_genrator) # Hello number 9

```  
  
---
# Pyhton : Generators (suite)

+- recuperer l'integralite sans next ? (Revenir a une liste)

```python
   result = [i for i in mafunction(maliste)] 
   # or encore
   result = list(mafunction(maliste))

   # Rq : gros inconvenient car vous perdez les benefices des generators
```

+- on peut creer un generator 

```python
  generator_created = (i for i in range(10)) # utilisation des parentheses et non des crochets
  print(generator_created)
  #Rq : Le generator prend beaucoup place qu'une liste
  listeFormGenerator = list(generator_created)
  print(listeFormGenerator)

```
+- empreinte memoire 

```python
  import sys

  liste = [ "Hello double {} ".format(i**2) for i in range(10000)]
  print(sys.getsizeof(liste)) # 87616 en byte
      
  generator = ("Hello double {} ".format(i**2) for i in range(10000))
  print(sys.getsizeof(generator)) # 112 en byte

  # Si je reconverti ce generator en liste je perds l'interet du generator 
  generatorTolist= list(generator)
  print(sys.getsizeof(generatorTolist)) # 83104 en byte

```

---
# Pyhton : Decorator 

+- Decorer une fonction : etendre sans la modifier 

+- Eviter les duplications de code 

+- une fonction de fonction (.. pas tout a fait)

```python

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

```

---
# Pyhton : Click (Introduction et CLI [SYSADMIN]) 

+- module click

+- installation 

$ pip3 install  click

+- specifique au CLI(Command line interface)

+- parsing des arguments et des options 

+- passage de fichiers 

+- edition d'aide

+- mise en place de l'environnement

+- Le project est videocli (virtualenv)

+- Utilisation
```python
   import click
   
   @click.command()
   def cli():
       print('Hello world')
```
+- utiliser le decorator click.command() pour activer le CLI
   $ ./video.py --help
   -> en sortie
```
   Usage: video.py [OPTIONS]
   
     DESCRIPTION DE NOTRE SCRIPT
   
   Options:
     --help  Show this message and exit.

```

---
# Pyhton : Click  (Introduction et CLI [SYSADMIN]) (suite1)


+- passer les arguments 

```python
  import click
   
   @click.command()
   @click.argument("name",default="moussbed")
   def cli(name):
       print("Hello {}".format(name))   
   # ./video.py bedril
```

+- passer les options 

```python
  import click
   
   @click.command()
   @click.option("--name",default="moussbed", help="Nom de l'utisateur")
   def cli(name):
       print("Hello {}".format(name))   
   # ./video.py --name bedril
```

+- prompt 

```python
  import click
   
   @click.command()
   @click.option("--name",prompt="A quelle personne ?", help="A quelle personne dire bonjour ?")
   def cli(name):
       print("Hello {}".format(name))   
   # $ ./video.py --name 
   # $ A quelle personne ? : 
```

+-  affichage

```python
   @click.command()
   @click.option("--name",prompt="A quelle personne ?", help="A quelle personne dire bonjour ?")
   def cli(name):
        click.echo(f"Hello {name}") # click.echo instead print

```
+- click.secho

```python
   @click.command()
   @click.option("--name",prompt="A quelle personne ?", help="A quelle personne dire bonjour ?")
   def cli(name):
        # affichage en couleur rouge et en gras
        click.secho(f"Hello {name} votre identifiant est {id} et votre age {age}", fg="red" , bold=True)
        
```

---
# Pyhton : Click  (Introduction et CLI [SYSADMIN]) (suite2)

+- positionnement de flag

```python
 @click.command() # active le CLI : ./video.py --help 
 @click.argument("name", default="moussbed") # passer les arguments : ./video.py  bedril
 @click.option("--id", default="000123444", help="Idenfiant de l'utilisateur ") # passer les options: ./video.py  --id 5555555
 @click.option("--age", prompt="Quel age a t-il ?", help="Definir l'age de l'utilisateur") # utilisation du prompt pour renseigner l'age
 @click.option("--fr", "-f", is_flag=True, help="Langue francaise") # ./video.py bedril --id 55555 --fr (sortie en francais) ou ./video.py bedril --id 55555 (sortie en anglais)
 def cli(name,id,age,fr):
     """
       DESCRIPTION DE NOTRE SCRIPT
     """ 
     #print("Hello {} votre identifiant est {} et votre age {}".format(name,id,age))
     #click.echo(f"Hello {name} votre identifiant est {id} et votre age {age}")
     if fr:
          click.secho(f"Bonjour {name} votre identifiant est {id} et votre age {age}", fg='red' , bold=True) # affichage en couleur rouge et en gras
     else :
          click.secho(f"Hello {name} your identifier is {id} and age {age}", fg='red' , bold=True) # affichage en couleur rouge et en gras

 if __name__ == '__main__':
    cli()

```

+- passer un tuple

```python
   @click.command()
   @click.option("--data", required=True, type=(str,int))
   def cli2(data):
       
       click.echo(f" {data[0]} -- {data[1]} ")
   
# $ ./video.py Bedril 12

```

+- passer une liste 

```python
   @click.command()
   @click.option("--names", "-n", multiple=True)
   def cli3(names):
       """
        DESCRIPTION DU SCRIPT
       """
       for name in names:
          click.echo(f" Hello {name} ")  
  
```

---
# Pyhton : Click  (Introduction et CLI [SYSADMIN]) (suite3)

+- passer un fichier 

```python
 @click.command()
 @click.argument("file_name", type=click.File('r'))
 def cli4(file_name):
    """
     DESCRIPTION DU SCRIPT
    """
    count=0
    for line in file_name:
        count += 1
        click.echo(f" {count} {line} ")   
 # $ ./video.py names.txt
```

---
# Pyhton : Pickle

+- serialisation/deserialisation = Python objects > binaire | binaire > python object

+- objects: class , liste , dictionnaire ...

+- compresser

+- serialization 

```python
  import pickle
  # Serialiation 
  dictionnaire = {
     "alias" : "moussbed",
     "firstname" : "Bedril",
     "town" : "Rose Hill"
  }
  output = open("output.pickle", "wb")
  pickle.dump(dictionnaire,output)
  output.close()
```

+- deserialisation

```python
 # deserialization 
 
 input = open("output.pickle", "rb")
 
 dictionnaire2= pickle.load(input)
 print(dictionnaire2) # {'alias': 'moussbed', 'firstname': 'Bedril', 'town': 'Rose Hill'}
 
 input.close()
```

