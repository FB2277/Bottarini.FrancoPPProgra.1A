# Menu general:

from data_stark import *
from funciones_00 import *
import os

def menu_general():
    print(" ----------------- ")
    print("|  Menu genereral |")
    print("|1️⃣  Stark 00      |")
    print("|2️⃣  Stark 01      |")
    print("|5️⃣  salida        |")
    print(" ----------------- ")
    opcion = input("Ingrese opcion: ")
    return opcion


def menu_stark_00():
    print(" ------------------------------------------------------------------ ")
    print("|                          Menu Stark 00                           |")
    print("|1. Los nombres de todos los superheroes                           |")
    print("|2. Los nombres de todos los superheroes y su altura               |")
    print("|3. El nombre del superheroe mas alto                              |")
    print("|4. El nombre del superheroe mas bajo                              |")
    print("|5. Informar el promedio de las alturas de todos los superheroes   |")
    print("|6. Informar nombre del superheroe mas alto y mas bajo             |")
    print("|7. Informar cual es el mas liviano y cual es el mas pesado        |")
    print("|8. Volver al menu general                                         |")
    print(" ------------------------------------------------------------------ ")
    opcion = input("Ingrese opcion: ")
    return opcion


def menu_stark_01():
    print(" ---------------------------------------------------------------------------------- ")
    print("|                                Menu Stark 01                                       |")
    print("|1.  El nombre de los superheroes de genero M                                        |")
    print("|2.  El nombre de los superheroes de genero F                                        |")
    print("|3.  Informar el nombre del superheroe mas alto de genero M                          |")
    print("|4.  Informar el nombre del superheroe mas alto de genero F                          |")
    print("|5.  Informar el nombre del superheroe mas bajo de genero M                          |")
    print("|6.  Informar el nombre del superheroe mas bajo de genero F                          |")
    print("|7.  Informar el promedio de las alturas de los superheroes de genero M              |")
    print("|8.  Informar el promedio de las alturas de los superheroes de genero F              |")
    print("|9.  Informar el nombre de los superheroes de la opcion 3 a 6                        |")
    print("|10. Informar la cantidad de superheroes por cada tipo color de ojos                 |")
    print("|11. Informar la cantidad de superheroes por cada tipo color de pelo                 |")
    print("|12. Informar la cantidad de superheroes por cada tipo de inteligencia               |")
    print("|13. Listar todos los superhéroes agrupados por color de ojos                        |")
    print("|14. Listar todos los superhéroes agrupados por color de pelo                        |")
    print("|15. Listar todos los superhéroes agrupados por tipo de inteligencia                 |")
    print("|16. Volver al menu general                                                          |")
    print(" ------------------------------------------------------------------------------------ ")
    opcion = input("Ingrese una opcion: ")
    return opcion





