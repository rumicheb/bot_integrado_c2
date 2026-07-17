import schedule
import time
import threading

def iniciar_hilo_planificador():
    def bucle():
        while True:
            schedule.run_pending()
            time.sleep(1)

    hilo_planificador = threading.Thread(target=bucle)
    hilo_planificador.daemon = True
    hilo_planificador.start()
    print( "Planificador iniciado en un hilo separado." )
