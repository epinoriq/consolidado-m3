
print("------------------Bienvenido a la Lista de personajes.------------------")

personajes = [
    {"id": 1, "nombre": "Harry Houdini", "tipo": "Mago"},
    {"id": 2, "nombre": "Newton", "tipo": "Cientifico"},
    {"id": 3, "nombre": "David Blaine", "tipo": "Mago"},
    {"id": 4, "nombre": "Hawking", "tipo": "Cientifico"},
    {"id": 5, "nombre": "Messi", "tipo": "Otros"},
    {"id": 6, "nombre": "Teller", "tipo": "Mago"},
    {"id": 7, "nombre": "Einstein", "tipo": "Cientifico"},
    {"id": 8, "nombre": "Pele", "tipo": "Otros"},
    {"id": 9, "nombre": "Juanes", "tipo": "Otros"},
]

copia_personajes = personajes

def ver_magos():
    for personaje in personajes:
        if (personaje["tipo"] == "Mago"):
            print("Nombre :", personaje["nombre"])

def ver_cientificos():
    for personaje in personajes:
        if (personaje["tipo"] == "Cientifico"):
            print("Nombre :", personaje["nombre"])

def ver_otros():
    for personaje in personajes:
        if (personaje["tipo"] == "Otros"):
            print("Nombre :", personaje["nombre"])

def imprimir_nombres():
    for personaje in personajes:
            print("Nombre :", personaje["nombre"], ", Tipo :", personaje["tipo"])


def hacer_grandioso():
    for personaje in personajes:
        if (personaje["tipo"] == "Mago"):
            #personaje["nombre"]="EL GRAN "+personaje["nombre"]
            #personajes.update({"nombre": "EL GRAN"+personaje["nombre"]})
            print("Nombre :","El gran "+personaje["nombre"])

def lista_actualizada():
    for personaje in personajes:
        if (personaje["tipo"] == "Mago"):
            print("Nombre :","El gran "+personaje["nombre"],", Tipo :", personaje["tipo"])
        else:
            print("Nombre :", personaje["nombre"], ", Tipo :", personaje["tipo"])

while True:
    print()
    print("1 - Ver lista de magos\n"
          "2 - Ver lista de cientificos\n"
          "3 - Ver lista de otros\n"
          "4 - Ver lista completa\n"
          "5 - Agregar nuevo apodo (El gran) a los magos\n"
          "6 - Ver lista actualizada\n"
          "7 - Salir")
    try:
        operacion = int(input(": "))
    except ValueError:
        nombre_operacion = "Por favor ingresar solo numeros, no letras u otros caracteres"
    else:
        if operacion == 1:
            ver_magos()
        elif operacion == 2:
            ver_cientificos()
        elif operacion == 3:
            ver_otros()
        elif operacion == 4:
            imprimir_nombres()
        elif operacion == 5:
            hacer_grandioso()
        elif operacion == 6:
            lista_actualizada()
        elif operacion == 7:
            break
        else:
            print("Numero ingreso no es el correcto. Por favor seleccione un numero indicado en la lista")