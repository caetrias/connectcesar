from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

from .selenium_setup import *

import time

class Historia05(LiveServerTestCase):
    @classmethod
    def setUpClass(cls):
        setup_selenium()
        
    @classmethod
    def tearDownClass(cls):
        finalizar_selenium()

    def test_002_scenario01(self):
                
        driver = setup_selenium()

        default_page(driver)
        login()

        #editar perfil
        editar_perfil = driver.find_element(By.ID, 'botao_perfil')
        editar_perfil.click()
        time.sleep(1)

        qualidades_usuario = driver.find_element(By.ID, 'qualidades_usuario')
        qualidades_usuario.send_keys('Prestativo, presente e gente boa')
        time.sleep(1)

        editar_perfil = driver.find_element(By.ID, 'nome_usuario')
        editar_perfil.clear()
        editar_perfil.send_keys('Carlos Marinho')
        time.sleep(1)

        idade_usuario = driver.find_element(By.ID, 'idade_usuario')
        idade_usuario.clear()
        idade_usuario.send_keys('18')
        time.sleep(1)

        periodo_select = driver.find_element(By.ID, 'periodo_usuario')
        select = Select(periodo_select)
        select.select_by_visible_text("3º")
        time.sleep(1)

        curso_usuario = driver.find_element(By.ID, 'curso_usuario')
        curso_usuario.clear()
        curso_usuario.send_keys('Ciência da Computação')
        time.sleep(1)

        mbti_usuario = driver.find_element(By.ID, 'mbti_usuario')
        mbti_usuario.clear()
        mbti_usuario.send_keys('ISTJ')
        time.sleep(1)

        confirmacao = driver.find_element(By.ID, 'botao_confirmar')
        confirmacao.click()
        time.sleep(1)

        perfil = driver.find_element(By.ID, 'perfil')
        perfil.click()
        time.sleep(1)

        visualizar_perfil = driver.find_element(By.ID, 'visualizar_perfil')
        visualizar_perfil.click()
        time.sleep(1)
        
    
    def test_002_scenario02(self):
                
        driver = setup_selenium()

        default_page(driver)
        login()

        #editar perfil
        editar_perfil = driver.find_element(By.ID, 'botao_perfil')
        editar_perfil.click()
        time.sleep(1)

        qualidades_usuario = driver.find_element(By.ID, 'qualidades_usuario')
        qualidades_usuario.send_keys('Bom comunicador e bom solucionador de problemas')
        time.sleep(1)

        editar_perfil = driver.find_element(By.ID, 'nome_usuario')
        editar_perfil.clear()
        editar_perfil.send_keys('Silvio Augusto')
        time.sleep(1)

        idade_usuario = driver.find_element(By.ID, 'idade_usuario')
        idade_usuario.clear()
        idade_usuario.send_keys('16')
        time.sleep(1)

        periodo_select = driver.find_element(By.ID, 'periodo_usuario')
        select = Select(periodo_select)
        select.select_by_visible_text("1º")
        time.sleep(1)

        curso_usuario = driver.find_element(By.ID, 'curso_usuario')
        curso_usuario.clear()
        curso_usuario.send_keys('Design')
        time.sleep(1)

        mbti_usuario = driver.find_element(By.ID, 'mbti_usuario')
        mbti_usuario.clear()
        mbti_usuario.send_keys('ISTP')
        time.sleep(1)

        confirmacao = driver.find_element(By.ID, 'botao_confirmar')
        confirmacao.click()
        time.sleep(1)

        perfil = driver.find_element(By.ID, 'perfil')
        perfil.click()
        time.sleep(1)

        visualizar_perfil = driver.find_element(By.ID, 'visualizar_perfil')
        visualizar_perfil.click()
        time.sleep(1)
