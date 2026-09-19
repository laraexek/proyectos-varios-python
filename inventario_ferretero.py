import os
import shutil

# Reglas de categorías y su contador inicial
categorias = {
    "Tornillo": "FERRETERIA/CORTANTES/TORNILLOS",
    "Martillo": "FERRETERIA/HERRAMIENTAS/MANUALES",
    "Clavo": "FERRETERIA/CORTANTES/CLAVOS"
}

# Diccionario para llevar la cuenta
conteo_productos = {"Tornillo": 0, "Martillo": 0, "Clavo": 0}

print("--- 🏪 SISTEMA DE INVENTARIO FERRETERO V1.0 ---")

archivos = os.listdir(".")

for archivo in archivos:
    for palabra_clave, ruta in categorias.items():
        if palabra_clave.lower() in archivo.lower():
            # Crear carpeta y mover
            os.makedirs(ruta, exist_ok=True)
            shutil.move(archivo, os.path.join(ruta, archivo))
            
            # ¡AQUÍ ESTÁ EL TRUCO! Sumamos uno al contador
            conteo_productos[palabra_clave] += 1
            break

# Generamos el reporte final para el dueño
print("\n📊 REPORTE DE INVENTARIO GENERADO:")
print("-" * 30)
for producto, cantidad in conteo_productos.items():
    print(f"📍 {producto}: {cantidad} unidades organizadas.")
print("-" * 30)
print("✅ Archivos movidos y base de datos actualizada.")
