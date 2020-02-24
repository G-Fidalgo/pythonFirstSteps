# coding=utf-8
import random

tabla2D = []

tablaUsados = []


def checkNum(number):
    if number in tablaUsados:
        print(tablaUsados)
        print("El numero ", str(number) + " ya esta en la tabla")
        True
    else:
        print("El numero ", str(number) + " se ha metido enla tabla")
        tablaUsados.append(number)
        False


def randomNum():
    x = random.randint(0, 50)
    if checkNum(x):
        randomNum()
    else:
        return x


def generarFila():
    fila = []
    for _ in range(6):
        numberToAppend = randomNum()
        fila.append(numberToAppend)
    return fila


for _ in range(2):
    tabla2D.append(generarFila())

print(tabla2D)
