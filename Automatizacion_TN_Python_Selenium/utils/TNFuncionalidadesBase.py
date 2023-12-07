from selenium import webdriver
from selenium.common.exceptions import TimeoutException, NoSuchElementException, ElementNotInteractableException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys # Importamos la clase Keys para poder usar las teclas especiales

from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from config.TNCredentials import *

class Selectores:
    COCKIE_BANNER = (By.XPATH, "//*[@id='container']/div[3]/div[2]/div/div[2]/a")
    AGREGAR_CARRITO1 = (By.CSS_SELECTOR, ".product-buy-btn.btn.btn-primary.js-prod-submit-form.js-addtocart.span12.cart")
    iniciar_compratn = (By. XPATH, "//*[@id='ajax-cart-submit-div']/input")
    MAIL_INGRESAR = (By. ID, "contact.email")
    selector_cp = (By. ID, "shippingAddress.zipcode")
    continuar = (By. XPATH, "//*[@id='main-column']/div[2]/form/div[2]/div[3]")
    envio = (By. CLASS_NAME, "selector")
    selector_DNI = (By. ID, "billingAddress.id_number")
    selector_nombre = (By. ID, "shippingAddress.first_name")
    selector_apellido = (By. ID, "shippingAddress.last_name")
    selector_calle = (By. ID, "shippingAddress.address")
    selector_numero = (By. ID, "shippingAddress.number")
    selector_departamento = (By. ID, "shippingAddress.floor")
    selector_barrio = (By. ID, "shippingAddress.locality")
    selector_ciudad = (By. ID, "shippingAddress.city")
    selector_CP_domicilio = (By. ID, "shippingAddress.zipcode")
    selector_continuar = (By. XPATH, "//*[@id='main-column']/div[2]/form/button/span")
    iframe_efectivo = (By. ID, "iFrameResizer0")
    selector_efectivo = (By.XPATH, "//*[@id='radio-option-custom_payment_cash_production']/label/div/div/div")
    selector_finalizar = (By.ID, "btnFinishCheckout")

class UtilidadesPruebas:
    """
    Clase que contiene las funcionalidades base para las pruebas automatizadas
    """
    def __init__(self, driver):
        self.driver = driver
        
    def esperar_por_los_elementos(self, localizador, timeout=10):
        """
        Función que espera por los elementos de la página
        """
        try:
            # Espere a que el elemento esté presente en el DOM y sea visible
            elemento = WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(localizador))
            
            # Espera a que el elemento sea visible
            
            WebDriverWait(self.driver, timeout).until(EC.visibility_of(elemento))
            
            # Espera a que el elemento esté habilitado para hacer click
            WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(elemento))
            
            return elemento
        except TimeoutException:
            
            raise AssertionError(f"El elemento {localizador} no estuvo listo")
        except NoSuchElementException:
            raise AssertionError(f"El elemento {localizador} no se encontró en la página")
        except ElementNotInteractableException:
            raise AssertionError(f"El elemento {localizador} no es interactuable")
        
class PaginaTN(UtilidadesPruebas):
    
    #Clase que contiene la funcionalidad para la pagina de inicio

    def __init__(self, driver):
        super().__init__(driver)
        self.Selectores = Selectores

    def cargar_pagina(self, url):
        """
        Función que carga la página principal que definamos en nuestra prueba
        """
        print(f"Cargando la página {url}")
        self.driver.get(url)
        self.driver.maximize_window()
        print("Página cargada")
        # assert "login" in self.driver.current_url, "La página no se cargo correctamente"
        

    def click_boton_cookie(self):
        """
        Función que hace click en el botón de Aceptar cookie
        """
        print("Haciendo click en el botón de Aceptar cookie")
        cookie = self.esperar_por_los_elementos(self.Selectores.COCKIE_BANNER)
        cookie.click()
        print("Botón de aceptar cookie clickeado")
        print("acepto las cookies exitosamente!!!!!")

