from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

from selenium_setup import *

import time

# Create a Chrome WebDriver instance

class Historia13(LiveServerTestCase):   
    @classmethod
    def setUpClass(cls):
        setup_selenium()

    @classmethod
    def tearDownClass(cls):
        finalizar_selenium() 

    def test_002_cenario2(self):
        
        driver = setup_selenium()

        default_page(driver)
        login()

        #pesquisa usuario
        buscar_perfil = driver.find_element(By.ID, 'busca')
        buscar_perfil.send_keys("edu")
        time.sleep(1)
        pesquisar_grupo = driver.find_element(By.ID, 'pesquisa')
        pesquisar_grupo.click()
        time.sleep(1)  