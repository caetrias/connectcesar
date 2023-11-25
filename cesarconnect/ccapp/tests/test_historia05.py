from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

from selenium_setup import *

import time


class Historia5(LiveServerTestCase):

        @classmethod
        def setUpClass(cls):
                setup_selenium()

        @classmethod
        def tearDownClass(cls):
                finalizar_selenium()
        
        def teste000(self):
                driver = setup_selenium()

                default_page(driver)
                login()

                editar_perfil = driver.find_element(By.ID, 'botao_perfil')
                editar_perfil.click()
                time.sleep(1)  # You can add a wait to allow the page to load, but it's better to use explicit waits

                # Find the "qualidades_usuario" element and send keys
                qualidades_usuario = driver.find_element(By.ID, 'qualidades_usuario')
                qualidades_usuario.send_keys('Prestativo, Presente e Gente Boa')
                time.sleep(1)

                # Find and clear the "nome_usuario" element, then send new keys
                editar_perfil = driver.find_element(By.ID, 'nome_usuario')
                editar_perfil.clear()  # Clear the existing text, if any.
                editar_perfil.send_keys('Bruno Ribeiro')
                time.sleep(1)

                # Find and interact with "idade_usuario" element
                idade_usuario = driver.find_element(By.ID, 'idade_usuario')
                idade_usuario.clear()
                idade_usuario.send_keys('25')
                time.sleep(1)

                # Find the select element
                periodo_select = driver.find_element(By.ID, 'periodo_usuario')
                # Create a Select object
                select = Select(periodo_select)
                # Select an option by its visible text
                select.select_by_visible_text("3º")  # Replace "3º" with the option you want to select
                time.sleep(1)

                # Find and interact with "curso_usuario" element
                curso_usuario = driver.find_element(By.ID, 'curso_usuario')
                curso_usuario.clear()
                curso_usuario.send_keys('Ciência da Computação')
                time.sleep(1)

                # Find and interact with "mbti_usuario" element
                mbti_usuario = driver.find_element(By.ID, 'mbti_usuario')
                mbti_usuario.clear()
                mbti_usuario.send_keys('ISTJ')
                time.sleep(1)

                # Click the confirmation button
                confirmacao = driver.find_element(By.ID, 'botao_confrimar')
                confirmacao.click()
                time.sleep(1)