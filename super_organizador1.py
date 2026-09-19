import os
import shutil
import datetime

# 1. EL "CEREBRO" DEL SISTEMA (Aquí es donde añades o quitas lo que quieras)
# Si mañana es un hotel, cambias esto por ["Habitacion", "Minibar", "Spa"]
productos_objetivo = ["Tornillo", "Martillo", "Clavo", "Pintura" ]

inventario = {}
precios = {}

# 2. CONTEO ROBUSTO
archivos = os.listdir('.')
for prod in productos_objetivo:
    # Esta línea busca sin importar si es Mayúscula o Minúscula
    encontrados = [f for f in archivos if prod.lower() in f.lower() and os.path.isfile(f)]
    cantidad = len(encontrados)
    inventario[prod] = cantidad
    
    # Mensaje de depuración para que veas qué está contando en la terminal
    if cantidad > 0:
        print(f"📦 Se encontraron {cantidad} archivos de {prod}")

# 3. PEDIR PRECIOS CON EL "PARACAÍDAS" (Try/Except)
print(f"--- 🛠️ Auditoría del día: {datetime.datetime.now().strftime('%d/%m/%Y')} ---")
for prod in productos_objetivo:
    try:
        valor = float(input(f"¿Precio actual de {prod}?: "))
        precios[prod] = valor
    except ValueError:
        print(f"⚠️ Error al teclear. Asignando precio de respaldo para {prod}.")
        precios[prod] = 1.0  # Precio base por si acaso

# 4. CREAR CARPETAS Y MOVER ARCHIVOS AUTOMÁTICAMENTE
for prod in productos_objetivo:
    carpeta = f"FERRETERIA_{prod.upper()}S"
    os.makedirs(carpeta, exist_ok=True)
    
    for f in archivos:
        if prod.lower() in f.lower() and os.path.isfile(f):
            shutil.move(f, os.path.join(carpeta, f))

# 5. GENERAR REPORTE CON TOTAL GENERAL
ahora = datetime.datetime.now()
nombre_archivo = ahora.strftime("REPORTE_%Y-%m-%d_%H-%M.csv")
total_general = 0

with open(nombre_archivo, "w") as f:
    f.write("Producto,Cantidad,Precio,Subtotal\n")
    for prod in productos_objetivo:
        subtotal = inventario[prod] * precios[prod]
        total_general += subtotal
        f.write(f"{prod},{inventario[prod]},{precios[prod]},{subtotal}\n")
    f.write(f"\nTOTAL,,, {total_general}")

print(f"\n✅ ¡Sistema procesado con éxito!")
print(f"💰 Total en caja: {total_general}")
