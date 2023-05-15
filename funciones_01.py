# Funciones del desafio 01
from data_stark import *
from menu import *
import os

#A
def mostrar_nombres_M(lista):
    print("\n")
    for heroes_M in lista:
        genero = heroes_M['genero']
        if genero == 'M':
            print(heroes_M['nombre'])
    print("\n")


#B
def mostrar_nombres_F(lista):
    print("\n")
    for heroes_F in lista:
        genero = heroes_F['genero']
        if genero == 'F':
            print(heroes_F['nombre'])
    print("\n")


#C
def heroe_m_alto_M(lista):
    print("\n")
    bandera_mas_alto_M = True
    altura_mas_alta_M = 0
    for heroe_alto_M in lista:
        genero = heroe_alto_M['genero']
        if genero == 'M':
            altura = float(heroe_alto_M['altura'])
            if bandera_mas_alto_M or altura > altura_mas_alta_M:
                bandera_mas_alto_M = False
                altura_mas_alta_M = altura
                super_heroe_alto_M = heroe_alto_M['nombre']
                el_heroe_mas_alto_M = super_heroe_alto_M
    
    print(f"El superheroe mas alto de genero M es, {el_heroe_mas_alto_M} y su altura es {altura_mas_alta_M}\n")
    


#D
def heroe_m_alto_F(lista):
    print("\n")
    bandera_mas_alto_F = True
    altura_mas_alta_F = 0
    for heroe_alto_F in lista:
        genero = heroe_alto_F['genero']
        if genero == 'F':
            altura = float(heroe_alto_F['altura'])
            if bandera_mas_alto_F or altura > altura_mas_alta_F:
                bandera_mas_alto_F = False
                altura_mas_alta_F = altura
                super_heroe_alto_F = heroe_alto_F['nombre']
                el_heroe_mas_alto_F = super_heroe_alto_F
    
    print(f"El superheroe mas alto de genero F es, {el_heroe_mas_alto_F} y su altura es {altura_mas_alta_F}\n")
    


#E
def heroe_m_bajo_M(lista):
    print("\n")
    bandera_mas_bajo_M = True
    altura_mas_baja_M = 0
    for heroe_bajo_M in lista:
        genero = heroe_bajo_M['genero']
        if genero == 'M':
            altura = float(heroe_bajo_M['altura'])
            if bandera_mas_bajo_M or altura < altura_mas_baja_M:
                bandera_mas_bajo_M = False
                altura_mas_baja_M = altura
                super_heroe_bajo_M = heroe_bajo_M['nombre']
                el_heroe_mas_bajo_M = super_heroe_bajo_M
    
    print(f"El superheroe mas bajo de genero M es, {el_heroe_mas_bajo_M} y su altura es {altura_mas_baja_M}\n")
    


#F
def heroe_m_bajo_F(lista):
    print("\n")
    bandera_mas_bajo_F = True
    altura_mas_baja_F = 0
    for heroe_bajo_F in lista:
        genero = heroe_bajo_F['genero']
        if genero == 'F':
            altura = float(heroe_bajo_F['altura'])
            if bandera_mas_bajo_F or altura < altura_mas_baja_F:
                bandera_mas_bajo_F = False
                altura_mas_baja_F = altura
                super_heroe_bajo_F = heroe_bajo_F['nombre']
                el_heroe_mas_bajo_F = super_heroe_bajo_F
    
    print(f"El superheroe mas bajo de genero F es, {el_heroe_mas_bajo_F} y su altura es {altura_mas_baja_F}\n")
   


#G
def promedio_altura_heroes_M(lista):
    print("\n")
    acumulador_alturas_M = 0
    contador = 0
    for heroe in lista:
        genero = heroe['genero']
        if genero == 'M':
            altura = float(heroe['altura'])
            acumulador_alturas_M += altura
            contador += 1
            promedio = acumulador_alturas_M / contador
    print(f"El promedio de la altura de todos los superheroes de genero M es: {promedio}\n")
    


#H
def promedio_altura_heroes_F(lista):
    print("\n")
    acumulador_alturas_F = 0
    contador = 0
    for heroe in lista:
        genero = heroe['genero']
        if genero == 'F':
            altura = float(heroe['altura'])
            acumulador_alturas_F += altura
            contador += 1
            promedio = acumulador_alturas_F / contador
    print(f"El promedio de la altura de todos los superheroes de genero F es: {promedio}\n")
    


