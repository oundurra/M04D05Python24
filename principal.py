from personaje import Personaje
import random

print("Bienvenido a Pelea de Orcos")
print("===========================")
print("")

n_personaje = input("Ingrese el nombre del personaje azul: ")
personajeazul = Personaje(n_personaje)
print("El estado del personaje es:")
print(personajeazul.get_estado())


orcoblanco = Personaje("Orco")

print("Ha aparecido un nuevo personaje: " + orcoblanco.nombre)

continuar = "S"
while continuar == "S":
    v_probabilidad = personajeazul.get_probabilidad(orcoblanco)

    print(f"Tienes un {v_probabilidad*100}% de ganarle al orco.")
    print("")
    print(f"Si ganas recibiras 50 puntos de experiencia y el orco perderá 30 y viceversa.")

    opcion = 0
    while opcion not in ("1","2"):
        opcion = input("Ingrese la opción: 1=Atacar, 2=Huir: ")

    opcion = int(opcion)

    if opcion == 1:
        if random.random() <= v_probabilidad:
            v_mensaje = "Gana"
            orcoblanco.set_estado(-30)
            personajeazul.set_estado(50)
        else:
            v_mensaje = "Pierde"
            orcoblanco.set_estado(50)
            personajeazul.set_estado(-30)
    else:
        v_mensaje = "Eres un gallina McFly"

    print("")
    print(v_mensaje)
    print(f"El estado del personaje es: {personajeazul.get_estado()}")
    print(f"El estado del orco es: {orcoblanco.get_estado()}")

    print("")

    continuar = ""
    while continuar not in ("S","N"):
        continuar = input("Ingrese la opción: S=Seguir , N=No Seguir: ")







