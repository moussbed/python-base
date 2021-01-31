#!/usr/bin/python3

dictionnaire = { "clef1" : "valeur1", "clef2" : "valeur2", "maliste" : ["valeur1","valeur2", "valeur3"]}
print(dictionnaire) # {'clef1': 'valeur1', 'clef2': 'valeur2'}

print(dictionnaire["clef1"]) # return valeur1
#print(dictionnaire["clef13"]) # KeyError: 'clef13'

print(dictionnaire["clef1"])  # return valeur1
print(dictionnaire.get("clef13")) # return None

dictionnaire["clef3"]="valeur3"
print(dictionnaire) # {'clef1': 'valeur1', 'clef2': 'valeur2', 'maliste': ['valeur1', 'valeur2', 'valeur3'], 'clef3': 'valeur3'}

dictionnaire.update({ "clef1" : "nvllevaleur1" , "clef2" : "nvllevaleur2"})
print(dictionnaire) # {'clef1': 'nvllevaleur1', 'clef2': 'nvllevaleur2', 'maliste': ['valeur1', 'valeur2', 'valeur3'], 'clef3': 'valeur3'}


del dictionnaire["clef2"]
print(dictionnaire) # {'clef1': 'nvllevaleur1', 'maliste': ['valeur1', 'valeur2', 'valeur3'], 'clef3': 'valeur3'}


deleted = dictionnaire.pop("maliste")
print(deleted) # ['valeur1', 'valeur2', 'valeur3']
print(dictionnaire) # {'clef1': 'nvllevaleur1', 'clef3': 'valeur3'}


print(len(dictionnaire))# 2
keys = dictionnaire.keys()
print(keys) # dict_keys(['clef1', 'clef3'])

values = dictionnaire.values()
print(values) # dict_values(['nvllevaleur1', 'valeur3'])

items = dictionnaire.items()
print(items) # dict_items([('clef1', 'nvllevaleur1'), ('clef3', 'valeur3')])


for key, value in dictionnaire.items():

     print(key,value)
