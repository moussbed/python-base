#!/usr/bin/python3
import mon_module as mm 
# from mon_module import mafunction
import sys

print(sys.path)

mavariable = "variable du main"   

print(mm.mafunction())
print(mm.mafunction(mavariable))

#print(mafunction())

maliste = [1, 3, 5, 6, 7, 4,0,12,9,8]
print(maliste[1:8:2]) # [3,6,4,12]
print(maliste)
