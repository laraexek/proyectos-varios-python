def monitor_pib_global():
  print("=" * 105)
  print(
      "   MONITOR DE EVOLUCIÓN DEL PIB: ÚLTIMOS 5 AÑOS (EN MILES DE MILLONES"
      " DE USD)"
  )
  print("=" * 105)

  # Base de datos estructurada con el PIB nominal (en MM USD) de los últimos 5 años
  # Valores basados en reportes macroeconómicos recientes (FMI / Banco Mundial)
  datos_pib = {
      "CHN": {
          "nombre": "China (Yuan)",
          "pib": [17750.0, 17960.0, 17790.0, 18530.0, 19370.0],
      },
      "USA": {
          "nombre": "Estados Unidos (Dólar)",
          "pib": [23320.0, 25460.0, 27360.0, 28780.0, 29850.0],
      },
      "EUR": {
          "nombre": "Eurozona / Europa (Euro)",
          "pib": [14260.0, 14080.0, 15120.0, 15500.0, 15900.0],
      },
      "JPN": {
          "nombre": "Japón (Yen)",
          "pib": [4940.0, 4230.0, 4210.0, 4110.0, 4200.0],
      },
      "CAN": {
          "nombre": "Canadá (Dólar can.)",
          "pib": [2000.0, 2140.0, 2140.0, 2240.0, 2320.0],
      },
      "MEX": {
          "nombre": "México (Peso mex.)",
          "pib": [1290.0, 1470.0, 1790.0, 1850.0, 1920.0],
      },
      "BRA": {
          "nombre": "Brasil (Real)",
          "pib": [1650.0, 1920.0, 2130.0, 2190.0, 2270.0],
      },
      "ARG": {
          "nombre": "Argentina (Peso arg.)",
          "pib": [487.0, 632.0, 641.0, 604.0, 630.0],
      },
      "COL": {
          "nombre": "Colombia (Peso col.)",
          "pib": [314.0, 344.0, 364.0, 381.0, 398.0],
      },
      "CHL": {
          "nombre": "Chile (Peso chileno)",
          "pib": [317.0, 301.0, 310.0, 316.0, 330.0],
      },
      "PER": {
          "nombre": "Perú (Sol)",
          "pib": [226.0, 243.0, 254.0, 268.0, 279.0],
      },
      "ECU": {
          "nombre": "Ecuador (Dólar/USD)",
          "pib": [106.0, 115.0, 119.0, 122.0, 126.0],
      },
      "VES": {
          "nombre": "Venezuela (Bolívar)",
          "pib": [85.0, 102.0, 108.0, 105.0, 110.0],
      },
  }

  # Cabecera de la tabla con los últimos 5 años
  print(
      f"{'País / Moneda':<28} | {'2021':<10} | {'2022':<10} | {'2023':<10} |"
      f" {'2024':<10} | {'2025 (Est.)':<12} | Tendencia"
  )
  print("-" * 105)

  for codigo, info in datos_pib.items():
    pib_vals = info["pib"]
    # Formatear cada año en miles de millones ($XXX.X B)
    s_21 = f"${pib_vals[0]:,.1f}B"
    s_22 = f"${pib_vals[1]:,.1f}B"
    s_23 = f"${pib_vals[2]:,.1f}B"
    s_24 = f"${pib_vals[3]:,.1f}B"
    s_25 = f"${pib_vals[4]:,.1f}B"

    # Análisis simple de tendencia comparando el primer año con el último de la serie
    if pib_vals[4] > pib_vals[0]:
      tendencia = "🟢 Crecimiento"
    elif pib_vals[4] == pib_vals[0]:
      tendencia = "🟡 Estable"
    else:
      tendencia = "🔴 Contracción"

    print(
        f"{info['nombre']}".ljust(28)
        + f"| {s_21.ljust(10)} | {s_22.ljust(10)} | {s_23.ljust(10)} |"
        + f" {s_24.ljust(10)} | {s_25.ljust(12)} | {tendencia}"
    )

  print("=" * 105)
  print(
      "💡 *Análisis:* El seguimiento plurianual del PIB permite identificar el"
      " dinamismo económico"
  )
  print(
      "estructural y la robustez macroeconómica a mediano plazo de cada cono"
      " monetario."
  )
  print("=" * 105)


if __name__ == "__main__":
  monitor_pib_global()