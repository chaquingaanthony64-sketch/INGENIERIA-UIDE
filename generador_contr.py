import random

longitud = int(input("Ingrese la longitud de la contraseña: "))
caracteres = ""

mayusculas = input("¿Desea usar mayúsculas? (si/no): ")
if mayusculas == "si":
    caracteres = caracteres + "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

minusculas = input("¿Desea usar minúsculas? (si/no): ")
if minusculas == "si":
    caracteres = caracteres + "abcdefghijklmnopqrstuvwxyz"

numeros = input("¿Desea usar números? (si/no): ")
if numeros == "si":
    caracteres = caracteres + "1234567890"

simbolos = input("¿Desea usar símbolos? (si/no): ")
if simbolos == "si":
    caracteres = caracteres + "@#$%&*"
