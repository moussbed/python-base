#!/usr/bin/python

letters = ["A", "B", "C", "D"]

for letter in letters:
    if letter == "C":
        print("Tu sors ...")
        break
    print(letter)

for letter in letters:
    if letter == "C":
        print("Tu saute ...")
        continue
    print(letter)


numbers = [1, 2, 3]
for letter in letters:
    for number in numbers:
        print(number, letter)

for letter in letters:
    for number in range(4):
        print(number, letter)
