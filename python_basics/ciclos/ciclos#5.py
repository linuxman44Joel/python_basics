# Aqui el Diccionario con los créditos de las asignaturas
asignaturas = {
  "Matemáticas": 6,
  "Física": 4,
  "Química": 5,
}

for asignatura, creditos in asignaturas.items():
  print(f"{asignatura} tiene {creditos} créditos")

total_creditos = sum(asignaturas.values())
print(f"Total de créditos: {total_creditos}")
