from Utilidades import menu, registro, listar, buscar, salir, promedio
from os import system

alumnos=[]
op=0
while True:
    system("cls")
    menu()
    op=int(input("1, 2 , 3, 4 o 5:  "))

    if op==1:
        system("cls")
        alumnos.append(registro())
        input("Presione enter para continuar: ")
    elif op==2:
        system("cls")
        listar(alumnos)
        input("Presione enter para continuar: ")
    elif op==3:
        system("cls")
        buscar(alumnos)
        input("Presione enter para continuar: ")

    elif op==4:
        system("cls")
        promedio(alumnos)
        input("Presione enter para continuar: ")
    elif op==5:
        system("cls")
        salir(alumnos)
        break
    else:
        print("Ingrese numero valido")
