from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

from selenium_setup import *

import time
'''
class Historia20(LiveServerTestCase):  
    @classmethod
    def setUpClass(cls):
        setup_selenium()

    @classmethod
    def tearDownClass(cls):
        finalizar_selenium()
    
    def test_003_cenario2(self):
    
        driver = setup_selenium()

        default_page(driver)
        login()
'''

#FALTA ADICIONAR ESSE TESTE!!!!!!