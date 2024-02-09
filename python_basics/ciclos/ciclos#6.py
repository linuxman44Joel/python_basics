def calcular_total_factura(cantidad, iva=21):
  """
  Calcula el total de una factura con IVA.

  Args:
    cantidad: La cantidad sin IVA.
    iva: El porcentaje de IVA a aplicar.

  Returns:
    El total de la factura.
  """
  total = cantidad * (1 + iva / 100)
  return total

# Pedir la cantidad al usuario
cantidad = float(input("Introduce la cantidad sin IVA: "))

# Pedir el IVA al usuario
iva = float(input("Introduce el porcentaje de IVA: "))

# Calcular el total de la factura
total = calcular_total_factura(cantidad, iva)

# Mostrar el total de la factura
print(f"Total de la factura: {total}")
