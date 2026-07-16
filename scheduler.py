# scheduler.py
import schedule
import time
import threading

def iniciar_hilo_planificador():
    """Ejecuta el ciclo de reloj del scheduler en un hilo secundario de fondo."""
    def bucle():
        while True:
            schedule.run_pending()
            time.sleep(1)
            
    hilo = threading.Thread(target=bucle)
    hilo.daemon = True
    hilo.start()
    print("⏳ Hilo del Scheduler activo y patrullando el reloj del sistema...")


