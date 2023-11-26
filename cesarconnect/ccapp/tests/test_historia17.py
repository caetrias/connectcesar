from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

from selenium_setup import *

import time

class Historia17(LiveServerTestCase):  
    @classmethod
    def setUpClass(cls):
        setup_selenium()

    @classmethod
    def tearDownClass(cls):
        finalizar_selenium()   

    def test_007_cenario01(self):
        
        driver = setup_selenium()

        default_page(driver)
        login()
        
        #pesquisa usuario
        buscar_usuario = driver.find_element(By.ID, 'busca')
        buscar_usuario.send_keys("yan")
        time.sleep(1)

        pesquisar_usuario = driver.find_element(By.ID, 'pesquisa')
        pesquisar_usuario.click()
        time.sleep(1) 

        #acessa o usuario
            #usuário encontrado
        acesar_usuario = driver.find_element(By.ID, 'usuario_encontrado')
        acesar_usuario.click()
        time.sleep(1)

    def test_007_cenario02(self):
        
        driver = setup_selenium()

        default_page(driver)
        login()
        
        #pesquisa usuario
        buscar_usuario = driver.find_element(By.ID, 'busca')
        buscar_usuario.send_keys("bruno")
        time.sleep(1)

        pesquisar_usuario = driver.find_element(By.ID, 'pesquisa')
        pesquisar_usuario.click()
        time.sleep(1) 

        '''
        #acessa o usuario
            #mais de um usuário encontrado
        acesar_usuario = driver.find_element(By.ID, 'usuario_encontrado')
        acesar_usuario.click()
        time.sleep(1)
        '''

    def test_007_cenario03(self):
        
        driver = setup_selenium()

        default_page(driver)
        login()
        
        #pesquisa usuario
        buscar_usuario = driver.find_element(By.ID, 'busca')
        buscar_usuario.send_keys("allan")
        time.sleep(1)

        pesquisar_usuario = driver.find_element(By.ID, 'pesquisa')
        pesquisar_usuario.click()
        time.sleep(1) 

        #acessa o usuario
            #nenhum usuário encontrado
        '''
        acesar_usuario = driver.find_element(By.ID, 'usuario_encontrado')
        acesar_usuario.click()
        time.sleep(1)   
        '''
