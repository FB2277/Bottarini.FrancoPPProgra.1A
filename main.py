# Main prueba de todas las funciones:

from data_stark import *
from funciones_00 import *
from funciones_01 import *
from menu import *
import os

while True:
    os.system("cls")
    match menu_general():


        case "1":
            stark_00()
        
        case "2":
            stark_01()
        
        case "5":
            if salida_menu():
                break
            

  

