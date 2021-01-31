#!/usr/bin/python3

if True:
    print("True")
else:
    print("False")

channel = "moussbed"

if channel == "moussbed":
    print("moussbed channel")
elif channel == "youtube":
    print("youtube channel")
else:
    print("No channel")

active = True
if channel == "moussbed" and active:
    print("moussbed channel is activated")
elif not active:
    print("channel doesn't activated")
else:
    print("No channel")

# Principe du is

l1 = ["A", "B", "C"]
l2 = ["A", "B", "C"]

if l1 == l2:
    print("Egalite")

if l1 is l2:
    print("Meme object")

# boolean

condition = False

if condition:
    print("Ca marche")
else:
    print("Ca ne marche pas")

if l1:
    print("Full list")
else:
    print("Empty list")
