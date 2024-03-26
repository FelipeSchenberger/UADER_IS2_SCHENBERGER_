#!/usr/bin/python
#*-------------------------------------------------------------------------*
#* factorial_OOP.py                                                        *
#* Calcula el factorial de un número mediante programación orientada a     *
#* objetos.                                                                 *
#* Dr.P.E.Colla (c) 2022                                                   *
#* Creative Commons                                                        *
#*-------------------------------------------------------------------------*
class Factorial:
    def init(self):
        pass

    def calcular_factorial(self, num):
        if num < 0:
            print("Factorial de un número negativo no existe")
            return None
        elif num == 0:
            return 1
        else:
            fact = 1
            while num > 1:
                fact *= num
                num -= 1
            return fact

    def run(self, min_num, max_num):
        resultados = {}
        for num in range(min_num, max_num + 1):
            resultados[num] = self.calcular_factorial(num)
        return resultados

#Ejemplo de uso:
factorial_calculator = Factorial()
resultados = factorial_calculator.run(5, 8)
for num, factorial in resultados.items():
    print(f"El factorial de {num} es {factorial}")