class compraTN(UtilidadesPruebas):

    "Clase que contine las funcionalidades pra comprar en TN"
    def __init__(self, driver):
        super().__init__(driver)
        self.selectores = Selectores()

    def click_boton_agregar_carrito(self):
        """
        Función que hace click en el botón de Aceptar agregar al carritp
        """
        print("Haciendo click en el botón de agregar al carrito")
        agregar_carrito = self.esperar_por_los_elementos(self.selectores.AGREGAR_CARRITO1)
        agregar_carrito.click()
        print("Botón agregar al carrito clickeado")
        print("agrego al carrito exitosamente!!!!!")

    def click_boton_iniciar_compra(self):
        """
        Función que hace click en el botón de iniciar compra
        """
        print("Haciendo click en el botón iniciar compra")
        iniciar_compratn = self.esperar_por_los_elementos(self.selectores.iniciar_compratn)
        iniciar_compratn.click()
        print("Botón iniciar compra")
        print("inicio compra exitosamente!!!!!")
    
    def ingresar_mail(self, mail):
        """
        Función que ingresa el mail en el campo mail
        """
        print(f"Ingresando el usuario {mail}")
        mail_elemento = self.esperar_por_los_elementos(self.selectores.MAIL_INGRESAR)
        mail_elemento.send_keys(mail)
        assert mail_elemento.get_property("value") == mail, "El mail de usuario no se ingreso correctamente"
        print("mail ingresado")

    def ingresar_codigo_postal(self, codigo_postal):
        """
        Función que ingresa el codigo postal en el campo codigo postal
        """
        print(f"Ingresando el usuario {codigo_postal}")
        CP_elemento = self.esperar_por_los_elementos(self.selectores.selector_cp)
        CP_elemento.send_keys(codigo_postal)
        assert CP_elemento.get_property("value") == codigo_postal, "El codigo postal no se ingreso correctamente"
        print("codigo postal ingresado")

    def click_continuar(self):
        """
        Función que hace click en el botón de continuar
        """
        print("Haciendo click en el botón continuar")
        continuar_compra = self.esperar_por_los_elementos(self.selectores.continuar)
        continuar_compra.click()
        print("Botón continuar")
        print("Ha clickeado en el boton continuar exitosamente!!!!!")

    def click_boton_envio_gratis(self):
        """
        Función que hace click en el botón envio gratis
        """
        print("Haciendo click en el botón envio gratis")
        envio_gratis = self.esperar_por_los_elementos(self.selectores.envio)
        envio_gratis.click()
        print("Botón envio gratis")
        print("Ha clickeado en el boton envio gratis exitosamente!!!!!")

    def ingresar_DNI(self, DNI):
        """
        Función que ingresa DNI en el campo DNI o CUIL
        """
        print(f"Ingresando el DNI {DNI}")
        DNI_elemento = self.esperar_por_los_elementos(self.selectores.selector_DNI)
        DNI_elemento.send_keys(DNI)
        assert DNI_elemento.get_property("value") == DNI, "El DNI no se ingreso correctamente"
        print("DNI ingresado")

    def ingresar_nombre(self, nombre):
        """
        Función que ingresa el nombre en el campo nombre
        """
        print(f"Ingresando el nombre {nombre}")
        nombre_elemento = self.esperar_por_los_elementos(self.selectores.selector_nombre)
        nombre_elemento.send_keys(nombre)
        assert nombre_elemento.get_property("value") == nombre, "El nombre no se ingreso correctamente"
        print("nombre ingresado")

    def ingresar_apellido(self, apellido):
        """
        Función que ingresa el apellido en el campo apellido
        """
        print(f"Ingresando el apellido {apellido}")
        apellido_elemento = self.esperar_por_los_elementos(self.selectores.selector_apellido)
        apellido_elemento.send_keys(apellido)
        assert apellido_elemento.get_property("value") == apellido, "El apellido no se ingreso correctamente"
        print("apellido ingresado")

    def ingresar_calle(self, calle):
        """
        Función que ingresa el calle en el campo calle
        """
        print(f"Ingresando la calle {calle}")
        calle_elemento = self.esperar_por_los_elementos(self.selectores.selector_calle)
        calle_elemento.send_keys(calle)
        assert calle_elemento.get_property("value") == calle, "la calle no se ingreso correctamente"
        print("calle ingresada")

    def ingresar_numero(self, numero):
        """
        Función que ingresa el numero  en el campo numero
        """
        print(f"Ingresando el numero {numero}")
        numero_elemento = self.esperar_por_los_elementos(self.selectores.selector_numero)
        numero_elemento.send_keys(numero)
        assert numero_elemento.get_property("value") == numero, "el numero no se ingreso correctamente"
        print("numero ingresado")

    def ingresar_departamento(self, departamento):
        """
        Función que ingresa el departamento   en el campo departamento
        """
        print(f"Ingresando el departamento {departamento}")
        departamento_elemento = self.esperar_por_los_elementos(self.selectores.selector_departamento)
        departamento_elemento.send_keys(departamento)
        assert departamento_elemento.get_property("value") == departamento, "el departamento no se ingreso correctamente"
        print("departamento ingresado")

    def ingresar_barrio(self, barrio):
        """
        Función que ingresa el barrio   en el campo barrio
        """
        print(f"Ingresando el barrio {barrio}")
        barrio_elemento = self.esperar_por_los_elementos(self.selectores.selector_barrio)
        barrio_elemento.send_keys(barrio)
        assert barrio_elemento.get_property("value") == barrio, "el barrio no se ingreso correctamente"
        print("barrio ingresado")

    def ingresar_ciudad(self, ciudad):
        """
        Función que ingresa el ciudad   en el campo ciudad
        """
        print(f"Ingresando el ciudad {ciudad}")
        ciudad_elemento = self.esperar_por_los_elementos(self.selectores.selector_ciudad)
        ciudad_elemento.send_keys(ciudad)
        assert ciudad_elemento.get_property("value") == ciudad, "la ciuadd no se ingreso correctamente"
        print("ciudad ingresado")
    
    
    def ingresar_cp_domicilio(self, codigo_postal):
        """
        Función que ingresa el codigo postal   en el campo codigo postal
        """
        print(f"Ingresando el codigo postal {codigo_postal}")
        cp_elemento = self.esperar_por_los_elementos(self.selectores.selector_CP_domicilio)
        cp_elemento.send_keys(codigo_postal)
        assert cp_elemento.get_property("value") == codigo_postal, "el codigo postal  no se ingreso correctamente"
        print("codigo postal ingresado")

    def click_boton_continuar(self):
        """
        Función que hace click en el botón continuar
        """
        print("Haciendo click en el botón cotinuar")
        continuar_elemento = self.esperar_por_los_elementos(self.selectores.selector_continuar)
        continuar_elemento.click()
        print("Botón continuar")
        print("Ha clickeado en el boton continuar exitosamente!!!!!")

    def cambiar_a_iframe(self):
        entrar_iframe = self.esperar_por_los_elementos(self.selectores.iframe_efectivo)
        self.driver.switch_to.frame(entrar_iframe)
        print("Logro entrar al iframe del boton efectivo")
        
    def salir_iframe(self):
        self.driver.switch_to.default_content()
        print("Logro salir del iframe del boton efectivo")

    def Volver_a_contenido_original(self):
    #Si es necesario, puedes regresar al contexto principal (fuera del iframe)
        self.driver.switch_to.default_content()
    
    def clic_efectivo(self):
        # Ahora estamos dentro del iframe, puedes interactuar con los elementos dentro de él
        efectivo = self.esperar_por_los_elementos(self.selectores.selector_efectivo)
        efectivo.click()
        



    def click_boton_finalizar_pedido(self):
        """
        Función que hace click en el botón finalizar pedido
        """
        print("Haciendo click en el botón finalizar pedido")
        finalizar_elemento = self.esperar_por_los_elementos(self.selectores.selector_finalizar)
        finalizar_elemento.click()
        print("Botón finalizar pedido")
        print("Ha clickeado en el boton finalizar pedido exitosamente!!!!!")


