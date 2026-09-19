import requests
from bs4 import BeautifulSoup
import urllib3

# Deshabilitar advertencias SSL del BCV
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:120.0) Gecko/20100101 Firefox/120.0'
}

def consultar_pagina_tabla(url, titulo):
    print(f"\n=======================================================")
    print(f" 📊 {titulo}")
    print(f"=======================================================")
    
    try:
        response = requests.get(url, headers=HEADERS, verify=False, timeout=15)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            tablas = soup.find_all('table')
            
            if tablas:
                for tabla in tablas:
                    filas = tabla.find_all('tr')
                    for fila in filas:
                        cols = [c.get_text().strip() for c in fila.find_all(['td', 'th'])]
                        if cols:
                            # Formato alineado estilo columna
                            print(" | ".join(f"{col:<20}" for col in cols))
            else:
                print("⚠️ No se encontraron tablas estructuradas en esta sección.")
        else:
            print(f"❌ Error al consultar la página (Código {response.status_code})")
    except Exception as e:
        print(f"⚠️ Error de conexión: {e}")

if __name__ == "__main__":
    print("🚀 INICIANDO CONSULTA DE TASAS E INDICADORES - BCV")
    
    # 1. Consultar Tasas del Mercado Cambiario Bancario
    consultar_pagina_tabla(
        "https://www.bcv.org.ve/tasas-informativas-sistema-bancario", 
        "TASAS INFORMATIVAS BANCARIAS (MERCADO CAMBIARIO)"
    )
    
    # 2. Consultar Tasas de Interés (Crédito y Ahorro)
    consultar_pagina_tabla(
        "https://www.bcv.org.ve/estadisticas/tasas-de-interes", 
        "TASAS DE INTERÉS SISTEMA FINANCIERO"
    )