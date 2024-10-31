print("\nRuvalcaba Valverde Mguel Angel_1212_3W")
print("--------Punto 4--------")
n = input("Ingresa tu nombre:")#esta es la recta final que emosinate
e = input("Ingresa tu edad:")#hay que haser valores
d = input("Ingresa tu direccion:")
t = input("Ingresa su tu telefono:")
Dicc = {#que despus los comvertiremos en las descrisiones del diccionario, oviamente tambien ha qye haser un dicionario
    "nombre":n,
    "edad":e,
    "direccion":d,
    "telefono":t
}
#nota: intente por un # en el print pero se me olvido, ya podemos continuar.
#y por ultimo se be el mensaje de aunto doxear
#Doxear: Acion de doxeo
#Doxeo: El acto de revelar informasion privada, como direccion, nmero telefonico, nombre y edad reales, todo con fines malisioso.
print(f"Hola <{Dicc["nombre"]}> tiene <{Dicc["edad"]}> años, vive en <{Dicc["direccion"]}> y su número de teléfono es <{Dicc["telefono"]}>.")
print("-------------------------------------")
print("Objetivo: Escribir un programa que pregunte al usuario su nombre, edad, dirección yteléfono y lo guarde en un diccionario. Después debe mostrar por pantalla el mensaje <nombre> tiene <edad> años, vive en <dirección> y su número de teléfono es <teléfono>.\n")
print("Resultado: Listo termine, pero en resumen se ben los valores eviados\n")
