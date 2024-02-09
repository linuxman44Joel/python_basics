
def mostrar_triangulo_rectangulo(altura):
    for i in range(1, altura + 1):
        for j in range(1, i + 1):
            print("*", end="")
        print()

altura = int(input("Introduzca un número entero: "))

mostrar_triangulo_rectangulo(altura)