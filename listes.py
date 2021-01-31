#!/usr/bin/python3

liste = list()  # liste = []

print(liste)  # []

liste = ["Bedril", "Moussakat", "Moussbed", "Kabane", "Sidoine"]

print(liste)  # ['Bedril', 'Moussakat', 'Moussbed', 'Kabane', 'Sidoine']

print(liste[0])  # Bedril

print(liste[0:3])  # ['Bedril', 'Moussakat', 'Moussbed']

print(liste[-1])  # Sidoine

print(liste[::-1])  # ['Sidoine', 'Kabane', 'Moussbed', 'Moussakat', 'Bedril']

liste.append("Yvonne")
print(liste)  # ['Bedril', 'Moussakat', 'Moussbed', 'Kabane', 'Sidoine', 'Yvonne']

liste.insert(1, "Tamo")
print(liste)  # ['Bedril', 'Tamo', 'Moussakat', 'Moussbed', 'Kabane', 'Sidoine', 'Yvonne']

liste.remove("Tamo")
print(liste)  # ['Bedril', 'Moussakat', 'Moussbed', 'Kabane', 'Sidoine', 'Yvonne']

liste2 = ["Henry", "Francis"]
liste.extend(liste2)
print(liste)  # ['Bedril', 'Moussakat', 'Moussbed', 'Kabane', 'Sidoine', 'Yvonne', 'Henry', 'Francis']

last_in = liste.pop()
print(last_in)  # Francis
print(liste)  # ['Bedril', 'Moussakat', 'Moussbed', 'Kabane', 'Sidoine', 'Yvonne', 'Henry']

liste.reverse()
print(liste)  # ['Henry', 'Yvonne', 'Sidoine', 'Kabane', 'Moussbed', 'Moussakat', 'Bedril']

liste.sort()
print(liste)  # ['Bedril', 'Henry', 'Kabane', 'Moussakat', 'Moussbed', 'Sidoine', 'Yvonne']

liste.sort(reverse=True)
print(liste)

liste3 = sorted(liste)
print(liste)  # ['Yvonne', 'Sidoine', 'Moussbed', 'Moussakat', 'Kabane', 'Henry', 'Bedril']
print(liste3)  # ['Bedril', 'Henry', 'Kabane', 'Moussakat', 'Moussbed', 'Sidoine', 'Yvonne']

minimun = min(liste)
print(minimun)  # Bedril

maximum = max(liste)
print(maximum)  # Yvonne

liste4 = [1, 20, 5, 45]
somme = sum(liste4)
print(somme)  # 71

print(liste.index("Yvonne"))

condition = "Yvonne" in liste

print(condition)  # true

# Parcours d'une liste 

for l in liste:
    print(l)

# Avec plus de precision 

letters = ["A", "B", "C", "D", "E"]

for index, valeur in enumerate(letters):
    print(index, valeur)

for index, valeur in enumerate(letters, start=1):
    print(index, valeur)

# Jointure 

jointure = ",".join(letters)
print(jointure)
