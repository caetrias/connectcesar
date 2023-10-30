from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

import time

# Create a Chrome WebDriver instance
driver = webdriver.Chrome()


def default_page():
     # Navega para a página desejada
        driver.get('http://127.0.0.1:8000/')
        time.sleep(1)
def login():
      # Visualiza o input e escreve nele
        email_input = driver.find_element(By.ID, 'exampleInputEmail1')
        email_input.click()
        email_input.send_keys('alunopiloto@gmail.com' + Keys.RETURN)
        time.sleep(1)

        # Visualiza o input e escreve nele
        password_input = driver.find_element(By.ID, 'exampleInputPassword1')
        password_input.click()
        password_input.send_keys('1234' + Keys.RETURN)
        time.sleep(1)
class Historia01(LiveServerTestCase):
    def test_000_setup(self):
         # Navega para a página desejada
        driver.get('http://127.0.0.1:8000/')
        time.sleep(1)
        #acessa criar perfil
        buscar_criar = driver.find_element(By.ID, 'confirmarcriar')
        buscar_criar.click()
        time.sleep(1)
        buscar_nome = driver.find_element(By.NAME, 'username')
        buscar_nome.click()
        buscar_nome.send_keys("alunopiloto")
        time.sleep(1)
        buscar_email = driver.find_element(By.NAME, 'email')
        buscar_email.click()
        buscar_email.send_keys("alunopiloto@gmail.com")
        time.sleep(1)
        buscar_senha = driver.find_element(By.NAME, 'senha')
        buscar_senha.click()
        buscar_senha.send_keys("1234" + Keys.RETURN)
        time.sleep(1)
class Historia11(LiveServerTestCase):
    def test_000_setup(self):
        default_page()
        login()
        
        #pesquisa o grupo
        buscar_perfil = driver.find_element(By.ID, 'busca')
        buscar_perfil.send_keys("ola")
        time.sleep(1)
        pesquisar_grupo = driver.find_element(By.ID, 'pesquisa')
        pesquisar_grupo.click()
        time.sleep(1)  

class Historia12(LiveServerTestCase):
    def test_001_setup(self):
        default_page()
        login()
        
        #pesquisa o grupo
        buscar_perfil = driver.find_element(By.ID, 'busca')
        buscar_perfil.send_keys("ola")
        time.sleep(1)
        pesquisar_grupo = driver.find_element(By.ID, 'pesquisa')
        pesquisar_grupo.click()
        time.sleep(1)
        #acessa o grupo  
        pesquisar_grupo = driver.find_element(By.ID, 'grupo_encontrado')
        pesquisar_grupo.click()
        time.sleep(1)  

class Historia13(LiveServerTestCase):       

    def test_002_cenario2(self):
            default_page()
            login()
            #pesquisa usuario
            buscar_perfil = driver.find_element(By.ID, 'busca')
            buscar_perfil.send_keys("edu")
            time.sleep(1)
            pesquisar_grupo = driver.find_element(By.ID, 'pesquisa')
            pesquisar_grupo.click()
            time.sleep(1)  

class Historia14(LiveServerTestCase):       

    def test_003_cenario2(self):
            default_page()
            login()
            #pesquisa usuario
            buscar_perfil = driver.find_element(By.ID, 'busca')
            buscar_perfil.send_keys("edu")
            time.sleep(1)
            pesquisar_grupo = driver.find_element(By.ID, 'pesquisa')
            pesquisar_grupo.click()
            time.sleep(1) 
            #acessa o usuario
            pesquisar_grupo = driver.find_element(By.ID, 'usuario_encontrado')
            pesquisar_grupo.click()
            time.sleep(1)  
           


"""
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

        # Close the browser window
        driver.close()
"""



    
