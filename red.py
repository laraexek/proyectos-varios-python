import urllib.request
import time

print("--- 🌍 Conectando con el mundo exterior ---")

try:
    # Intentamos abrir la página de Google para ver si hay internet
    inicio = time.time()
    urllib.request.urlopen("http://www.google.com", timeout=5)
    fin = time.time()
    
    # Calculamos cuánto tardó en milisegundos
    latencia = round((fin - inicio) * 1000)
    
    print("✅ ¡Conexión exitosa!")
    print(f"🚀 Google respondió en: {latencia} ms")
    print("--- Tu Python ya sabe hablar con internet ---")

except Exception as e:
    print("❌ Error: No se pudo conectar. Revisa tu internet.")
    print(f"Detalle: {e}")
