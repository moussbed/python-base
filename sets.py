#!/usr/bin/python3

set_vide = {}
print(set_vide)

set_full = {"A", "B", "D", "K", "E", "A", "D"}
print(set_full)  # {'B', 'D', 'A', 'K', 'E'}  : doublon retirer

first_set = {"A", "B", "C", "D", "E", "A", "D", "I"}
second_set = {"T", "C", "A", "K"}

intersection = first_set.intersection(second_set)
print(intersection)  # {'A', 'C'}

difference = first_set.difference(second_set)
print(difference)  # {'D', 'I', 'E', 'B'}

union = first_set.union(second_set)
print(union)  # {'C', 'I', 'A', 'E', 'D', 'K', 'B', 'T'}

# remove, doesn't throws error if element not exist
first_set.discard("Z")
