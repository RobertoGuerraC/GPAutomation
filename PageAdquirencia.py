from BasePageObject import *
import openpyxl
from BaseDatos import *
from Logger import *

# Selenium waits 10sg before thrown an exception
driver.implicitly_wait(10)

# Openning the excel book with all the data
scanntech_doc = openpyxl.load_workbook('Scanntech.xlsx')

estab_data = scanntech_doc['Establecimientos']
comercio_data = scanntech_doc['Comercios']

# Adquirencia Class, all the paths will be in here.
class Adquirencia:

    # We can only use xpath -
    logger.info('Creatin paths of adquirencia')

    adq_button = '//*[@id="menu"]/ul/li[6]/a'

    gestion_establecimientos = '//*[@id="menu"]/ul/li[6]/ul/li[1]/a'

    venta_liq = '//*[@id="menu"]/ul/li[6]/ul/li[2]/a'
    modeloTasa = '//*[@id="menu"]/ul/li[6]/ul/li[2]/ul/li[1]/a'
    habilitEst = '//*[@id="menu"]/ul/li[6]/ul/li[2]/ul/li[2]/a'

    comercios = '//*[@id="menu"]/ul/li[6]/ul/li[3]/a'
    comercios_gestion = '//*[@id="menu"]/ul/li[6]/ul/li[3]/ul/li[1]/a'
    comercios_param = '//*[@id="menu"]/ul/li[6]/ul/li[3]/ul/li[2]/a'
    comercios_promo = '//*[@id="menu"]/ul/li[6]/ul/li[3]/ul/li[2]/ul/li[1]/a'
    comercios_cierres = '//*[@id="menu"]/ul/li[6]/ul/li[3]/ul/li[2]/ul/li[2]/a'
    comercios_pago = '//*[@id="menu"]/ul/li[6]/ul/li[3]/ul/li[2]/ul/li[3]/a'
    comercios_financiacion = '//*[@id="menu"]/ul/li[6]/ul/li[3]/ul/li[2]/ul/li[4]/a'
    comercios_transaccion = '//*[@id="menu"]/ul/li[6]/ul/li[3]/ul/li[2]/ul/li[5]/a'
    comercios_aranceles = '//*[@id="menu"]/ul/li[6]/ul/li[3]/ul/li[2]/ul/li[6]/a'
    comercios_rubros = '//*[@id="menu"]/ul/li[6]/ul/li[3]/ul/li[2]/ul/li[7]/a'
    comercios_liquid = '//*[@id="menu"]/ul/li[6]/ul/li[3]/ul/li[3]/a'

    movimientos = '//*[@id="menu"]/ul/li[6]/ul/li[4]/a'
    mov_autorizaciones = '//*[@id="menu"]/ul/li[6]/ul/li[4]/ul/li[1]/a'
    mov_consumos = '//*[@id="menu"]/ul/li[6]/ul/li[4]/ul/li[2]/a'
    mov_ajustes = '//*[@id="menu"]/ul/li[6]/ul/li[4]/ul/li[4]/a'

    gestion_leyenda = '//*[@id="menu"]/ul/li[6]/ul/li[5]/a'

    gestion_uindex = '//*[@id="menu"]/ul/li[6]/ul/li[6]/a'

    promotores = '//*[@id="menu"]/ul/li[6]/ul/li[7]/a'

    pestana_establecimiento = '//*[@id="tab-0"]/a'
    boton_buscar_estab = '//*[@id="tab-container-0"]/header/form/fieldset[2]/div/button[1]'
    razon_social_global = '//*[@id="tab-container-0"]/div[3]/table/tbody/tr[1]/td[2]/div'

    logger.info('Ending the charge of attributes with path ')

