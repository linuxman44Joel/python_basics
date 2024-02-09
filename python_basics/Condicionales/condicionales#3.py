def determinar_grupo(nombre, sexo):

  nombre_en_mayusculas = nombre.upper()

  if sexo == "H":
    if nombre_en_mayusculas[0] >= "N":
      grupo = "A"
    else:
      grupo = "B"
  elif sexo == "M":
    if nombre_en_mayusculas[0] < "M":
      grupo = "A"
    else:
      grupo = "B"
  else:
    print("Sexo no válido.")
    return

  print(f"El usuario pertenece al grupo {grupo}.")

nombre = input("Introduce tu nombre: ")
sexo = input("Introduce tu sexo (H/M): ")

determinar_grupo(nombre, sexo)