#I
def informar_nombre_puntos_C_al_F(lista):
    print("\n")
    bandera_mas_alto_M = True
    altura_mas_alta_M = 0
    bandera_mas_alto_F = True
    altura_mas_alta_F = 0
    bandera_mas_bajo_M = True
    altura_mas_baja_M = 0
    bandera_mas_bajo_F = True
    altura_mas_baja_F = 0
    for heroe_alto_M in lista:
        genero = heroe_alto_M['genero']
        if genero == 'M':
            altura = float(heroe_alto_M['altura'])
            if bandera_mas_alto_M or altura > altura_mas_alta_M:
                bandera_mas_alto_M = False
                altura_mas_alta_M = altura
                super_heroe_alto_M = heroe_alto_M['nombre']
                el_heroe_mas_alto_M = super_heroe_alto_M
    
    for heroe_alto_F in lista:
        genero = heroe_alto_F['genero']
        if genero == 'F':
            altura = float(heroe_alto_F['altura'])
            if bandera_mas_alto_F or altura > altura_mas_alta_F:
                bandera_mas_alto_F = False
                altura_mas_alta_F = altura
                super_heroe_alto_F = heroe_alto_F['nombre']
                el_heroe_mas_alto_F = super_heroe_alto_F

    for heroe_bajo_M in lista:
        genero = heroe_bajo_M['genero']
        if genero == 'M':
            altura = float(heroe_bajo_M['altura'])
            if bandera_mas_bajo_M or altura < altura_mas_baja_M:
                bandera_mas_bajo_M = False
                altura_mas_baja_M = altura
                super_heroe_bajo_M = heroe_bajo_M['nombre']
                el_heroe_mas_bajo_M = super_heroe_bajo_M

    for heroe_bajo_F in lista:
        genero = heroe_bajo_F['genero']
        if genero == 'F':
            altura = float(heroe_bajo_F['altura'])
            if bandera_mas_bajo_F or altura < altura_mas_baja_F:
                bandera_mas_bajo_F = False
                altura_mas_baja_F = altura
                super_heroe_bajo_F = heroe_bajo_F['nombre']
                el_heroe_mas_bajo_F = super_heroe_bajo_F

    print(f""" 
El superheroe mas alto de genero M es: {el_heroe_mas_alto_M}
El superheroe mas alto de genero F es: {el_heroe_mas_alto_F}
El superheroe mas bajo de genero M es: {el_heroe_mas_bajo_M}
El superheroe mas bajo de genero F es: {el_heroe_mas_bajo_F}
\n""")


#J 
def informar_cantidad_heroes_por_color_ojos(lista):
    print("\n")
    contador_brown = 0
    for heroe_ojos_brown in lista:
        color_ojos = (heroe_ojos_brown['color_ojos'])
        if color_ojos == 'Brown':
            contador_brown += 1
    print(f"La cantidad de heroes que tienen ojos Brown son: {contador_brown}")

    print("======================================================\n")

    contador_blue = 0
    for heroe_ojos_blue in lista:
        color_ojos = (heroe_ojos_blue['color_ojos'])
        if color_ojos == 'Blue':
            contador_blue += 1
    print(f"La cantidad de heroes que tienen ojos Blue son: {contador_blue}")

    print("======================================================\n")

    contador_green = 0
    for heroe_ojos_green in lista:
        color_ojos = (heroe_ojos_green['color_ojos'])
        if color_ojos == 'Green':
            contador_green += 1
    print(f"La cantidad de heroes que tienen ojos Green son: {contador_green}")

    print("======================================================\n")

    contador_yellow = 0
    for heroe_ojos_yellow in lista:
        color_ojos = (heroe_ojos_yellow['color_ojos'])
        if color_ojos == 'Yellow' or color_ojos == 'Yellow (without irises)':
            contador_yellow += 1
    print(f"La cantidad de heroes que tienen ojos Yellow son: {contador_yellow}")

    print("======================================================\n")

    contador_hazel = 0
    for heroe_ojos_hazel in lista:
        color_ojos = (heroe_ojos_hazel['color_ojos'])
        if color_ojos == 'Hazel':
            contador_hazel += 1
    print(f"La cantidad de heroes que tienen ojos Hazel son: {contador_hazel}")

    print("======================================================\n")

    contador_silver = 0
    for heroe_ojos_silver in lista:
        color_ojos = (heroe_ojos_silver['color_ojos'])
        if color_ojos == 'Silver':
            contador_silver += 1
    print(f"La cantidad de heroes que tienen ojos Silver son: {contador_silver}")

    print("======================================================\n")

    contador_red = 0
    for heroe_ojos_red in lista:
        color_ojos = (heroe_ojos_red['color_ojos'])
        if color_ojos == 'Red':
            contador_red += 1
    print(f"La cantidad de heroes que tienen ojos Red son: {contador_red}\n")


