import itertools
from math import perm

bienvenida = input("""Seleccione que probabilidad desea calcular: Ganar Loteria (l), Lanzamiento dados (d), Lanzamiento monedas (m), Probabilidad general (g):""").lower()
if bienvenida == "l":
    n1 = input("Ingrese la cantidad total de números en el cartón: ")
    n2 = input("Ingrese la cantidad de números que debe elegir: ")
    n1 = int(n1)
    n2 = int(n2)
    n2 = n1 - n2
    n2 = perm(n2)
    n1 = perm(n1)
    division = n2 / n1
    probabilidad = division * 100
    mensaje = f"La probabilidad de ganar es: {probabilidad}%"
    print(mensaje)

elif bienvenida == "d":
    def calcular_probabilidad(dados, objetivo):
        resultados_posibles = list(itertools.product(range(1, 7), repeat=dados))
        ocurrencias_objetivo = sum(1 for resultado in resultados_posibles if sum(resultado) == objetivo)
        probabilidad = ocurrencias_objetivo / len(resultados_posibles)
        return probabilidad
    dados = int(input("Ingrese la cantidad de dados: "))
    objetivo = int(input("Ingrese el número objetivo: "))
    probabilidad = calcular_probabilidad(dados, objetivo)
    print(f"La probabilidad de obtener {objetivo} en {dados} dados es: {probabilidad:.2%}")

elif bienvenida == "m":
    cara_o_sello = input("¿Cara (c) o sello (s)?").lower()
    n1 = input("Ingresa la cantidad de lanzamientos: ")
    n1 = int(n1)
    casos_totales = 2 ** n1
    moneda = 1 / casos_totales * 100
    print(f"La probabilidad de {cara_o_sello} ocurra {n1} veces seguidas es de: {moneda} %.")

elif bienvenida == "g":
    suceso = input("¿Que suceso quieres que ocurra?")
    n1 = input("Ingresa numero total de soluciones posibles:")
    n2 = input("Ingresa numero de casos favorables totales:")
    n1 = int(n1)
    n2 = int(n2)
    division = n2 / n1
    probabilidad = division * 100
    mensaje = f"La probabilidad de {suceso} ocurra es de: {probabilidad} %."
    print(mensaje)

else:
    print("Escala incorrecta")