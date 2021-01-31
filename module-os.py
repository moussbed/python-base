#!/usr/bin/python3

import os 

import datetime

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

print(os.stat('tata')) #s.stat_result(st_mode=16877, st_ino=7557194, st_dev=16777221, st_nlink=3, st_uid=501, st_gid=20, st_size=96, st_atime=1611514913, st_mtime=1611514713, st_ctime=1611514713)      

print(os.stat('tata').st_size)# 96

dateModifiedTimeStamp= os.stat('tata').st_mtime
print(datetime.datetime.fromtimestamp(dateModifiedTimeStamp)) # 2021-01-24 22:58:33.248134


#Parcourir un repertoire (fichiers et repertoire) et afficher le contenu

for chemin,repertoires,fichiers in os.walk('/tmp'):
    print(chemin,repertoires,fichiers)


# Variable d'environnement

print(os.environ)
print(os.environ.get('HOME'))


# Jointure avec ou sans slash

os.path.join('/Users/bedrilmoussakat', 'teste.txt')
os.path.join('/Users/bedrilmoussakat/', 'teste.txt')
os.chdir("/Users/bedrilmoussakat") 
print(os.listdir())

# dirname, basename, split, splitext

print(os.path.dirname('/Users/bedrilmoussakat/teste.txt')) # /Users/bedrilmoussakat
print(os.path.basename('/Users/bedrilmoussakat/teste.txt')) # teste.txt
print(os.path.split('/Users/bedrilmoussakat/teste.txt')) # ('/Users/bedrilmoussakat', 'teste.txt')
print(os.path.splitext('/Users/bedrilmoussakat/teste.txt')) # ('/Users/bedrilmoussakat/teste', '.txt')

# Condition

os.path.exists('/Users/bedrilmoussakat/teste.txt')
os.path.isdir('/Users/bedrilmoussakat/teste.txt')
os.path.isfile('/Users/bedrilmoussakat/teste.txt')