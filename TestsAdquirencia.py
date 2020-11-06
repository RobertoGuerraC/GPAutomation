from PageBatch import *
from PageObject import *

# Adquirencia Establecimientos

batch = BatchAdquirencia()

get('https://v2batch-web-qa.global.globalprocessing.net.ar/')

# Creamos funcion para crear un establecimiento
def crear_establecimiento():

    iniciar_sesion()
    # adquirencia.crear_establecimientos()


def ejecutar_presentacion():

    iniciar_sesion()
    batch.proceso_presentacion()


ejecutar_presentacion()
