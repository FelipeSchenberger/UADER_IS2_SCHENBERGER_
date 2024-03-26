#!/usr/bin/python
#*-------------------------------------------------------------------------*
#* factorial.py                                                            *
#* calcula el factorial de un número                                       *
#* Dr.P.E.Colla (c) 2022                                                   *
#* Creative commons                                                        *
#*-------------------------------------------------------------------------*
import sys

# Función para calcular el factorial de un número
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

# Función para calcular y mostrar los factoriales dentro de un rango dado
def calculate_factorials(start, end):
    for num in range(start, end + 1):
        print("Factorial de", num, "! es", factorial(num))

# Función para solicitar al usuario el rango de números
def get_range_from_user():
    start = int(input("Por favor, ingresa el número inicial del rango: "))
    end = int(input("Por favor, ingresa el número final del rango: "))
    return start, end

# Verifica si se proporcionaron argumentos de línea de comandos
if len(sys.argv) == 1:
    # Si no se proporcionaron argumentos, solicita al usuario el rango
    start, end = get_range_from_user()
else:
    # Si se proporcionaron argumentos, verifica el formato y extrae los números del rango
    if "-" in sys.argv[1]:
        if sys.argv[1].startswith("-"):
            # Si el rango es "-hasta", el inicio es 1 y el final es el número indicado
            start = 1
            end = int(sys.argv[1][1:])
        elif sys.argv[1].endswith("-"):
            # Si el rango es "desde-", el inicio es el número indicado y el final es 60
            start = int(sys.argv[1][:-1])
            end = 60
        else:
            # Si el rango es "desde-hasta", extrae los números de inicio y fin
            start, end = map(int, sys.argv[1].split("-"))
    else:
        # Si el formato del rango es incorrecto, muestra un mensaje de error
        print("Formato de rango incorrecto. Por favor usa el formato 'desde-hasta', '-hasta' o 'desde-'.")
        sys.exit()

# Calcula y muestra los factoriales dentro del rango dado
calculate_factorials(start, end)
