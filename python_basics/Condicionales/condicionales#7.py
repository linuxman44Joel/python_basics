# Pedir datos al usuario
cantidad = float(input("Introduce la cantidad a invertir: "))
interes = float(input("Introduce el interés anual (en %): "))
anios = int(input("Introduce el número de años: "))

capital_obtenido = []
for i in range(anios):
  capital_obtenido.append(cantidad * (1 + interes / 100) ** (i + 1))

for i in range(anios):
  print(f"Año {i + 1}: {capital_obtenido[i]:.2f}€")
