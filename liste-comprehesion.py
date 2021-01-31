#!/usr/bin/python3



liste = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] # long
liste = [i for i in range(10)] # short 
print(liste) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]




maliste = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
pairs=[]
for i in maliste:
    if i % 2 ==0 :
        pairs.append(i)
   
# This code above is too long, we can use a faster way that way

pairs = [i for i in maliste if i % 2 ==0]
print(pairs)


# Multiply each element by ten 
maliste = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
doubleListe=[]
for i in maliste:
    doubleListe.append(i*10)

# This code above is too long, we can use a faster way that way
doubleListe=[i*10 for i in maliste]
print(doubleListe) # [0, 10, 20, 30, 40, 50, 60, 70, 80, 90]



maliste=[0, 1, 2, 3, 4] 
letters = ["A", "B",  "C"] 
maliste_letters=[]
for i in maliste:
    for j in letters:
        maliste_letters.append("{} {}".format(i,j))

# This code above is too long, we can use a faster way that way 

maliste_letters= ["{} {}".format(i,j) for i in maliste for j in letters ]

print(maliste_letters)# ['0 A', '0 B', '0 C', '1 A', '1 B', '1 C', '2 A', '2 B', '2 C', '3 A', '3 B', '3 C', '4 A', '4 B', '4 C']