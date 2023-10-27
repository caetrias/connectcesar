from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.by import By  # Importe a classe By
from selenium.webdriver.common.keys import Keys  # Importe a classe Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
driver = webdriver.Chrome()
class Historia11(LiveServerTestCase):
    def teste_000_setup(self):
       pass
       # Navega para a página desejada
       driver.get('http://127.0.0.1:8000/')
       time.sleep(1)
       #visualiza o input e escreve nele 
       input_element = driver.find_element(By.ID, 'exampleInputEmail1')
       input_element.click()
       input_element.send_keys('edu@gmail.com' + Keys.RETURN)
       time.sleep(1)
       #visualiza o input e escreve nele 
       input_element2 = driver.find_element(By.ID, 'exampleInputPassword1')
       input_element2.click()
       input_element2.send_keys('1234' + Keys.RETURN)
       time.sleep(3)
       #driver.quit()
    def tese_001_cenario1(self):
        input_element3 = driver.find_element(By.ID, 'botao_perfil'  + Keys.RETURN)
        input_element3.click()
        time.sleep(1)