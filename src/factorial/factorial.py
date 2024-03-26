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

if len(sys.argv) == 1:
    range_input = input("Por favor, ingresa el rango (desde-hasta) para calcular los factoriales: ")
    start, end = map(int, range_input.split("-"))
else:
    start, end = map(int, sys.argv[1].split("-"))

calculate_factorials(start, end)
