import datetime
import requests


def calcular_proteccion_inflacion():
  print("=" * 65)
  print("    SIMULADOR ANTIDESTRUCCIÓN DE AHORROS EN BOLÍVARES")
  print("=" * 65)

  # Consultamos las tasas actuales del mercado en Venezuela
  url_venezuela = "https://ve.dolarapi.com/v1/dolares"

  try:
    resp = requests.get(url_venezuela)
    if resp.status_code != 200:
      print("[Error] No se pudo conectar con los servidores de indicadores.")
      return

    datos = resp.json()
    tasa_paralelo = None
    tasa_oficial = None

    for item in datos:
      if item.get("fuente") == "paralelo":
        tasa_paralelo = item.get("promedio")
      elif item.get("fuente") == "oficial":
        tasa_oficial = item.get("promedio")

    if not tasa_paralelo:
      print("[Error] No se encontró la tasa paralela de referencia.")
      return

    print(f"📊 Indicador Base Actual (Paralelo): {tasa_paralelo:,.2f} VES/USD")
    print(f"🏛️ Indicador Oficial (BCV): {tasa_oficial:,.2f} VES/USD")
    print("-" * 65)

    # Nota metodológica: En escenarios de devaluación constante, la variación
    # de la moneda extranjera es el reflejo directo de la pérdida de valor del bolívar.
    # Simulamos tasas de devaluación promedio basadas en comportamientos típicos recientes (ej. estimados conservadores del 0.15% al 0.5% diario).

    # Supongamos una tasa de devaluación diaria estimada del mercado (ej. 0.3% diario o recuperada de históricos)
    # Para efectos prácticos del script, calculamos proyecciones exponenciales:
    devaluacion_diaria_est = 0.0025  # 0.25% diario estimado de pérdida de valor

    # Matemáticas de interés compuesto para la inflación/devaluación
    # Fórmula: Monto_futuro = Monto_actual * (1 + tasa)^tiempo
    factor_diario = (1 + devaluacion_diaria_est) - 1
    factor_semanal = ((1 + devaluacion_diaria_est) ** 7) - 1
    factor_mensual = ((1 + devaluacion_diaria_est) ** 30) - 1

    print("📉 ESTIMACIÓN DE PÉRDIDA DE PODER ADQUISITIVO (INFLACIÓN CAMBIARIA):")
    print(f"   * Estimado de devaluación Diaria:  ~{factor_diario * 100:.2f}%")
    print(f"   * Estimado de devaluación Semanal: ~{factor_semanal * 100:.2f}%")
    print(f"   * Estimado de devaluación Mensual: ~{factor_mensual * 100:.2f}%")
    print("-" * 65)

    print("🛡️ TASA DE RENDIMIENTO REQUERIDA PARA PROTEGER TUS AHORROS:")
    print(
        "Para que tu dinero en bolívares **no pierda valor**, cualquier"
        " instrumento de ahorro, fondo o rendimiento al que destines tus"
        " ingresos debe ofrecerte NETAMENTE al menos las siguientes tasas de"
        " ganancia:"
    )
    print(
        f"   👉 Debes buscar opciones que rinden más de:"
        f" **{factor_mensual * 100:.2f}% Mensual**"
    )
    print(
        "   💡 *Consejo práctico:* En la economía venezolana, la defensa más"
        " directa contra esta curva es migrar el excedente de ahorro a"
        " activos de refugio de valor estables (como divisas físicas o"
        " equivalentes digitales seguros) para anular el impacto de la"
        " devaluación diaria."
    )
    print("=" * 65)

  except Exception as e:
    print(f"[Error de ejecución]: {e}")


if __name__ == "__main__":
  calcular_proteccion_inflacion()