from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

from selenium_setup import *

import time


class Historia01(LiveServerTestCase):
    @classmethod
    def setUpClass(cls):
        setup_selenium()

    @classmethod
    def tearDownClass(cls):
        finalizar_selenium()

    def test_000_setup(self):
        # Navega para a página desejada
        driver = setup_selenium()

        default_page(driver)

        #acessa criar perfil
        buscar_criar = driver.find_element(By.ID, 'confirmarcriar')
        buscar_criar.click()
        time.sleep(1)
        buscar_nome = driver.find_element(By.NAME, 'username')
        buscar_nome.click()
        buscar_nome.send_keys("alunopiloto")
        time.sleep(1)
        buscar_email = driver.find_element(By.NAME, 'email')
        buscar_email.click()
        buscar_email.send_keys("alunopiloto@gmail.com")
        time.sleep(1)
        buscar_senha = driver.find_element(By.NAME, 'senha')
        buscar_senha.click()
        buscar_senha.send_keys("1234" + Keys.RETURN)
        time.sleep(1)


 