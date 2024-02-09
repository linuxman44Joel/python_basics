def invertir_frase(frase):
  palabras = frase.split()
  palabras_invertidas = palabras[::-1]

  frase_invertida = " ".join(palabras_invertidas)

  print(f"Frase invertida: {frase_invertida}")

frase = input("Introduce una frase: ")
invertir_frase(frase)
