from BasePageObject import *

def iniciar_sesion():
    login_username = send_keys('//*[@id="username"]', 'adminbatch')
    login_password = send_keys('//*[@id="password"]', 'GlobalProc')
    login_button = click('//*[@id="kc-login"]')

def screenshot():
    folder = 'path'
    file_name = 'nombre.png'
