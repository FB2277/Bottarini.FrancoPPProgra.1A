# Funciones del desafio 00:
from data_stark import *
from menu import *
import os

#B
def mostrar_nombres(lista):
    print("\n")
    for nombre in lista:
        print(nombre['nombre'])
    print("\n")


#C
def mostrar_nom_alt(lista):
    print("\n")
    for nombre_altura in lista:
        print(f"El nombre es: {nombre_altura['nombre']},   La altura es: {nombre_altura ['altura']}")
    print("\n")


#D
def heroe_mas_alto(lista):
    print("\n")
    bandera_mas_alto = True
    altura_mas_alta = 0
    for heroe in lista:
        altura = float(heroe['altura'])
        if bandera_mas_alto or altura > altura_mas_alta:
            bandera_mas_alto = False
            altura_mas_alta = altura
            super_heroe = heroe['nombre']
            el_heroe_mas_alto = super_heroe
    print(f"El superheroe mas alto es, {el_heroe_mas_alto} y su altura es, {altura_mas_alta}\n")


#E
def heroe_mas_bajo(lista):
    print("\n")
    bandera_mas_bajo = True
    altura_mas_baja = 0
    for heroe in lista:
        altura = float(heroe['altura'])
        if bandera_mas_bajo or  altura < altura_mas_baja:
            bandera_mas_bajo = False
            altura_mas_baja = altura
            super_heroe = heroe['nombre']
            el_heroe_mas_bajo = super_heroe
    print(f"El superheroe mas bajo es, {el_heroe_mas_bajo} y su altura es, {altura_mas_baja}\n")


#F
def promedio_altura_heroes(lista):
    print("\n")
    acumulador_alturas = 0
    for heroe in lista:
        altura = float(heroe['altura'])
        acumulador_alturas += altura
        promedio = acumulador_alturas / len(lista)
    print(f"El promedio de la altura de los superheroes es:{promedio}\n")


#G
def nombre_m_alto_m_bajo(lista):
    print("\n")
    bandera_mas_alto = True
    bandera_mas_bajo = True
    altura_mas_alta = 0
    altura_mas_baja = 0
    for heroe_alto in lista:
        altura = float(heroe_alto['altura'])
        if bandera_mas_alto or altura > altura_mas_alta:
            bandera_mas_alto = False
            altura_mas_alta = altura
            super_heroe_alto = heroe_alto['nombre']
            el_heroe_mas_alto = super_heroe_alto
    
    for heroe_bajo in lista:
        altura = float(heroe_bajo['altura'])
        if bandera_mas_bajo or altura < altura_mas_baja:
            bandera_mas_bajo = False
            altura_mas_baja = altura
            super_heroe_bajo = heroe_bajo['nombre']
            el_heroe_mas_bajo = super_heroe_bajo

    print(f"El nombre del superheroe mas alto es, {el_heroe_mas_alto} y el nombre del superheroe mas bajo es, {el_heroe_mas_bajo}\n")


#H
def informar_m_pesado_m_liviano(lista):
    print("\n")
    bandera_mas_pesado = True
    bandera_mas_liviano = True
    peso_mas_pesado = 0
    peso_mas_liviano = 0
    for heroe_pesado in lista:
        peso = float(heroe_pesado['peso'])
        if bandera_mas_pesado or peso > peso_mas_pesado:
            bandera_mas_pesado = False
            peso_mas_pesado = peso
            super_heroe_pesado = heroe_pesado['nombre']
            el_heroe_mas_pesado = super_heroe_pesado

    for heroe_liviano in lista:
        peso = float(heroe_liviano['peso'])
        if bandera_mas_liviano or peso < peso_mas_liviano:
            bandera_mas_liviano = False
            peso_mas_liviano = peso
            super_heroe_liviano = heroe_liviano['nombre']
            el_heroe_mas_liviano = super_heroe_liviano
    
    print(f"El nombre del superheroe mas pesado es, {el_heroe_mas_pesado} y el superheroe mas liviano es, {el_heroe_mas_liviano}\n")




def stark_00():
    while True:
        os.system("cls")
        match menu_stark_00():

            case "1":
                mostrar_nombres(lista_personajes)

            case "2":
                mostrar_nom_alt(lista_personajes)

            case "3":
                heroe_mas_alto(lista_personajes)

            case '4':
                heroe_mas_bajo(lista_personajes)

            case "5":
                promedio_altura_heroes(lista_personajes)

            case "6":
                nombre_m_alto_m_bajo(lista_personajes)

            case "7":
                informar_m_pesado_m_liviano(lista_personajes)

            case "8":
                break



        os.system("Pause")


def salida_menu():
  salida = input("\nDesea salir?(s o n)🤔: ")
  if salida.lower() == "s":
    print("Saliste, hasta luego")
    return True
  else:
    return False





