def evaluar_empleado(nombre, puntuacion):
 
 
  if puntuacion < 0.4:
    nivel = "Inaceptable"
    recompensa = 0
  elif puntuacion >= 0.4 and puntuacion < 0.6:
    nivel = "Aceptable"
    recompensa = 2400 * 0.4
  else:
    nivel = "Meritorio"
    recompensa = 2400 * 0.6

  print(f"Nombre: {nombre}")
  print(f"Nivel: {nivel}")
  print(f"Recompensa: {recompensa}€")


nombre = input("Introduce el nombre del empleado: ")
puntuacion = float(input("Introduce la puntuación del empleado: "))

evaluar_empleado(nombre, puntuacion)
