def menu():
    print("Seleccione una opcion")
    print("1.	Registrar alumno")
    print("2.	Listar todos los alumnos")
    print("3.	Buscar alumnos por nivel")
    print("4.	Calcular la nota promedio de los alumnos")
    print("5.	Salir del programa y guardar")

def registro():
    notas=[]
    nom=input("ingrese Nombre del alumno: ")
    ape=input("Ingrese Apellido del alumno: ")
    edad=input("Ingrese edad del alumno: ")
    lvl=input("Ingrese el nivel del estudiante (Ejemplo: 1°, 2°, 3°, etc.): ")
    n1=int(input("1° Nota: "))
    n2=int(input("2° Nota: "))
    n3=int(input("3° Nota: "))
    n4=int(input("4° Nota: "))
    n5=int(input("5° Nota: "))
    notas.append(n1)
    notas.append(n2)
    notas.append(n3)
    notas.append(n4)
    notas.append(n5)
    reg={"Nombre":nom,"Apellido":ape,"Edad":edad,"Nivel":lvl,"Notas":notas}
    return reg

def listar(lista):
    for i in range(len(lista)):
        print(f"{i+1}° Alumno")
        print(f"{lista[i]["Nombre"]}, {lista[i]["Apellido"]}, {lista[i]["Edad"]}, {lista[i]["Nivel"]}, {lista[i]["Notas"]}")
        print("*******************************")

def buscar(lista):
    codigo=input("Ingrese nivel que desea buscar: ")
    encontrado=False

    for i in range(len(lista)):
        if codigo==lista[i]["Nivel"]:
            encontrado=True
    
    if encontrado==True:
        print(f"Nivel: {lista[i]["Nivel"]}")
        print(f"Nombre: {lista[i]["Nombre"]}")
        print(f"Apllido: {lista[i]["Apellido"]}")
        print(f"Edad: {lista[i]["Edad"]}")
        print(f"Notas: {lista[i]["Notas"]}")
        print("**************************")
        print(" ")
    else:
        print("Nivel no encontrado")


def promedio(lista):
    for i in lista:
        print(f"Nombre: {lista[i]["Nombre"]}")
        print(f"Notas: {lista[i]["Notas"]}")
        print(f"El promedio de notas es: {(lista[i]["Notas"][0]+lista[i]["Notas"][1]+lista[i]["Notas"][2]+lista[i]["Notas"][3]+lista[i]["Notas"][4])/5}")
        print("******************************")
        print(" ")

def salir(lista):
    with open ("Listapeliculas.txt","w") as archivo:
        for i in lista:
            txt= i["Nombre"]+", "+i["Apellido"]+", "+i["Edad"]+", "+i["Nivel"]+", "+"\n"
            archivo.write(txt)

