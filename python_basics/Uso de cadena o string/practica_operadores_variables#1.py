def mostrar_nombre_completo(nombre_completo):
 
  print(f"Nombre completo en minúsculas: {nombre_completo.lower()}")
  print(f"Nombre completo en mayúsculas: {nombre_completo.upper()}")
  print(f"Nombre completo con mayúsculas al inicio: {nombre_completo.title()}")


nombre_completo = input("Introduce tu nombre completo: ")

mostrar_nombre_completo(nombre_completo)
