import sys
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'pages')))

from login_page import LoginPage
from product_page import ProductPage

class TestAddToCart:
    def setUp(self):
        # Inicializando driver do navegador
        chrome_service = Service("C:\\WebDriver\\chromedriver.exe")
        self.driver = webdriver.Chrome(service=chrome_service)
        self.driver.get("https://www.saucedemo.com/")
        
        # Iniciando as páginas
        self.login_page = LoginPage(self.driver)
        self.product_page = ProductPage(self.driver)

    def test_add_to_cart(self):
        # Fazendo login
        self.login_page.login("standard_user", "secret_sauce")

        # Verificação de login
        assert self.login_page.is_login_successful(), "Login falhou!"

        # Acessando a página de produtos
        assert self.product_page.is_product_page(), "Página de produtos não carregada!"

        # Adiciona um produto ao carrinho e verifica se realmente foi adicionado
        self.product_page.add_product_to_cart()
        cart_count = self.product_page.get_cart_item_count()

        assert cart_count == "1", "Produto não foi adicionado ao carrinho!"
        
        # Mensagem indicando que o produto foi adicionado ao carrinho
        print("Produto adicionado ao carrinho!")

    def tearDown(self):
        # Espera para poder ver o resultado do teste
        time.sleep(5)
        self.driver.quit()

# Executa o teste
if __name__ == "__main__":
    test = TestAddToCart()
    test.setUp()
    test.test_add_to_cart()
    test.tearDown()