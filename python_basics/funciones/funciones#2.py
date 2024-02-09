def contar_palabras(texto):
  
  palabras = texto.lower().split()  # Convertir a minúsculas y separar palabras
  conteo_palabras = {}
  for palabra in palabras:
    if palabra in conteo_palabras:
      conteo_palabras[palabra] += 1
    else:
      conteo_palabras[palabra] = 1
  return conteo_palabras

def palabra_mas_repetida(conteo_palabras):
  
  palabra_mas_repetida = ""
  frecuencia_mayor = 0
  for palabra, frecuencia in conteo_palabras.items():
    if frecuencia > frecuencia_mayor:
      palabra_mas_repetida = palabra
      frecuencia_mayor = frecuencia
  return palabra_mas_repetida, frecuencia_mayor


texto = input("Introduce un texto: ")

conteo_palabras = contar_palabras(texto)
palabra_mas_repetida, frecuencia_mayor = palabra_mas_repetida(conteo_palabras)


print("Palabras y frecuencias:", conteo_palabras)
print("Palabra más repetida:", palabra_mas_repetida)
print("Frecuencia de palabra más repetida:", frecuencia_mayor)
