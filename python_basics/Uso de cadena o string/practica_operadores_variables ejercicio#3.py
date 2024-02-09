def mostrar_numero_telefono(numero_telefono):
  

  prefijo, numero, extension = numero_telefono.split('-')

  numero = numero.replace(prefijo, '')
  numero = numero.replace(extension, '')


  return numero


if __name__ == '__main__':
  
  numero_telefono = input('Introduce un número de teléfono: ')

  
  print(mostrar_numero_telefono(numero_telefono))