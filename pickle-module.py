#!/usr/bin/python3

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



# deserialization 

input = open("output.pickle", "rb")

dictionnaire2= pickle.load(input)
print(dictionnaire2) # {'alias': 'moussbed', 'firstname': 'Bedril', 'town': 'Rose Hill'}

input.close()