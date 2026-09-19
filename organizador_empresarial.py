import os
import shutil

def organizador_empresarial(archivo_datos, carpeta_raiz):
    print(f"--- 🏢 INICIANDO ORGANIZACIÓN PARA: {carpeta_raiz} ---")
    
    if not os.path.exists(archivo_datos):
        print(f"❌ No se encontró el archivo: {archivo_datos}")
        return

    with open(archivo_datos, "r") as f:
        for linea in f:
            # Separamos los 3 niveles de categoría
            # Ejemplo: Categoria, Tipo, Nombre
            partes = linea.strip().split(",")
            
            if len(partes) == 3:
                cat, tipo, nombre = partes
                
                # Creamos la ruta (Ej: Farmacia/Antibioticos/Liquido/Amoxicilina)
                ruta_final = os.path.join(carpeta_raiz, cat, tipo, nombre)
                os.makedirs(ruta_final, exist_ok=True)
                
                # Simulación de mover el reporte o archivo de stock
                archivo_stock = f"reporte_{nombre}.txt"
                # Si el archivo existe, lo movemos a su nueva carpeta
                if os.path.exists(archivo_stock):
                    shutil.move(archivo_stock, os.path.join(ruta_final, archivo_stock))
                    print(f"📦 Stock de {nombre} organizado en {cat}.")
                else:
                    print(f"📂 Carpeta creada para {nombre} (Sin archivo pendiente).")

# --- AQUÍ DECIDES PARA QUIÉN TRABAJAS HOY ---
# Solo tienes que cambiar estas dos líneas según el cliente:
organizador_empresarial("insumos_medicos.txt", "FARMACIA_SISTEMA")
# organizador_empresarial("insumos_medicos.txt", "FARMACIA_SISTEMA")
