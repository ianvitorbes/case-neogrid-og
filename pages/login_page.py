# pages/login_page.py
from selenium.webdriver.common.by import By
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'pages')))


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username_field = (By.ID, "user-name")
        self.password_field = (By.ID, "password")
        self.login_button = (By.ID, "login-button")
        self.error_message = (By.XPATH, "//*[@data-test='error']")  # Caso haja erro

    # Método para inserir o nome de usuário
    def enter_username(self, username):
        self.driver.find_element(*self.username_field).send_keys(username)
    
    # Método para inserir a senha
    def enter_password(self, password):
        self.driver.find_element(*self.password_field).send_keys(password)
    
    # Método para clicar no botão de login
    def click_login(self):
        self.driver.find_element(*self.login_button).click()
    
    # Método para verificar se o login foi bem-sucedido
    def is_login_successful(self):
        return "Swag Labs" in self.driver.title

    # Método para verificar se há mensagem de erro de login
    def is_login_error(self):
        return "Epic sadface" in self.driver.find_element(*self.error_message).text

    # Método para realizar o login completo
    def login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()
