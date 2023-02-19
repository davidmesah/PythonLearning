

def es_bisiesto(t):
    return t % 400 == 0 or (t % 100 != 0 and t % 4 == 0)

print("Comprobador de años bisiestos")
fecha = int(input("Escriba un año y le diré si es bisiesto: "))
if es_bisiesto(fecha):
    print("El año", fecha, "es un año bisiesto.")
else:
    print("El año", fecha, "no es un año bisiesto.")


