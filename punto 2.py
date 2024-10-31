print("\nRuvalcaba Valverde Mguel Angel_1212_3W")
print("--------Punto 2--------")
cur = {
    "Esgrima": 0,
    "Matematicas": 0,
    "Biologia": 0,
    "Estudio de Idiomas Antiguas": 0,
    "Escritura": 0
}
print("--Allade los creditos que tiene--")
C1 = float(input(f"Calisficasion de Esgrima:"))
cur["Esgrima"] = C1
C2 = float(input(f"Calisficasion de Matematicas:"))
cur["Matematicas"] = C2
C3 = float(input(f"Calisficasion de Biologia:"))
cur["Biologia"] = C3
C4 = float(input(f"Calisficasion de Estudio de Idiomas Antiguas:"))
cur["Estudio de Idiomas Antiguas"] = C4
C5 = float(input(f"Calisficasion de Escritura:"))
cur["Escritura"] = C5
print("--Mostrar Creditos Optenidos--")
print(f"Los creditos son {cur["Esgrima"]}, en Esgrima.") 
print(f"Los creditos son {cur["Matematicas"]}, en Matematicas.") 
print(f"Los creditos son {cur["Biologia"]}, en Biologia.") 
print(f"Los creditos son {cur["Estudio de Idiomas Antiguas"]}, en Estudio de Idiomas Antiguas.") 
print(f"Los creditos son {cur["Escritura"]}, en Escritura.") 

print("--------------------------------------")
print("Objetivo: Escribir un programa que almacene el diccionario\ncon los créditos de las asignaturas de un curso {'Matemáticas': 6, 'Física': 4, 'Química': 5} y\ndespués muestre por pantalla los créditos de cada asignatura en el\nformato <asignatura>\ntiene <créditos> créditos, donde <asignatura> es\ncada una de las asignaturas del curso, y <créditos> son sus créditos.\nAl final debemostrar también el número total de créditos del curso.\n")
print("Resultado: se bieron los creditos de cada respectivo curso y el nombre del curso.\n")
