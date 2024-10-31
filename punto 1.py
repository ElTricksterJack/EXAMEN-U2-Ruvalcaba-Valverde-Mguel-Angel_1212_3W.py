print("\nRuvalcaba Valverde Mguel Angel_1212_3W")
print("--------Punto 1--------")
#bueno no dise que hay que haser un dicionario sino una LISTA.
#PRIMERO hay que definir las materias.
#tambien allade las de harry poter si quieres
print("Escribe los nombres de las Materias")
M1 = input("Materia 1: ")
M2 = input("Materia 2: ")
M3 = input("Materia 3: ")
M4 = input("Materia 4: ")
M5 = input("Materia 5: ")
M6 = input("Materia 6: ")
M7 = input("Materia 7: ") 
MATE = [M1,M2,M3,M4,M5,M6,M7]#guntemoslas en una lista
C1 = float(input(f"Calisficasion de {MATE[0]}:"))#y dales su calificasion, respctiva a cada uno
C2 = float(input(f"Calisficasion de {MATE[1]}:"))
C3 = float(input(f"Calisficasion de {MATE[2]}:"))
C4 = float(input(f"Calisficasion de {MATE[3]}:"))
C5 = float(input(f"Calisficasion de {MATE[4]}:"))
C6 = float(input(f"Calisficasion de {MATE[5]}:"))
C7 = float(input(f"Calisficasion de {MATE[6]}:"))
CAL = [C1,C2,C3,C4,C5,C6,C7]#ahora pasa esas calificasiones a un lista

print("\n--Para Aprobar el Minimo es 6--")
print("--Estas son las materias que recursaras--")#y con esto, beremos si algun alguna calificasion es menor que 6
if CAL[0] < 6:
    print("recursaras",MATE[0])

if CAL[1] < 6:
    print("recursaras",MATE[1])

if CAL[2] < 6:
    print("recursaras",MATE[2])

if CAL[3] < 6:
    print("recursaras",MATE[3])

if CAL[4] < 6:
    print("recursaras",MATE[4])

if CAL[5] < 6:
    print("recursaras",MATE[5])

if CAL[6] < 6:
    print("recursaras",MATE[6])
#bueno eso es todo, adios
print("--------------------------------------")
print("Objetivo: Escribir un programa que almacene las\nasignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y\nLengua) en una lista, pregunte al usuario la nota que ha sacado en cada\nasignatura y elimine de la lista las asignaturas aprobadas. Al final el\nprograma debe mostrar por pantalla las asignaturas que el usuario tiene que repetir.\n")
print("Resultado: se motraron las materias con calificasion baja, y se quitaron las materias aprobadas.\n")
