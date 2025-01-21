import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class TestLogin(unittest.TestCase):

    def setUp(self):
        # Inicializa o chromedriver com o caminho do serviço
        chrome_service = Service("C:\\WebDriver\\chromedriver.exe")
        self.driver = webdriver.Chrome(service=chrome_service)

    def test_valid_login(self):
        driver = self.driver
        driver.get("https://www.saucedemo.com/")

        # Inserir credenciais
        username = driver.find_element(By.ID, "user-name")
        username.send_keys("standard_user")
        
        password = driver.find_element(By.ID, "password")
        password.send_keys("secret_sauce")
        
        # Clicar no botão de login
        login_button = driver.find_element(By.ID, "login-button")
        login_button.click()

        # Verificar se o login foi bem-sucedido
        assert "Swag Labs" in driver.title

        # Espera que o usuário pressione Enter para fechar
        input("Pressione Enter para fechar o navegador...")

    def tearDown(self):
        # Fechar o navegador após o teste
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
