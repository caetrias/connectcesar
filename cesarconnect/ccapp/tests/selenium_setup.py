from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import time

driver = None

def setup_selenium():
    global driver
    if driver is None:
        driver = webdriver.Chrome()
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
