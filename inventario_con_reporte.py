import os
import shutil
import datetime
# 1. RUTAS: para saber a donde mover cada archivo
categorias = {
	"Tornillo": "FERRETERIA/TORNILLOS",
	"Martillo": "FERRETERIA/MARTILLOS",
	"Clavo": "FERRETERIA/CLAVOS"
}
# 2. DINERO - Con protección contra errores de dedo
print("\n--- 🛠️ Configuración de Precios del Día ---")

try:
    precio_tornillo = float(input("¿Precio del Tornillo hoy? (ej: 0.50): "))
    precio_martillo = float(input("¿Precio del Martillo hoy? (ej: 15.0): "))
    precio_clavo = float(input("¿Precio del Clavo hoy? (ej: 0.10): "))
except ValueError:
    # Si escribes una letra o dejas vacío, entra aquí:
    print("\n⚠️  ¡Oops! No escribiste un número válido.")
    print("Sugerencia: Usa el punto (.) para decimales, no la coma (,).")
    print("Cargando precios de respaldo para no detener el reporte...")
    
    precio_tornillo = 0.50
    precio_martillo = 15.00
    precio_clavo = 0.10

precios = {
    "Tornillo": precio_tornillo,
    "Martillo": precio_martillo,
    "Clavo": precio_clavo
}
# 3. CONTAOR: Para saber cuantos archivos movios
inventario = {"Tornillo": 0, "Martillo": 0, "Clavo": 0}

# 4. LÓGICA DE ORGANIZACIÓN Y MOVIMIENTO
for archivo in os.listdir("."):
    # Recorremos el diccionario de categorías para saber a dónde mover cada archivo
    for clave, ruta in categorias.items():
        if clave.lower() in archivo.lower():
            # Creamos la carpeta si no existe
            os.makedirs(ruta, exist_ok=True)
            
            # MOVEMOS el archivo a su nueva casa
            shutil.move(archivo, os.path.join(ruta, archivo))
            
            # Sumamos al inventario
            inventario[clave] += 1
            print(f"✅ Movido: {archivo} -> {ruta}")
            break

# 5. GENERACIÓN DEL REPORTE CON SUMA TOTAL
total_dinero = 0  # <--- Aquí empezamos el contador en cero
ahora = datetime.datetime.now()
fecha_formateada = ahora.strftime("%Y-%m-%d_%H-%M")
nombre_archivo = f"REPORTE_{fecha_formateada}.csv"
with open(nombre_archivo, "w") as f:
    f.write("Producto,Cantidad,Precio Unitario,Subtotal\n")
    
    for producto, cantidad in inventario.items():
        precio = precios[producto]
        subtotal = cantidad * precio
        
        # Sumamos el subtotal al gran total
        total_dinero += subtotal 
        
        # Escribimos la fila del producto
        f.write(f"{producto},{cantidad},{precio},{subtotal}\n")
    
    # AL FINAL: Escribimos una fila especial con el TOTAL GENERAL
    f.write(f"\nTOTAL,,, {total_dinero}\n")

print(f"✅ Reporte generado: {nombre_archivo}")
print(f"💰 El total acumulado es: {total_dinero}")
