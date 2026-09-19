import os

print("--- Monitor de RAM para Pedrinn ---")

# Este comando le pide a Linux la info de la memoria
os.system("free -h")

print("\n¡Listo! Si ves que 'libre' es poco, recuerda usar la escoba.")
