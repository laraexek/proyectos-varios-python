import os
import subprocess
import time

def monitorear_inestabilidad():
    print("--- Vigilante de Integridad Eléctrica (Modo Fedora) ---")
    
    
    # Esta es la línea que debes verificar o actualizar
    # Ahora solo miramos lo ocurrido en el ÚLTIMO MINUTO (--since "1 min ago")
    comando = "sudo journalctl --since '1 min ago' | grep -Ei 'voltage|power|battery|acpi|PRUEBA'"
    
    while True:
        try:
            # Revisamos si el Kernel ha reportado errores de energía o voltaje
            resultado = subprocess.check_output(comando, shell=True).decode('utf-8')
            
            # Palabras clave que indican que el hardware está sufriendo
            alertas = ["voltage", "power", "acpi", "critical"]
            
            if any(palabra in resultado.lower() for palabra in alertas):
                print("\n[PRECAUCIÓN] Se detectaron anomalías de hardware en los logs.")
                print("El sistema eléctrico podría estar inestable.")
                # Esto lanzará un aviso visual en Fedora que dura 10 segundos
            os.system('notify-send -u critical "⚠️ ALERTA ELÉCTRICA" "Inestabilidad detectada. ¡Guarda y apaga pronto!"')
            
            time.sleep(10)
            
        except Exception as e:
            time.sleep(10)

if __name__ == "__main__":
    monitorear_inestabilidad()




