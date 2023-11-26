from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

from selenium_setup import *

import time

class Historia18(LiveServerTestCase):
    @classmethod
    def setUpClass(cls):
        setup_selenium()

    @classmethod
    def tearDownClass(cls):
        finalizar_selenium()

    def test_008_scenario01(self):
        driver = setup_selenium()

        default_page(driver)

        login()

        #visualizar meu grupo
            #não estou em nenhum grupo
        ver_grupo = driver.find_element(By.ID, 'botao_meugrupo')
        ver_grupo.click()
        time.sleep(1)

    def test_008_scenario02(self):
        driver = setup_selenium()

        default_page(driver)

        login()

        '''
        #visualizar meu grupo
        meugrupo = driver.find_element(By.ID, 'botao_meugrupo')
        meugrupo.click()
        time.sleep(1)

        #não estou em nenhum grupo
        sem_acesso_grupo = driver.find_element(By.ID, 'sem_acesso')
        sem_acesso_grupo.click()
        time.sleep(1)

        default_page(driver)
        '''

        #criação de um grupo
        criacao_grupo = driver.find_element(By.ID, 'criar_grupo')
        criacao_grupo.click()
        time.sleep(1)

        nome_do_grupo = driver.find_element(By.ID, 'nome_do_grupo')
        nome_do_grupo.click()
        nome_do_grupo.send_keys("mainstreet")
        time.sleep(1)

        descricao_grupo = driver.find_element(By.ID, 'descricao_grupo')
        descricao_grupo.click()
        descricao_grupo.send_keys("grupo de estudo")
        time.sleep(1)

        periodo_select = driver.find_element(By.ID, 'periodo_grupo')
        select = Select(periodo_select)
        select.select_by_visible_text("3º")
        time.sleep(1)

        '''
        cria_grupo = driver.find_element(By.ID, 'confirma_grupo')
        cria_grupo.click()
        time.sleep(1)

        default_page(driver)

        #visualizar meu grupo
        meugrupo = driver.find_element(By.ID, 'botao_meugrupo')
        meugrupo.click()
        time.sleep(1)
        '''