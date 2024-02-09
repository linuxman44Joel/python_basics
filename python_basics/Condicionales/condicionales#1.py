def verificar_contrasena(contrasena_guardada):

  contrasena_introducida = input("Introduce la contraseña: ")


  contrasena_guardada = contrasena_guardada.lower()
  contrasena_introducida = contrasena_introducida.lower()

  if contrasena_guardada == contrasena_introducida:
    print("La contraseña coincide.")
  else:
    print("La contraseña no coincide.")

contrasena_guardada = "{Introduce la contraseña}"
verificar_contrasena(contrasena_guardada)
