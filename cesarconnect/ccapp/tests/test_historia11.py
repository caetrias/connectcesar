from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

from selenium_setup import *

import time

class Historia11(LiveServerTestCase):  
    @classmethod
    def setUpClass(cls):
        setup_selenium()  

    @classmethod
    def tearDownClass(cls):
        finalizar_selenium()   

    def test_006_scenario01(self):
        
        driver = setup_selenium()

        default_page(driver)
        login()
        #seleciona meu grupo no nav bar
        editar_perfil = driver.find_element(By.ID, 'botao_meugrupo')
        editar_perfil.click()
        time.sleep(1)  

        # selecion a opção editar meu grupo
        editar_grupo = driver.find_element(By.ID, 'editargrupo')
        editar_grupo.click()
        time.sleep(1)
        #seleciona a opçao nome do grupo e altera
        editar_grupo = driver.find_element(By.ID, 'input_nome_grupo')
        editar_grupo.send_keys('Campo Minado')
        time.sleep(1)
    
        # seleciona e altera o periodo do grupo
        periodo_select = driver.find_element(By.ID, 'input_periodo_grupo')
        select = Select(periodo_select)
        select.select_by_visible_text("3º")  
        time.sleep(1)

       # selecion a opção editar DESCRIÇÃO
        editar_descricao = driver.find_element(By.ID, 'qualidades_grupo')
        editar_descricao.click()
        editar_descricao.send_keys('Corrida de chiken maluca em C')
        time.sleep(1)

        # Click the confirmation button
        confirmacao = driver.find_element(By.ID, 'botao_confirmar_grupo')
        confirmacao.click()
        time.sleep(1)

    def test_006_scenario02(self):
        
        driver = setup_selenium()

        default_page(driver)
        login()
        #seleciona meu grupo no nav bar
        editar_perfil = driver.find_element(By.ID, 'botao_meugrupo')
        editar_perfil.click()
        time.sleep(1)  

        # selecion a opção editar meu grupo
        editar_grupo = driver.find_element(By.ID, 'editargrupo')
        editar_grupo.click()
        time.sleep(1)
        #seleciona a opçao nome do grupo e altera
        editar_grupo = driver.find_element(By.ID, 'input_nome_grupo')
        editar_grupo.send_keys('chiken run')
        time.sleep(1)
    
        # seleciona e altera o periodo do grupo
        periodo_select = driver.find_element(By.ID, 'input_periodo_grupo')
        select = Select(periodo_select)
        select.select_by_visible_text("3º")  
        time.sleep(1)

        # selecion a opção editar DESCRIÇÃO
        editar_descricao = driver.find_element(By.ID, 'qualidades_grupo')
        editar_descricao.click()
        editar_descricao.send_keys('Corrida de chiken maluca em C')
        time.sleep(1)

        # Click the confirmation button
        confirmacao = driver.find_element(By.ID, 'botao_confirmar_grupo')
        confirmacao.click()
        time.sleep(1)