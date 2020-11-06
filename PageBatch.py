from BasePageObject import *
import openpyxl
# import BaseDatos
from Logger import *

logger.info('estoy aqui')
# Selenium waits 10sg before thrown an exception
driver.implicitly_wait(10)

# Openning the excel book with all the data
scanntech_doc = openpyxl.load_workbook('Scanntech.xlsx')

# batch_data = scanntech_doc['Batchs']

class BatchAdquirencia:

    logger.info('Asignando valor de xpath a variables')
    procesos = '//*[@id="home"]/nav/ul/li[3]/a'
    entidad_filtro = '//*[@id="entidades"]'
    entidad_701 = '//*[@id="entidades"]/option[6]'
    nombre_filtro = '//*[@id="nombre_proceso"]'
    buscar = '/html/body/div/div[1]/form/fieldset[3]/button'

    ejecutar_presentacion = '//*[@id="tabla_procesos_body"]/tr/td[5]/a/i'

    parametro2 = '//*[@id="parametro_02"]'

    confirmar = '//*[@id="boton_confirmacion_lanzamiento"]'
    lanzar = '//*[@id="boton_lanzamiento"]'

    historial = '//*[@id="home"]/nav/ul/li[4]/a'

    def proceso_presentacion(self):
        logger.debug('Empieza lanzamiento de proceso de presentacion')
        click(self.procesos)
        click(self.entidad_filtro)
        click(self.entidad_701)
        send_keys(self.nombre_filtro, 'Presentacion Comercio')
        click(self.buscar)
        try:
            click(self.ejecutar_presentacion)
        except:
            click(self.ejecutar_presentacion)

        send_keys(self.parametro2, '20201103')
        click(self.confirmar)
        click(self.lanzar)
        click(self.historial)
        try:
            print(driver.find_element_by_xpath('//*[@id="ejecuciones_body"]/tr[1]/td[1]/span').get_attribute('title'))
            logger.debug('Todo bien')
        except:
            logger.error('No funciono')