#K
def informar_cantidad_heroes_por_color_pelo(lista):
    print("\n")
    contador_yellow = 0
    for heroe_pelo_yellow in lista:
        color_pelo = (heroe_pelo_yellow['color_pelo'])
        if color_pelo == 'Yellow':
            contador_yellow += 1
    print(f"La cantidad de heroes que tienen el pelo Yellow son: {contador_yellow}")

    print("========================================================\n")

    contador_marron_blanco_ambos = 0
    for heroe_pelo_marron_blanco_ambos in lista:
        color_pelo = (heroe_pelo_marron_blanco_ambos['color_pelo'])
        if color_pelo == 'Brown' or color_pelo == 'White' or color_pelo == 'Brown / White':
            contador_marron_blanco_ambos += 1
    print(f"La cantidad de heroes que tienen el pelo Brown or White or ambos son: {contador_marron_blanco_ambos}")

    print("=========================================================================\n")

    contador_black = 0
    for heroe_pelo_black in lista:
        color_pelo = (heroe_pelo_black['color_pelo'])
        if color_pelo == 'Black':
            contador_black += 1
    print(f"La cantidad de heroes que tienen el pelo Black son: {contador_black}")

    print("========================================================\n")

    contador_auburn = 0
    for heroe_pelo_auburn in lista:
        color_pelo = (heroe_pelo_auburn['color_pelo'])
        if color_pelo == 'Auburn':
            contador_auburn += 1
    print(f"La cantidad de heroes que tienen el pelo Auburn son: {contador_auburn}")

    print("========================================================\n")

    contador_red_orange = 0
    for heroe_pelo_red_orange in lista:
        color_pelo = (heroe_pelo_red_orange['color_pelo'])
        if color_pelo == 'Red / Orange' or color_pelo == 'Red':
            contador_red_orange += 1
    print(f"La cantidad de heroes que tienen el pelo Red or Red/Orange son: {contador_red_orange}")

    print("====================================================================\n")

    contador_no_hair = 0
    for heroe_no_hair in lista:
        color_pelo = (heroe_no_hair['color_pelo'])
        if color_pelo == 'No Hair':
            contador_no_hair += 1
    print(f"La cantidad de heroes que no tienen pelo son: {contador_no_hair}")

    print("==================================================\n")

    contador_blond = 0
    for heroe_pelo_blond in lista:
        color_pelo = (heroe_pelo_blond['color_pelo'])
        if color_pelo == 'Blond':
            contador_blond += 1
    print(f"La cantidad de heroes que tienen el pelo Blond son: {contador_blond}")

    print("========================================================\n")

    contador_green = 0
    for heroe_pelo_green in lista:
        color_pelo = (heroe_pelo_green['color_pelo'])
        if color_pelo == 'Green':
            contador_green += 1
    print(f"La cantidad de heroes que tienen el pelo Green son: {contador_green}\n")


#L
def informar_cantidad_heroes_por_intligencia(lista):
    print("\n")
    contador_no_tiene = 0
    for heroe_inteligencia_no_tiene in lista:
        heroe_inteligencia = (heroe_inteligencia_no_tiene['inteligencia'])
        if heroe_inteligencia == '':
            contador_no_tiene += 1
    print(f"La cantidad de heroes que no tienen inteligencia son: {contador_no_tiene}") 

    print("=================================================================\n")
    
    contador_average = 0
    for heroe_inteligencia_average in lista:
        heroe_inteligencia = (heroe_inteligencia_average['inteligencia'])
        if heroe_inteligencia == 'average':
            contador_average += 1
    print(f"La cantidad de heroes que tienen inteligencia average son: {contador_average}")

    print("=================================================================\n")
    
    contador_good = 0
    for heroe_inteligencia_good in lista:
        heroe_inteligencia = (heroe_inteligencia_good['inteligencia'])
        if heroe_inteligencia == 'good':
            contador_good += 1
    print(f"La cantidad de heroes que tienen inteligencia good son: {contador_good}")

    print("=================================================================\n")
    
    contador_high = 0
    for heroe_inteligencia_high in lista:
        heroe_inteligencia = (heroe_inteligencia_high['inteligencia'])
        if heroe_inteligencia == 'high':
            contador_high += 1
    print(f"La cantidad de heroes que tienen inteligencia high son: {contador_high}\n")


