#from django.test import TestCase
from selenium import webdriver
from selenium.webdriver.common.by import By  # Importe a classe By
from selenium.webdriver.common.keys import Keys  # Importe a classe Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Inicializa o driver do Chrome
driver = webdriver.Chrome()

# Navega para a página desejada
driver.get('http://127.0.0.1:8000/')
wait = WebDriverWait(driver, 10)
input_element = wait.until(EC.presence_of_element_located((By.NAME, 'exampleInputEmail1')))
input_element.click()
input_element.send_keys('Texto que você deseja inserir' + Keys.RETURN)
driver.quit()