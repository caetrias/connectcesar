from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

from .selenium_setup import *

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
        editar_perfil = driver.find_element(By.ID, 'criar_grupo')
        editar_perfil.click()
        time.sleep(1)  # You can add a wait to allow the page to load, but it's better to use explicit waits

        # Find the "qualidades_usuario" element and send keys
        qualidades_usuario = driver.find_element(By.ID, 'nome_do_grupo')
        qualidades_usuario.send_keys('Terça de Energia')
        time.sleep(1)

        # Find and clear the "nome_usuario" element, then send new keys
        editar_perfil = driver.find_element(By.ID, 'descricao_grupo')
        editar_perfil.clear()  # Clear the existing text, if any.
        editar_perfil.send_keys('Terça maneira')
        time.sleep(1)

        # Find the select element
        periodo_select = driver.find_element(By.ID, 'periodo_grupo')
        # Create a Select object
        select = Select(periodo_select)
        # Select an option by its visible text
        select.select_by_visible_text("4º")  # Replace "3º" with the option you want to select
        time.sleep(1)

        # Click the confirmation button
        confirmacao = driver.find_element(By.ID, 'confirma_grupo')
        confirmacao.click()
        time.sleep(1)
        editar_perfil = driver.find_element(By.ID, 'botao_meugrupo')
        editar_perfil.click()
        time.sleep(1)  

        # selecion a opção deletar meu grupo
        deletar_grupo = driver.find_element(By.ID, 'deletargrupo')
        deletar_grupo.click()
        time.sleep(1)

        '''
        #visualizar meu grupo
        meugrupo = driver.find_element(By.ID, 'botao_meugrupo')
        meugrupo.click()
        time.sleep(1)
        '''