#!/usr/bin/python3

num_int = 4
num_float = 45.34

print(type(num_int))  # <class 'int'>

print(type(num_float))  # <class 'float'>

# Operations
print(2 + 2)  # 4
print(3 / 2)  # 1.5
print(3 // 2)  # 1
print(3 ** 2)  # 9 : puissance
print(3 % 2)  # 1
print(3 * 2 + 1)  # 7
print(3 * (2 + 1))  # 9

# incrementation

number = 1
number += 1
print(number)  # 2

# functions

print(abs(-4))  # 4
print(round(3.7))  # 4
print(round(3.23, 2))  # 3.23 : arrondie de 2 chiffre apres la virgule
print(round(-3.37, 1))  # -3.4 : arrondie d' 1 chiffre apres la virgule

# comparaison

print(3 == 2)
print(2 != 3)

# caster

number1 = "100"
number2 = "200"

print(number1 + number2)  # 100200
print(int(number1) + int(number2))  # 300
