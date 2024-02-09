def decimal_a_binario(numero):

  binario = ""
  while numero > 0:
    resto = numero % 2
    numero //= 2
    binario = str(resto) + binario
  return binario


numero = int(input("Introduce un número decimal: "))


binario = decimal_a_binario(numero)

print(f"El número {numero} en binario es: {binario}")
