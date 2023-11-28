from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

import time

driver = None

def setup_selenium():
    global driver
    if driver is None:
        chrome_options = Options()
        chrome_options.add_argument("--headless")  # Rodar em modo headless
        chrome_options.add_argument("--no-sandbox")  # Necessário para CI/CD
        chrome_options.add_argument("--disable-dev-shm-usage")  # Evitar problemas de memória
        driver = webdriver.Chrome(options=chrome_options)
    return driver

def finalizar_selenium():
    global driver
    if driver:
        driver.quit()
        driver = None

    return driver

def default_page(chrome): 
    chrome.get('http://127.0.0.1:8000/')
    time.sleep(1)


def login():
    email_input = driver.find_element(By.ID, 'exampleInputEmail1')
    email_input.click()
    email_input.send_keys('migc@gmail.com' + Keys.RETURN)
    time.sleep(1)

    password_input = driver.find_element(By.ID, 'exampleInputPassword1')
    password_input.click()
    password_input.send_keys('marquinhos' + Keys.RETURN)
    time.sleep(1)
