#!/usr/bin/python
#*-------------------------------------------------------------------------*
#* factorial.py                                                            *
#* calcula el factorial de un número                                       *
#* Dr.P.E.Colla (c) 2022                                                   *
#* Creative commons                                                        *
#*-------------------------------------------------------------------------*
import sys

def factorial(num): 
    if num < 0: 
        print("Factorial de un número negativo no existe")
        return None
    elif num == 0: 
        return 1
    else: 
        fact = 1
        while(num > 1): 
            fact *= num 
            num -= 1
        return fact 

def calculate_factorials(start, end):
    for num in range(start, end + 1):
        print("Factorial de", num, "! es", factorial(num))

def get_range_from_user():
    start = int(input("Por favor, ingresa el número inicial del rango: "))
    end = int(input("Por favor, ingresa el número final del rango: "))
    return start, end

if len(sys.argv) == 1:
    start, end = get_range_from_user()
else:
    if "-" in sys.argv[1]:
        if sys.argv[1].startswith("-"):
            start = 1
            end = int(sys.argv[1][1:])
        elif sys.argv[1].endswith("-"):
            start = int(sys.argv[1][:-1])
            end = 60
        else:
            start, end = map(int, sys.argv[1].split("-"))
    else:
        print("Formato de rango incorrecto. Por favor usa el formato 'desde-hasta', '-hasta' o 'desde-'.")
        sys.exit()

calculate_factorials(start, end)
