import time
from utils.TNFuncionalidadesBase import *
from config.TNCredentials import *



options = webdriver.ChromeOptions()
# options.add_argument("--headless") #Que no se vea en la pantalla 
# options.add_argument("--sandbox")
# options.add_argument("--disable-dev-shm-usage")

service = ChromeService(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)


iniciar_TN = PaginaTN(driver)
iniciar_TN.cargar_pagina(login_url)
iniciar_TN.click_boton_cookie()

compra = compraTN(driver)
compra.click_boton_agregar_carrito()
compra.click_boton_iniciar_compra()
compra.ingresar_mail(mail)
compra.ingresar_codigo_postal(codigo_postal)
compra.click_continuar()
#compra.click_boton_envio_gratis()
#compra.ingresar_DNI(DNI)
compra.ingresar_nombre(nombre)
compra.ingresar_apellido(apellido)
compra.ingresar_calle(calle)
compra.ingresar_numero(numero)
compra.ingresar_departamento(departamento)
compra.ingresar_barrio(barrio)
#compra.ingresar_ciudad(ciudad)
#compra.ingresar_cp_domicilio(codigo_postal)
compra.click_boton_continuar()
#compra.cambiar_a_iframe()
#compra.clic_efectivo()
#compra.salir_iframe()
compra.click_boton_finalizar_pedido()

time.sleep(900)





