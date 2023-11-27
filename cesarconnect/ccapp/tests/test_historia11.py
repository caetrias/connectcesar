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
        editar_perfil = driver.find_element(By.ID, 'criar_grupo')
        editar_perfil.click()
        time.sleep(1)  # You can add a wait to allow the page to load, but it's better to use explicit waits

        # Find the "qualidades_usuario" element and send keys
        qualidades_usuario = driver.find_element(By.ID, 'nome_do_grupo')
        qualidades_usuario.send_keys('Apple Watchhh')
        time.sleep(1)

        # Find and clear the "nome_usuario" element, then send new keys
        editar_perfil = driver.find_element(By.ID, 'descricao_grupo')
        editar_perfil.clear()  # Clear the existing text, if any.
        editar_perfil.send_keys('Monitor de PC rodado a energia eolica')
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
        
        #seleciona meu grupo no nav bar
        editar_perfil = driver.find_element(By.ID, 'criar_grupo')
        editar_perfil.click()
        time.sleep(1)
         # Find the "qualidades_usuario" element and send keys
        qualidades_usuario = driver.find_element(By.ID, 'nome_do_grupo')
        qualidades_usuario.send_keys('Apple Watchh')
        time.sleep(1)

        # Find and clear the "nome_usuario" element, then send new keys
        editar_perfil = driver.find_element(By.ID, 'descricao_grupo')
        editar_perfil.clear()  # Clear the existing text, if any.
        editar_perfil.send_keys('Monitor de PC rodado a energia eolica')
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