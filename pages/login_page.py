from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'pages')))

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username_field = (By.ID, "user-name")
        self.password_field = (By.ID, "password")
        self.login_button = (By.ID, "login-button")
        self.error_message = (By.XPATH, "//*[@data-test='error']")
        self.page_title = "Swag Labs"  # Título da página que deve ser carregada após login bem-sucedido

    def enter_username(self, username):
        """
        Inserção de usuário no campo de login.
        """
        username_input = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.username_field)
        )
        username_input.send_keys(username)

    def enter_password(self, password):
        """
        Inserção de senha no campo de login.
        """
        password_input = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.password_field)
        )
        password_input.send_keys(password)

    def click_login(self):
        """
        Clica no botão de login.
        """
        login_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.login_button)
        )
        login_button.click()

    def is_login_successful(self):
        """
        Verifica se o login foi bem-sucedido.
        Retorna True se o título da página contiver 'Swag Labs'.
        """
        WebDriverWait(self.driver, 10).until(
            EC.title_contains(self.page_title)
        )
        return True

    def is_login_error(self):
        """
        Verifica se ocorreu um erro no login, retornando True se a mensagem de erro for exibida.
        """
        try:
            WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located(self.error_message)
            )
            return "Epic sadface" in self.driver.find_element(*self.error_message).text
        except:
            return False

    def login(self, username, password):
        """
        Método completo para realizar o login.
        """
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()

        if self.is_login_successful():
            return True
        else:
            return False