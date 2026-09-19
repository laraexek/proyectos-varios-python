import requests

# Diccionario con regiones y coordenadas (Latitud, Longitud) de ciudades clave
CIUDADES_VZLA = {
    "Caracas (Centro)": {"lat": 10.4880, "lon": -66.8791},
    "Maracaibo (Zulia/Occidente)": {"lat": 10.6427, "lon": -71.6125},
    "Valencia (Centro)": {"lat": 10.1620, "lon": -68.0077},
    "Barquisimeto (Lara/Centro-Occidente)": {"lat": 10.0647, "lon": -69.3570},
    "Mérida (Andes)": {"lat": 8.5983, "lon": -71.1450},
    "Puerto La Cruz (Oriente)": {"lat": 10.2138, "lon": -64.6328},
    "San Fernando de Apure (Llanos)": {"lat": 7.8878, "lon": -67.4724},
    "Puerto Ordaz (Guayana/Sur)": {"lat": 8.2978, "lon": -62.7115},
    "Porlamar (Margarita/Insular)": {"lat": 10.9577, "lon": -63.8697}
}

# Códigos de estado del tiempo de Open-Meteo a texto en español
WMO_CODES = {
    0: "☀️ Despejado",
    1: "🌤️ Principalmente despejado",
    2: "⛅ Parcialmente nublado",
    3: "☁️ Nublado",
    45: "🌫️ Niebla",
    51: "🌦️ Llovizna ligera",
    61: "🌧️ Lluvia moderada",
    63: "🌧️ Lluvia fuerte",
    80: "🌩️ Chubascos",
    95: "⛈️ Tormenta eléctrica"
}

def consultar_clima():
    print("=" * 65)
    print("        🌤️ REPORTE DEL CLIMA - REGIONES DE VENEZUELA 🇻🇪")
    print("=" * 65)

    for ciudad, coords in CIUDADES_VZLA.items():
        # Endpoint de Open-Meteo
        url = f"https://api.open-meteo.com/v1/forecast?latitude={coords['lat']}&longitude={coords['lon']}&current_weather=true"

        try:
            response = requests.get(url, timeout=10)
            if response.status_code == 200:
                data = response.json()["current_weather"]
                
                temp = data["temperature"]
                viento = data["windspeed"]
                code = data["weathercode"]
                estado = WMO_CODES.get(code, "🌡️ Variable")

                # Salida alineada para la terminal
                print(f"📍 {ciudad:<38}")
                print(f"   ├─ Estado:      {estado}")
                print(f"   ├─ Temperatura: {temp} °C")
                print(f"   └─ Viento:      {viento} km/h")
                print("-" * 65)
            else:
                print(f"❌ Error al consultar {ciudad}")

        except Exception as e:
            print(f"⚠️ Error de conexión para {ciudad}: {e}")

if __name__ == "__main__":
    consultar_clima()