
asignaturas = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]


notas = []
for asignatura in asignaturas:
  nota = float(input(f"Introduce la nota de {asignatura}: "))
  notas.append(nota)


asignaturas_repetir = []
for i in range(len(asignaturas)):
  if notas[i] < 5:
    asignaturas_repetir.append(asignaturas[i])


if asignaturas_repetir:
  print("Las asignaturas que tienes que repetir son:")
  for asignatura in asignaturas_repetir:
    print(f" - {asignatura}")
else:
  print("¡Enhorabuena! Has aprobado todas las asignaturas.")
