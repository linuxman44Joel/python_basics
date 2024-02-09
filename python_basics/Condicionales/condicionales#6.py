# Función para mostrar el menú vegetariano
def mostrar_menu_vegetariano():
    print("Ingredientes vegetarianos:")
    print("1. Pimiento")
    print("2. Tofu")


# Función para mostrar el menú no vegetariano
def mostrar_menu_no_vegetariano():
    print("Ingredientes no vegetarianos:")
    print("1. Peperoni")
    print("2. Jamón")
    print("3. Salmón")


# Función para obtener la elección del usuario
def obtener_eleccion_usuario():
    while True:
        eleccion = input("¿Qué tipo de pizza desea? (V/NV): ")
        if eleccion.upper() not in ["V", "NV"]:
            print("Opción no válida. Introduzca V para vegetariana o NV para no vegetariana.")
        else:
            return eleccion.upper()


# Función para obtener el ingrediente elegido por el usuario
def obtener_ingrediente_elegido(es_vegetariano):
    if es_vegetariano:
        mostrar_menu_vegetariano()
    else:
        mostrar_menu_no_vegetariano()

    while True:
        ingrediente = input("Elija su ingrediente: ")
        if not ingrediente.isdigit() or int(ingrediente) not in range(1, 4):
            print("Opción no válida. Introduzca un número del 1 al 3.")
        else:
            return int(ingrediente)


# Función para mostrar la pizza elegida por el usuario
def mostrar_pizza_elegida(es_vegetariano, ingrediente_elegido):
    if es_vegetariano:
        ingrediente = "Pimiento" if ingrediente_elegido == 1 else "Tofu"
    else:
        ingrediente = "Peperoni" if ingrediente_elegido == 1 else "Jamón" if ingrediente_elegido == 2 else "Salmón"

    print(f"Su pizza es {ingrediente}, mozzarella, tomate.")
    if es_vegetariano:
        print("Su pizza es vegetariana.")
    else:
        print("Su pizza no es vegetariana.")


# Obtener la elección del usuario
eleccion_usuario = obtener_eleccion_usuario()

# Obtener el ingrediente elegido por el usuario
ingrediente_elegido = obtener_ingrediente_elegido(eleccion_usuario == "V")

# Mostrar la pizza elegida por el usuario
mostrar_pizza_elegida(eleccion_usuario == "V", ingrediente_elegido)