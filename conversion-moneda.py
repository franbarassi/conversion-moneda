# Valor actual del Euro y Dolar con respecto al Peso Mexicano
tipo_cambio_eur_a_mxn = 23.70
tipo_cambio_usd_a_mxn = 20.75

while True:
    tipo_conversion = input("Ingrese la moneda origen para la conversión (EUR/USD): ").lower()
    if tipo_conversion in ("eur", "usd"):
        break
    else:
        print("El dato ingresado no es válido.")

while True:
    try:
        monto_a_convertir = float(input("Ingrese el monto a convertir: "))
        break
    except ValueError:
        print("El dato ingresado no es válido.")

# Conversión utilizando el tipo de cambio correspondiente
if tipo_conversion == "eur":
    resultado = monto_a_convertir * tipo_cambio_eur_a_mxn
    moneda = "EUR"
elif tipo_conversion == "usd":
    resultado = monto_a_convertir * tipo_cambio_usd_a_mxn
    moneda = "USD"

print(f"El monto de {monto_a_convertir} {moneda} es: {resultado:.2f} pesos mexicanos.")