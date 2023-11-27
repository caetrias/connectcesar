from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

from selenium_setup import *

import time


class Historia20(LiveServerTestCase):
    @classmethod
    def setUpClass(cls):
        setup_selenium()

    @classmethod
    def tearDownClass(cls):
        finalizar_selenium()

    def test_020_scenario01(self):
        
        driver = setup_selenium()

        default_page(driver)
        login()
        #seleciona meu grupo no nav bar
        editar_perfil = driver.find_element(By.ID, 'botao_meugrupo')
        editar_perfil.click()
        time.sleep(1)  

        # selecion a opção deletar meu grupo
        deletar_grupo = driver.find_element(By.ID, 'deletargrupo')
        deletar_grupo.click()
        time.sleep(1)
        