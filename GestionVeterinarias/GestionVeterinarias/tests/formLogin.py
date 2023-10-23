import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from django.test import LiveServerTestCase, TransactionTestCase, override_settings
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class MiPruebaSelenium(TransactionTestCase):
    def setUp(self):
        chrome_options = webdriver.ChromeOptions()
        #chrome_options.add_argument("--headless")  # Opcional: ejecutar en modo headless (sin interfaz gráfica)

        # Inicializa el controlador de Chrome
        self.browser = webdriver.Chrome(options=chrome_options)


    def tearDown(self):
        time.sleep(10)
        self.browser.quit()

    def test_inicio_de_sesion(self):
        # Abre la página de inicio de sesión
        self.browser.get('http://127.0.0.1:8000/cuentas/login')

      
        # Realiza acciones de prueba, por ejemplo, llenar campos y hacer clic en botones
        username_input = self.browser.find_element("id", "username")
        password_input = self.browser.find_element("id", "password")
        login_button = self.browser.find_element("id", "login")


        username_input.send_keys('juan.lopez')   
        password_input.send_keys('P@ssw0rd123')   
        login_button.submit()
        


        # Verifica el resultado esperado
        self.assertEqual(self.browser.current_url, 'http://127.0.0.1:8000/')

    