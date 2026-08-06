equipos = {
    "Portatil 1": {
        "disponible": True,
        "prestamos": []
    },
    "Portatil 2": {
        "disponible": True,
        "prestamos": []
    },
    "Video Beam": {
        "disponible": True,
        "prestamos": []
    }
}



def mostrar_equipos():

    print("\n===== LISTA DE EQUIPOS =====")

    for nombre, datos in equipos.items():

        if datos["disponible"] == True:
            estado = "Disponible"
        else:
            estado = "Prestado"

        print(nombre, "-", estado)



def registrar_prestamo():

    mostrar_equipos()

    equipo = input("\nEscriba el nombre del equipo: ")

    if equipo not in equipos:
        print("Ese equipo no existe.")
        return

    if equipos[equipo]["disponible"] == False:
        print("Ese equipo ya está prestado.")
        return

    usuario = input("Nombre del usuario: ")
    fecha = input("Fecha del préstamo: ")

    prestamo = (usuario, fecha)

    equipos[equipo]["prestamos"].append(prestamo)

    equipos[equipo]["disponible"] = False

    print("Préstamo registrado correctamente.")



def devolver_equipo():

    equipo = input("\nIngrese el nombre del equipo: ")

    if equipo not in equipos:
        print("Ese equipo no existe.")
        return

    if equipos[equipo]["disponible"] == True:
        print("Ese equipo ya está disponible.")
        return

    equipos[equipo]["disponible"] = True

    print("Equipo devuelto correctamente.")



def ver_historial():

    print("\n===== HISTORIAL =====")

    for nombre, datos in equipos.items():

        print("\nEquipo:", nombre)

        if len(datos["prestamos"]) == 0:
            print("Sin préstamos registrados.")
        else:

            for prestamo in datos["prestamos"]:

                usuario = prestamo[0]
                fecha = prestamo[1]

                print("Usuario:", usuario)
                print("Fecha:", fecha)



def agregar_equipo():

    nombre = input("\nNombre del nuevo equipo: ")

    if nombre in equipos:
        print("Ese equipo ya existe.")
        return

    equipos[nombre] = {
        "disponible": True,
        "prestamos": []
    }

    print("Equipo agregado correctamente.")



def menu():

    opcion = ""

    while opcion != "6":

        print("\n==============================")
        print(" Sistema de Préstamos")
        print("==============================")
        print("1. Ver equipos")
        print("2. Registrar préstamo")
        print("3. Devolver equipo")
        print("4. Ver historial")
        print("5. Agregar equipo")
        print("6. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            mostrar_equipos()

        elif opcion == "2":
            registrar_prestamo()

        elif opcion == "3":
            devolver_equipo()

        elif opcion == "4":
            ver_historial()

        elif opcion == "5":
            agregar_equipo()

        elif opcion == "6":
            print("Programa finalizado.")

        else:
            print("Opción no válida.")



menu()