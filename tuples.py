#!/usr/bin/python3

mon_tuple_vide = tuple()
print(mon_tuple_vide)

mon_tuple_full = ("A", "B", "C", "D")
print(mon_tuple_full)  # ('A', 'B', 'C', 'D')

# mon_tuple_vide[0]="Z"
print(mon_tuple_full)

# mon_tuple_full.remove("A")

mon_tuple_full.count("A")

condition = "A" in mon_tuple_full
