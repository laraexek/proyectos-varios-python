import requests


def consultar_tasas_bolivar():
  print("=" * 65)
  print("      MONITOR DE CONVERSIÓN DE MONEDAS (Base: Bolívar VES)")
  print("=" * 65)

  # Usamos una API abierta global para obtener tasas con respecto al Dólar (USD)
  url = "https://open.er-api.com/v6/latest/USD"

  try:
    respuesta = requests.get(url)
    if respuesta.status_code == 200:
      datos = respuesta.json()
      rates = datos.get("rates", {})

      # Obtenemos cuánto vale 1 USD en Bolívares (VES)
      ves_por_usd = rates.get("VES")

      if not ves_por_usd:
        print(
            "[Error] No se encontró la tasa para el Bolívar (VES) en el"
            " servidor."
        )
        return

      print(f"💱 Tasa de referencia base: 1 USD = {ves_por_usd:,.2f} VES\n")
      print("Calculando equivalencias frente a otras monedas...\n")

      # Monedas de interés a comparar (Código ISO y Nombre amigable)
      monedas_interes = {
          "COP": "Peso colombiano",
          "PEN": "Sol peruano",
          "ARS": "Peso argentino",
          "EUR": "Euro",
          "BRL": "Real brasileño",
          "CLP": "Peso chileno",
      }

      print(f"{'Moneda':<25} | {'Valor en la moneda extranjera':<15} | {'Equivalente en Bolívares'}")
      print("-" * 65)

      for codigo, nombre in monedas_interes.items():
        tasa_usd_a_moneda = rates.get(codigo)
        if tasa_usd_a_moneda:
          # Matemáticas financieras: Cruzamos los valores a través del USD
          # Cuántos Bolívares cuesta 1 unidad de la moneda extranjera
          valor_en_ves = ves_por_usd / tasa_usd_a_moneda
          print(f"{nombre} ({codigo})".ljust(27) + f"| 1 {codigo} = {valor_en_ves:,.4f} VES")
        else:
          print(f"{nombre} ({codigo})".ljust(27) + "| No disponible")

      print("=" * 65)

    else:
      print(f"[Error] Conexión fallida. Código: {respuesta.status_code}")

  except Exception as e:
    print(f"[Error de red]: {e}")


if __name__ == "__main__":
  consultar_tasas_bolivar()