#M
def informar_superheroe_por_cada_color_ojos(lista):
    print("\nLos superheroes que tienen el color de ojos Brown son:")
    print("--------------------------------------------------------")
    for heroe_ojos_marron in lista:
        color_ojos = (heroe_ojos_marron['color_ojos'])
        if color_ojos == 'Brown':
            print(heroe_ojos_marron['nombre'])
    
    print("\n======================================================\n")
    
    print("Los superheroes que tienen el color de ojos Blue son:")
    print("-----------------------------------------------------")
    for heroe_ojos_azul in lista:
        color_ojos = (heroe_ojos_azul['color_ojos'])
        if color_ojos == 'Blue':
            print(heroe_ojos_azul['nombre'])
    
    print("\n======================================================\n")
    
    print("Los superheroes que tienen el color de ojos Green son:")
    print("------------------------------------------------------")
    for heroe_ojos_verde in lista:
        color_ojos = (heroe_ojos_verde['color_ojos'])
        if color_ojos == 'Green':
            print(heroe_ojos_verde['nombre'])

    print("\n======================================================\n")
    
    print("Los superheroes que tienen el color de ojos Yellow son:")
    print("-------------------------------------------------------")
    for heroe_ojos_amarillo in lista:
        color_ojos = (heroe_ojos_amarillo['color_ojos'])
        if color_ojos == 'Yellow' or color_ojos == 'Yellow (without irises)':
            print(heroe_ojos_amarillo['nombre'])

    print("\n======================================================\n")
    
    print("Los superheroes que tienen el color de ojos Hazel son:")
    print("------------------------------------------------------")
    for heroe_ojos_hazel in lista:
        color_ojos = (heroe_ojos_hazel['color_ojos'])
        if color_ojos == 'Hazel':
            print(heroe_ojos_hazel['nombre'])
    
    print("\n======================================================\n")

    print("Los superheroes que tienen el color de ojos Silver son:")
    print("-------------------------------------------------------")
    for heroe_ojos_silver in lista:
        color_ojos = (heroe_ojos_silver['color_ojos'])
        if color_ojos == 'Silver':
            print(heroe_ojos_silver['nombre'])

    print("\n======================================================\n")

    print("Los superheroes que tienen el color de ojos Red son:")
    print("----------------------------------------------------")
    for heroe_ojos_rojo in lista:
        color_ojos = (heroe_ojos_rojo['color_ojos'])
        if color_ojos == 'Red':
            print(heroe_ojos_rojo['nombre'])
    print("\n")

