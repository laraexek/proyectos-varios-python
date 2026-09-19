def monitor_balanza_comercial():
  print("=" * 95)
  print(
      "   MONITOR DE RESPALDO COMERCIAL Y PRODUCTIVIDAD (BALANZA COMERCIAL EN"
      " MM USD)"
  )
  print("=" * 95)

  # Datos base de comercio exterior (Exportaciones vs Importaciones en miles de millones USD)
  # Valores basados en reportes oficiales recientes de balanza comercial anualizada.
  datos_comerciales = {
      "CHN": {
          "nombre": "China (Yuan)",
          "exportaciones": 3380.0,
          "importaciones": 2550.0,
      },
      "USA": {
          "nombre": "Estados Unidos (Dólar)",
          "exportaciones": 2010.0,
          "importaciones": 3170.0,
      },
      "EUR": {
          "nombre": "Eurozona / Europa (Euro)",
          "exportaciones": 3100.0,
          "importaciones": 2950.0,
      },
      "JPN": {
          "nombre": "Japón (Yen)",
          "exportaciones": 720.0,
          "importaciones": 850.0,
      },
      "RUS": {
          "nombre": "Rusia (Rublo)",
          "exportaciones": 420.0,
          "importaciones": 300.0,
      },
      "CAN": {
          "nombre": "Canadá (Dólar can.)",
          "exportaciones": 570.0,
          "importaciones": 565.0,
      },
      "MEX": {
          "nombre": "México (Peso mex.)",
          "exportaciones": 590.0,
          "importaciones": 605.0,
      },
      "BRA": {
          "nombre": "Brasil (Real)",
          "exportaciones": 340.0,
          "importaciones": 270.0,
      },
      "CHL": {
          "nombre": "Chile (Peso chileno)",
          "exportaciones": 95.0,
          "importaciones": 85.0,
      },
      "PER": {
          "nombre": "Perú (Sol)",
          "exportaciones": 65.0,
          "importaciones": 55.0,
      },
      "COL": {
          "nombre": "Colombia (Peso col.)",
          "exportaciones": 50.0,
          "importaciones": 63.0,
      },
      "ECU": {
          "nombre": "Ecuador (Dólar/USD)",
          "exportaciones": 31.0,
          "importaciones": 29.0,
      },
      "VES": {
          "nombre": "Venezuela (Bolívar)",
          "exportaciones": 10.0,
          "importaciones": 12.0,
      },
  }

  print(
      f"{'País / Moneda':<30} | {'Exportaciones':<15} | {'Importaciones':<15}"
      f" | {'Balanza (Neto)':<15} | {'Estado'}"
  )
  print("-" * 95)

  for codigo, info in datos_comerciales.items():
    exp = info["exportaciones"]
    imp = info["importaciones"]
    balanza = exp - imp

    str_exp = f"${exp:,.1f}B"
    str_imp = f"${imp:,.1f}B"
    str_balanza = f"${balanza:+,.1f}B"

    # Clasificación analítica de respaldo comercial
    if balanza > 50:
      estado = "🟢 Superávit Sólido"
    elif balanza > 0:
      estado = "🟡 Superávit Leve"
    elif balanza > -30:
      estado = "🟠 Déficit Moderado"
    else:
      estado = "🔴 Déficit Estructural"

    print(
        f"{info['nombre']}".ljust(30)
        + f"| {str_exp.ljust(15)} | {str_imp.ljust(15)} |"
        + f" {str_balanza.ljust(15)} | {estado}"
    )

  print("=" * 95)
  print(
      "💡 *Análisis:* Los países con superávit sólido (como China o Rusia) demuestran"
      " un fuerte"
  )
  print(
      "respaldo productivo externo, mientras que los deficitarios dependen de"
      " factores financieros o deuda."
  )
  print("=" * 95)


if __name__ == "__main__":
  monitor_balanza_comercial()