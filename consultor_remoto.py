import os
import shutil

# Esta es la ruta hacia la carpeta del cliente en el Escritorio
ruta_cliente = os.path.expanduser("~/Escritorio/CLIENTE_REMOTO")

print(f"🌐 Conectando remotamente a: {ruta_cliente}...")

if os.path.exists(ruta_cliente):
    # Creamos una carpeta de 'Backup' para el cliente
    ruta_backup = os.path.join(ruta_cliente, "Mantenimiento_Preventivo")
    os.makedirs(ruta_backup, exist_ok=True)
    
    print("✅ Acceso concedido. Organizando archivos sueltos...")
    
    # Buscamos archivos .txt para asegurar su respaldo
    encontrados = 0
    for archivo in os.listdir(ruta_cliente):
        if archivo.endswith(".txt"):
            shutil.move(os.path.join(ruta_cliente, archivo), os.path.join(ruta_backup, archivo))
            print(f"   📥 Asegurado: {archivo}")
            encontrados += 1
    
    if encontrados == 0:
        print("   ℹ️ No hay archivos pendientes de organizar.")
else:
    print("❌ Error de red: No se encontró la ruta del cliente.")

print("\n--- 🔌 DESCONECTADO DEL CLIENTE ---")
