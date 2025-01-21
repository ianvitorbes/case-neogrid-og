import sys
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

# Adiciona a pasta 'pages' ao sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'pages')))

# Importando as classes das páginas
from login_page import LoginPage
from product_page import ProductPage

class TestAddToCart:
    def setUp(self):
        # Inicializa o driver do Chrome
        chrome_service = Service("C:\\WebDriver\\chromedriver.exe")
        self.driver = webdriver.Chrome(service=chrome_service)
        self.driver.get("https://www.saucedemo.com/")  # Acesso à página de login
        
        # Inicializa as páginas
        self.login_page = LoginPage(self.driver)
        self.product_page = ProductPage(self.driver)

    def test_add_to_cart(self):
        # Faz o login com as credenciais válidas
        self.login_page.enter_username("standard_user")
        self.login_page.enter_password("secret_sauce")
        self.login_page.click_login()

        # Verifica se o login foi bem-sucedido
        assert self.login_page.is_login_successful(), "Login falhou!"

        # Acessa a página de produtos
        assert self.product_page.is_product_page(), "Página de produtos não carregada!"

        # Seleciona um produto e adiciona ao carrinho
        add_to_cart_button = self.driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack")
        add_to_cart_button.click()

        # Verifica se o produto foi adicionado ao carrinho
        cart_count = self.driver.find_element(By.CLASS_NAME, "shopping_cart_badge")
        assert cart_count.text == "1", "Produto não foi adicionado ao carrinho!"

    def tearDown(self):
        # Espera para poder ver o resultado do teste
        time.sleep(2)

        # Fecha o navegador após o teste
        self.driver.quit()

# Executa o teste
if __name__ == "__main__":
    test = TestAddToCart()
    test.setUp()
    test.test_add_to_cart()
    test.tearDown()