# Now this class control the paths inside establecimientos
class AdqEstablecimiento(Adquirencia):
    # Declaramos variable que controla los tabs - Define logic for tabs.
    tab = 0
    estab_cod = f'//*[@id="tab-container-{tab}"]/header/form/fieldset[1]/div[1]/input'
    estab_razon = f'//*[@id="tab-container-{tab}"]/header/form/fieldset[1]/div[2]/input'
    estab_buscar_button = f'//*[@id="tab-container-{tab}"]/header/form/fieldset[2]/div/button[1]'
    estab_nuevo_button = f'//*[@id="tab-container-{tab}"]/header/form/fieldset[2]/div/button[2]'
    tab = 1
    estab_cod_tribut = f'//*[@id="tab-container-{tab}"]/form/div[1]/div/div[1]/div[1]/div/input'
    estab_razon_soc = f'//*[@id="tab-container-{tab}"]/form/div[1]/div/div[2]/div[1]/div/input'
    estab_pos_impositiva = f'//*[@id="tab-container-{tab}"]/form/div[1]/div/div[1]/div[2]/div/select'
    # Options will be managed by excel file
    op = 2
    estab_pos_impositiva_op = f'//*[@id="tab-container-{tab}"]/form/div[1]/div/div[1]/div[2]/div/select/option[{op}]'
    estab_fecha_creacion = f'//*[@id="tab-container-{tab}"]/form/div[1]/div/div[2]/div[2]/div/input'
    estab_calle = f'//*[@id="tab-container-{tab}"]/form/div[1]/div/div[3]/div[1]/div/input'
    estab_cp = f'//*[@id="tab-container-{tab}"]/form/div[1]/div/div[3]/div[5]/div/input'
    estab_localidad = f'//*[@id="tab-container-{tab}"]/form/div[1]/div/div[4]/div[1]/div/input'
    estab_provincia = f'//*[@id="tab-container-{tab}"]/form/div[1]/div/div[4]/div[2]/div/select'
    # Options will be managed by excel file
    op2 = 12
    estab_provincia_op = f'//*[@id="tab-container-{tab}"]/form/div[1]/div/div[4]/div[2]/div/select/option[{op2}]'
    estab_telefono = f'//*[@id="tab-container-{tab}"]/form/div[1]/div/div[4]/div[3]/div/input'
    estab_guardar = f'//*[@id="tab-container-{tab}"]/form/div[3]/div[1]/div/button[1]'

    # Define a method to create an establecimiento
    def crear_establecimientos(self):
        click(Adquirencia.adq_button)
        click(Adquirencia.gestion_establecimientos)
        click(self.estab_nuevo_button)

        # Send Keys, take data from Excel
        send_keys(self.estab_cod_tribut, estab_data['A2'].value)
        send_keys(self.estab_razon_soc, estab_data['B2'].value)
        click(self.estab_pos_impositiva)
        click(self.estab_pos_impositiva_op)
        send_keys(self.estab_fecha_creacion, estab_data['C2'].value)
        send_keys(self.estab_calle, estab_data['D2'].value)
        send_keys(self.estab_cp, estab_data['E2'].value)
        send_keys(self.estab_localidad, estab_data['F2'].value)
        click(self.estab_provincia)
        click(self.estab_provincia_op)
        send_keys(self.estab_telefono, estab_data['G2'].value)

        # Take the screenshot and save it
        screenshot('C:/Users/rguerra/Desktop/automatizacion')
        click(self.estab_guardar)

        # Take screenshot of the confirm screen
        screenshot('C:/Users/rguerra/Desktop/automatizacion')

        # Verify the data base with the data on excel
        con.execute(f"select razon_social from establecimientos where id_establecimiento = {estab_data['A2'].value}")
        razon_social = con.fetchall()
        # Validamos Establecimiento
        click(Adquirencia.pestana_establecimiento)
        click(Adquirencia.boton_buscar_estab)
        razon_social_global = Adquirencia.razon_social_global.get_attribute('value')

        if razon_social == razon_social_global:
            logger.info("Establecimiento dado de alta con exito")
        else:
            logger.error("Establecimiento no fue dado de alta")


