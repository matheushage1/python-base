#!/usr/bin/python3

"Criando uma tabuda bem simples"

__version__ = "0.1.0"
__author__ = "Matheus Hage"

numbers = list(range(0, 11))

print(numbers)

# Iterable (objetos percorríveis)

for number in numbers:
    print("Tabuada do", number)
    for other_number in numbers:
        print(number * other_number)
    print("-------------------")