#N
def informar_superheroe_por_cada_color_pelo(lista):
    print("\nLos superheroes que tienen el pelo de color Yellow son:")
    print("---------------------------------------------------------")
    for heroe_pelo_amarillo in lista:
        color_pelo = (heroe_pelo_amarillo['color_pelo'])
        if color_pelo == 'Yellow':
            print(heroe_pelo_amarillo['nombre'])

    print("\n======================================================\n")
    
    print("Los superheroes que tienen el pelo de color Brown, White o Brown/White son:")
    print("---------------------------------------------------------------------------")
    for heroe_pelo_marron_blanco_ambos in lista:
        color_pelo = (heroe_pelo_marron_blanco_ambos['color_pelo'])
        if color_pelo == 'Brown' or color_pelo == 'White' or color_pelo == 'Brown / White':
            print(heroe_pelo_marron_blanco_ambos['nombre'])

    print("\n======================================================\n")
    
    print("Los superheroes que tienen el pelo de color Black son:")
    print("------------------------------------------------------")
    for heroe_pelo_negro in lista:
        color_pelo = (heroe_pelo_negro['color_pelo'])
        if color_pelo == 'Black':
            print(heroe_pelo_negro['nombre'])

    print("\n======================================================\n")
    
    print("Los superheroes que tienen el pelo de color Auburn son:")
    print("-------------------------------------------------------")
    for heroe_pelo_auburn in lista:
        color_pelo = (heroe_pelo_auburn['color_pelo'])
        if color_pelo == 'Auburn':
            print(heroe_pelo_auburn['nombre'])

    print("\n======================================================\n")
    
    print("Los superheroes que tienen el pelo de color Red o Red/Orange son:")
    print("-----------------------------------------------------------------")
    for heroe_pelo_rojo_naranja in lista:
        color_pelo = (heroe_pelo_rojo_naranja['color_pelo'])
        if color_pelo == 'Red / Orange' or color_pelo == 'Red':
            print(heroe_pelo_rojo_naranja['nombre'])

    print("\n======================================================\n")
    
    print("Los superheroes que no tienen pelo son:")
    print("---------------------------------------")
    for heroe_pelo_sin_pelo in lista:
        color_pelo = (heroe_pelo_sin_pelo['color_pelo'])
        if color_pelo == 'No Hair':
            print(heroe_pelo_sin_pelo['nombre'])

    print("\n======================================================\n")
    
    print("Los superheroes que tienen el pelo de color Blond son:")
    print("------------------------------------------------------")
    for heroe_pelo_blond in lista:
        color_pelo = (heroe_pelo_blond['color_pelo'])
        if color_pelo == 'Blond':
            print(heroe_pelo_blond['nombre'])

    print("\n======================================================\n")
    
    print("Los superheroes que tienen el pelo de color Green son:")
    print("------------------------------------------------------")
    for heroe_pelo_verde in lista:
        color_pelo = (heroe_pelo_verde['color_pelo'])
        if color_pelo == 'Green':
            print(heroe_pelo_verde['nombre'])
    print("\n")

#O
def informar_superheroe_por_cada_inteligencia(lista):
    print("\nLos superheroes que tienen la inteligencia average son:")
    print("-------------------------------------------------------")
    for heroe_inteligencia_average in lista:
        heroe_inteligencia = (heroe_inteligencia_average['inteligencia'])
        if heroe_inteligencia == 'average':
            print(heroe_inteligencia_average['nombre'])

    print("\n======================================================\n")
    
    print("Los superheroes que tienen la inteligencia good son:")
    print("----------------------------------------------------")
    for heroe_inteligencia_good in lista:
        heroe_inteligencia = (heroe_inteligencia_good['inteligencia'])
        if heroe_inteligencia == 'good':
            print(heroe_inteligencia_good['nombre'])

    print("\n======================================================\n")
    
    print("Los superheroes que tienen la inteligencia high son:")
    print("----------------------------------------------------")
    for heroe_inteligencia_high in lista:
        heroe_inteligencia = (heroe_inteligencia_high['inteligencia'])
        if heroe_inteligencia == 'high':
            print(heroe_inteligencia_high['nombre'])

    print("\n======================================================\n")
    
    print("Los superheroes que no tienen inteligencia son:")
    print("-----------------------------------------------")
    for heroe_inteligencia_good in lista:
        heroe_inteligencia = (heroe_inteligencia_good['inteligencia'])
        if heroe_inteligencia == '':
            print(f"{heroe_inteligencia_good['nombre']}: No tiene")
    print("\n")




def stark_01():
    while True:
        os.system("cls")
        match menu_stark_01():

            case "1":
                mostrar_nombres_M(lista_personajes)

            case "2":
                mostrar_nombres_F(lista_personajes)            
            
            case "3":
                heroe_m_alto_M(lista_personajes)
            
            case "4":
                heroe_m_alto_F(lista_personajes)
            
            case "5":
                heroe_m_bajo_M(lista_personajes)
            
            case "6":
                heroe_m_bajo_F(lista_personajes)
            
            case "7":
                promedio_altura_heroes_M(lista_personajes)
            
            case "8":
                promedio_altura_heroes_F(lista_personajes)
            
            case "9":
                informar_nombre_puntos_C_al_F(lista_personajes)
            
            case "10":
                informar_cantidad_heroes_por_color_ojos(lista_personajes) 
            
            case "11":
                informar_cantidad_heroes_por_color_pelo(lista_personajes)

            case "12":
                informar_cantidad_heroes_por_intligencia(lista_personajes)
            
            case "13":
                informar_superheroe_por_cada_color_ojos(lista_personajes)
            
            case "14":
                informar_superheroe_por_cada_color_pelo(lista_personajes)
            
            case "15":
                informar_superheroe_por_cada_inteligencia(lista_personajes)
            
            case "16":
                break    

        
        os.system("Pause")









