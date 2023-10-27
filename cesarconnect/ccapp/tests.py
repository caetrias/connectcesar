#from django.test import TestCase
from selenium import webdriver
from selenium.webdriver.common.by import By  # Importe a classe By
from selenium.webdriver.common.keys import Keys  # Importe a classe Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Inicializa o driver do Chrome
driver = webdriver.Chrome()

# Navega para a página desejada
driver.get('http://127.0.0.1:8000/')
wait = WebDriverWait(driver, 10)
time.sleep(1)
#visualiza o input e escreve nele 
input_element = driver.find_element(By.ID, 'exampleInputEmail1')
input_element.click()
input_element.send_keys('edu@gmail.com' + Keys.RETURN)
time.sleep(1)
#visualiza o input e escreve nele 
input_element2 = wait.until(EC.presence_of_element_located((By.ID, 'exampleInputPassword1')))
input_element2.click()
input_element2.send_keys('1234' + Keys.RETURN)
time.sleep(1)
driver.quit()


