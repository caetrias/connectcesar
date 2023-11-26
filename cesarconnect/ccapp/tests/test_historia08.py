from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

from selenium_setup import *

import time

class Historia08(LiveServerTestCase):
    @classmethod
    def setUpClass(cls):
        setup_selenium()

    @classmethod
    def tearDownClass(cls):
        finalizar_selenium()

    def test_004_scenario01(self):
        driver = setup_selenium()
    
        default_page(driver)
        login()

        #pesquisar por grupo
            #grupo não encontrado
        buscar_grupo = driver.find_element(By.ID, 'busca')
        buscar_grupo.send_keys("grupo10")
        time.sleep(1)

        pesquisar_grupo = driver.find_element(By.ID, 'pesquisa')
        pesquisar_grupo.click()
        time.sleep(1) 

    def test_004_scenario02(self):
        driver = setup_selenium()
    
        default_page(driver)
        login()

        #pesquisar por grupo
            #grupo encontrado
        buscar_grupo = driver.find_element(By.ID, 'busca')
        buscar_grupo.send_keys("grupo87")
        time.sleep(1)
        
        pesquisar_grupo = driver.find_element(By.ID, 'pesquisa')
        pesquisar_grupo.click()
        time.sleep(1)

    def test_004_scenario03(self):
        
        driver = setup_selenium()
        
        default_page(driver)
        login()

        #pesquisa o grupo
            #encontrado mais de um grupo com "grup"
        buscar_grupo = driver.find_element(By.ID, 'busca')
        buscar_grupo.send_keys("grup")
        time.sleep(1)
        pesquisar_grupo = driver.find_element(By.ID, 'pesquisa')
        pesquisar_grupo.click()
        time.sleep(1)

